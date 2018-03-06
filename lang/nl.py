# -*- coding: utf-8 -*-
from phonetics import Phonetics


class DutchPhonetics(Phonetics):
    def _word_ruleset(self, word):
        t = DutchPhonetics._table

        if word == 'een':
            return t['mute'] + t['n']
        if word == 'en':
            return t['e'] + t['n']
        if word == '1':
            return t['ee'] + t['n']
        if word == 'terug':
            return t['t'] + t['r+'] + t['u'] + t['g']
        return word

    def _syllable_ruleset(self, syllables):
        newsyllables = [x for x in syllables]
        for s in range(len(syllables)):
            e = len(syllables[s])
            ew = lambda suffix: syllables[s].endswith(suffix)
            sw = lambda prefix: syllables[s].startswith(prefix)
            ls = syllables[s - 1] if s > 0 else ''
            rs = syllables[s + 1] if s + 1 < len(syllables) else ''

            def f(char, offset, other_chars):
                c = syllables[s].find(char)
                if c >= 0:
                    if offset + c >= len(syllables[s]) or offset + c < 0:
                        return False, c
                    return syllables[s][c + offset] in other_chars, c
                return False, c

            def r(key, start, end=-1):
                newsyllables[s] = Phonetics._replace_letters(newsyllables[s], self._table[key], start, end)

            # major exceptions
            if ew('ig') and not rs:
                r('mute', e - 2, e - 1)
            if ew('tie') and not rs:
                r('mute', e - 2, e - 1)
            if ew('cht') and rs.startswith('j'):
                r('null', e - 1)
            if ew('lijk') and not rs and ls and not ls.endswith('ge'):
                r('mute', e - 3, e - 1)

            # vowel combinations
            if ew('uw'):
                r('uw', e - 2)
            if ew('eeuw'):
                r('eeu', e - 4)
            if ew('ieuw'):
                r('ieu', e - 4)

            # ch exception for vowels
            ch = rs.startswith('ch')
            # e vowel
            if ew('e') and not [x for x in ('ee', 'oe', 'ie') if ew(x)]:
                if not rs or (not ls and syllables[s] in ('be', 'te', 'ge') and len(syllables) > 2):
                    r('mute', e - 1)
                elif not ch and rs:
                    r('ee', e - 1)
            if ew('en') and not [x for x in ('aen', 'een', 'oen', 'ien') if ew(x)]:
                if ls:
                    r('mute', e - 2, e - 1)
                elif len(syllables) == 1 and sw(self._vowels):
                    r('mute', e - 2, e - 1)

            if ew('i') and not ch and not [x for x in ('ai', 'ei', 'ui', 'oi') if ew(x)]:
                r('ie', e - 1)
            if ew('u') and not ch and not [x for x in ('uu', 'au', 'eu', 'ou') if ew(x)]:
                r('uu', e - 1)
            if ew('a') and not ch and not ew('aa'):
                r('aa', e - 1)
            if ew('o') and not ch and not ew('oo'):
                r('oo', e - 1)

            # accents
            newsyllables[s] = newsyllables[s].replace(u'éé', self._table[u'é'])
            newsyllables[s] = newsyllables[s].replace(u'é', self._table[u'é'])
            newsyllables[s] = newsyllables[s].replace(u'è', self._table[u'è'])

            # consonants
            if ew('b') and not rs:
                r('p', e - 1)
            if ew('d') and not rs:
                r('t', e - 1)

            Ct, C = f('c', 1, ('e', 'i'))
            if Ct:
                r('s', C, C + 1)
            Lt, L = f('l', 1, self._vowels)
            if Lt:
                r('l+', L, L + 1)
            Rt, R = f('r', 1, self._vowels)
            if Rt:
                r('r+', R, R + 1)
            Yt, Y = f('y', 1, self._vowels)
            if Yt:
                r('j', Y, Y + 1)

        return newsyllables

    # accents that do not change pronunciation, but intonation (and sometimes don't appear in Dutch anyways)
    # we replace accents with letters, then process them later into devanagiri
    _accents = {
        u'ç': 's',
        u'ë': 'e',
        u'ï': 'i',
        u'ö': 'o',
        u'ä': 'a',
        u'ü': 'u',
        u'à': 'a',
        u'á': 'a',
        u'ì': 'i',
        u'í': 'i',
        u'ò': 'o',
        u'ó': 'o',
        u'ù': 'u',
        u'ú': 'u'

    }

    _table = {
        'null': '',

        # short vowels
        'a': 'अ',
        'e': 'इ',
        'i': 'ऋ',
        'o': 'ओ',
        'u': 'उ',
        'y': 'य',

        # accents
        u'é': 'E', # == ee
        u'è': 'R', # == e

        # mute e / schwa
        'mute': 'Uh',

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
        'c': 'क',  # == k
        'd': 'डी',
        'f': 'फ',
        'g': 'ग',
        'h': 'ह',
        'j': 'ज',
        'k': 'क',
        'l': 'ल',
        'l+': 'ल',  # alternative when before a vowel (lopen)
        'm': 'म',
        'n': 'न',
        'p': 'प',
        'q': 'क्यू',  # == k
        'r': 'र',
        'r+': 'र',  # alternative when before a vowel (rennen)
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
        'ng': 'नग',
        'isch': 'नग'  # == ies
    }
