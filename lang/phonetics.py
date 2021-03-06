class Phonetics:

    def __init__(self):
        assert type(self) is not Phonetics, "Cannot construct from base class"

        self._table_n = -1
        for k in self._table:
            self._table[k] = unicode(self._table[k], 'utf-8')
            if len(k) > self._table_n:
                self._table_n = len(k)

    def word_to_devanagari(self, word):
        for a in self._accents:
            word = word.replace(a, self._accents[a])

        syllables = word.split('-')

        # exceptions for words as a whole
        rword = self._word_ruleset(word)
        if rword != word:
            return rword

        rsyllables = self._syllable_ruleset(syllables)

        ntable = [[] for x in range(self._table_n)]
        for key in self._table:
            ntable[len(key) - 1].append(key)
        for n in range(self._table_n - 1, -1, -1):  # from big to small
            for key in ntable[n]:
                for s in range(len(rsyllables)):
                    rsyllables[s] = rsyllables[s].replace(key, self._table[key])

        return ''.join([h for h in rsyllables])

    @staticmethod
    def _replace_letters(word, replacement, start, end=-1):
        if end is -1:
            end = len(word)

        assert not start > end, 'start is larger than end'
        replaced = False
        letters = [x for x in word]
        for c in range(len(letters)):
            if start <= c < end:
                if replaced:
                    letters[c] = ''
                else:
                    letters[c] = replacement
                    replaced = True
        return ''.join(letters)

    def _word_ruleset(self, word):
        raise NotImplementedError

    def _syllable_ruleset(self, syllables):
        raise NotImplementedError

    _vowels = ('a', 'e', 'i', 'u', 'o', 'y')
    _accents = dict()
    _table = dict()
