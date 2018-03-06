# -*- coding: utf-8 -*-

import nltk
import pyphen
import lang
import googletrans


# http://www.dutchgrammar.com/en/?n=SpellingAndPronunciation.04
class Phoneticate:
    def __init__(self, language):
        self._hyphen = pyphen.Pyphen(lang=language)
        self._phonetics = lang.languages[language]()
        self._translator = googletrans.Translator()
        self._trans_lang = language[0:2]

    def interpret(self, text):
        text = self._translator.translate(text, src=self._trans_lang, dest=self._trans_lang).text

        words = nltk.word_tokenize(text.lower(), 'dutch', True)

        words_nopunct = nltk.word_tokenize(text.lower().translate('`~!@#$%^&*()_+-=[]{}\\|;:\'",./<>?'), 'dutch', True)
        word_dict = {x: self._hyphen.inserted(x) for x in words_nopunct}

        for word in word_dict:
            word_dict[word] = self._phonetics.word_to_devanagari(word_dict[word])

        for w in range(len(words)):
            word = words[w]
            if word_dict.has_key(word):
                words[w] = word_dict[word]

        translation = self._translator.translate(text, src=self._trans_lang, dest='english').text
        return text, translation, ' '.join(words)


if __name__ == '__main__':
    debug_text = u"één eren kopen koperen achterbadkamerdeur was even schuw en stond wagenwijd en fatsoenlijk open vandaag, waarom zijn dan zeeën zo zout, egoïstisch en zachtjes? Klein zuchtje."
    sentence = unicode(raw_input('Enter text: '), 'utf-8') if not debug_text else debug_text

    phoneticate = Phoneticate('nl-NL')
    i, t, p = phoneticate.interpret(sentence)

    print u"Interpretation: {}".format(i)
    print u"Translation: \t{}".format(t)
    print u"Phonetic: \t\t{}".format(p)
