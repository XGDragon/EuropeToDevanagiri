# -*- coding: utf-8 -*-

import nltk
import pyphen
import lang
from lang import nl

# http://www.dutchgrammar.com/en/?n=SpellingAndPronunciation.04

language = 'nl-NL'

# try:
#     spelling = enchant.request_dict(language)
# except enchant.errors.DictNotFoundError as e:
#     raise e

class Phoneticate:
    def __init__(self, language):
        self.hyphen = pyphen.Pyphen(lang=language)
        self.phonetics = lang.languages[language]()

debug_text = u"een achterbadkamerdeur was schuw en stond wagenwijd en fatsoenlijk open vandaag, waarom zijn dan zeeën zo zout en egoïstisch?"
text = unicode(raw_input('Enter text: '), 'utf-8') if not debug_text else debug_text

words = nltk.word_tokenize(text.lower(), 'dutch', True)

words_nopunct = nltk.word_tokenize(text.lower().translate('`~!@#$%^&*()_+-=[]{}\\|;:\'",./<>?'), 'dutch', True)
word_dict = {x: hyphen.inserted(x) for x in words_nopunct}

for word in word_dict:
    word_dict[word] = phonetics.word_to_devanagari(word)

for w in range(len(words)):
    word = words[w]
    if word_dict.has_key(word):
        words[w] = word_dict[word]

print ' '.join(words)
