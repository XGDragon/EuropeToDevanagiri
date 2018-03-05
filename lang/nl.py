# -*- coding: utf-8 -*-
import phonetics

class DutchPhonetics(phonetics.Phonetics):
    def _word_ruleset(self, word):
        t = DutchPhonetics._table

        if word == 'een':
            return t['mute'] + t['n']
        if word == '1':
            return t['ee'] + t['n']
        return word

    def _syllable_ruleset(self, syllables):
        return syllables

    _table = {
        # short vowels
        'a': 'अ',
        'e': 'इ',
        'i': 'ऋ',
        'o': 'ओ',
        'u': 'उ',
        'y': 'य',

        # mute e
        'mute': 'रे',

        # long vowels
        'aa': 'आ',
        'ee': 'ई',
        'ie': 'इए',
        'oo': 'ऊ',
        'uu': 'ऊ',

        # combined vowels
        'ae': 'ऐ',
        'ai': 'ई',
        'au': 'औ',
        'ei': 'इ',
        'eu': 'एउ',
        'ij': 'ए',  # == ei
        'oe': 'ओए',
        'oi': 'ओई',
        'ou': 'ओऊ',
        'ui': 'उई',
        'aai': 'आई',
        'oei': 'ओएइ',
        'ooi': 'ऊई',
        'uw': 'उव',
        'eeu': 'ईउ',  # these always end in w when its at the end
        'ieu': 'इएउ',  # these always end in w when its at the end

        # consonants
        'b': 'बी',
        'c': 'क',
        'd': 'डी',
        'f': 'फ',
        'g': 'ग',
        'h': 'ह',
        'j': 'ज',
        'k': 'क',
        'l': 'ल',
        'm': 'म',
        'n': 'न',
        'p': 'प',
        'q': 'क्यू',  # == k
        'r': 'र',
        's': 'स',
        't': 'टी',
        'v': 'व्',
        'w': 'व',
        'x': 'क्ष',
        'z': 'ज',

        # combined consonants
        'yj': 'जा',
        'th': 'थ',  # == t
        'ch': 'च',  # == g
        'sch': 'सच',
        'ng': 'नग'
    }