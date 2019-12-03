#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_to_ipa

a simple text-to-IPA translator in Python 3

using CMU's pronouncing dictionary, @wwesantos' Arpabet-to-IPA dictionary, and spaCy 2.0 for tokenization

@mcarlisle

modified 20191203 again, why not

uses 
* words to arpabet: https://github.com/words/cmu-pronouncing-dictionary, https://github.com/cmusphinx/cmudict
* arpabet to ipa:   https://github.com/wwesantos/arpabet-to-ipa

"""

# -------------------------
#  START IMPORT STATEMENTS 
# -------------------------
import sys
import json
from spacy.lang.en import English
# -------------------------
#   END  IMPORT STATEMENTS
# -------------------------


# ------------------------
#  START GLOBAL VARIABLES 
# ------------------------
with open('cmu-pronouncing-dictionary.json', 'r') as f:
    cmudict = json.load(f)
with open('arpabet_ipa_dict.json', 'r') as f:
    ARPABET_IPA_dict = json.load(f)
# TODO we'll figure out how to put stresses in later
# ... perhaps a pull request would like to do it?
#with open('arpabet_ipa_dict_stress.json', 'r') as f:
#    ARPABET_IPA_dict_stress = json.load(f)
# ------------------------
#   END  GLOBAL VARIABLES 
# ------------------------


# ----------------------------------
#  START FUNCTION, CLASS DEFINITIONS 
# ----------------------------------
def cmu_ARPA_IPA_sub_word(word, stress=False):
    try:
        cmu = cmudict[word.lower()]
    except:  # if word not in cmudict, just leave it as is and return unchanged
        return word
    cmu_split = cmu.split(' ')
    IPA = ""
    for c in cmu_split:
        if stress:
            IPA = IPA + ARPABET_IPA_dict_stress[c] 
            # TODO - fix where accents go. Needs syllable-level parsing.
        else:
            IPA = IPA + ARPABET_IPA_dict[c]
    return IPA

def transliterate_to_ipa(doc):
	eng_parser = English() # initialize spaCy nlp object
	IPA_text   = doc
	IPA_object = eng_parser(doc)

	for i in range(len(IPA_object)):
	    IPA_text = IPA_text.replace(IPA_object[i].text, \
	    	cmu_ARPA_IPA_sub_word(IPA_object[i].text), 1)
	    # there shouldn't be bad replacements here because we are
	    # replacing just the first instance, which should be next in sequence

	return IPA_text

# ----------------------------------
#   END  FUNCTION, CLASS DEFINITIONS 
# ----------------------------------


# ------------
#  BEGIN MAIN 
# ------------

if __name__ == "__main__":

	def usage():
		print("\nThanks for trying text_to_ipa!")
		print("\nUsage: ")
		print("\nFor command-line text and terminal output: ")
		print("\npython text_to_ipa -t \"text\"") # 2 args
		print("\nFor text file input and terminal output: ")
		print("\npython text_to_ipa -f infile.txt") # 2 args
		print("\nFor text file input and text file output: ")
		print("\npython text_to_ipa -f infile.txt -o outfile.txt\n") # 4 args

	# simple CLI menu, no bells and whistles here
	if len(sys.argv) == 1:
		usage()

	elif sys.argv[1] == "-t":
		if len(sys.argv) == 3:
			doc = sys.argv[2] 
			# verify that python catches entire string in double quotes on command line
			print(transliterate_to_ipa(doc))
		else:
			usage()

	elif sys.argv[1] == "-f":

		if len(sys.argv) in (3,5):
			try:
				with open(sys.argv[2], "r") as f:
				    doc = f.read() # TODO verify this is text
				IPA_doc = transliterate_to_ipa(doc)
				if len(sys.argv) == 3: # print to terminal
					print(IPA_doc)
				elif len(sys.argv) == 5: # write out to output file
					if sys.argv[3] == "-o":
						try:
							with open(sys.argv[4], "w") as f:
								f.write(IPA_doc)
						except:
							print(f"text_to_ipa: could not write to output file {sys.argv[4]}")
				else:
					usage()

			except:
				print(f"text_to_ipa: input file {sys.argv[2]} not found")

		else:
			usage()

	else:
		usage()

	# TODO just put this in a Docker container w/ a spaCy virtual env
    
# ------------
#   END  MAIN 
# ------------

