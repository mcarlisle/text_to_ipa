Text-to-IPA basic translation: command-line tool

https://en.wikipedia.org/wiki/International_Phonetic_Alphabet

Resources: 
* words to arpabet:  https://github.com/words/cmu-pronouncing-dictionary, https://github.com/cmusphinx/cmudict
* arpabet to ipa:    https://github.com/wwesantos/arpabet-to-ipa
* tokenization, etc: https://spacy.io/ (requires spaCy in Python 3)

I'm sure this could use some improvements; please, submit a pull request!

Usage:
For command-line text and terminal output:

  python text_to_ipa -t "text"

For text file input and terminal output: 

  python text_to_ipa -f infile.txt

For text file input and text file output:

  python text_to_ipa -f infile.txt -o outfile.txt
  
Or, just play with it in <a href="text_to_ipa.ipynb">a Jupyter notebook</a>!
