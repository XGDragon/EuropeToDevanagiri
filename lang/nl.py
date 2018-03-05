# -*- coding: utf-8 -*-
from phonetics import Phonetics


class DutchPhonetics(Phonetics):
    def _word_ruleset(self, word):
        t = DutchPhonetics._table

        if word == 'een':
            return t['mute'] + t['n']
        if word == '1':
            return t['ee'] + t['n']
        return word

    def _syllable_ruleset(self, syllables):
        for s in range(len(syllables)):
            e = len(syllables[s])
            ew = lambda suffix: syllables[s].endswith(suffix)
            sw = lambda prefix: syllables[s].startswith(prefix)
            ls = syllables[s - 1] if s > 0 else u''
            rs = syllables[s + 1] if s + 1 < len(syllables) else u''

            def r(key, start, end=-1):
                syllables[s] = Phonetics._replace_letters(syllables[s], self._table[key], start, end)

            if ew('uw'):
                r('uw', e - 2)
            if ew('eeuw'):
                r('eeu', e - 4)
            if ew('ieuw'):
                r('ieu', e - 4)

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
        'uw': 'ऊव',
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
