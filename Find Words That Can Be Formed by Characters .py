class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        length = 0

        for word in words:
            word_count = Counter(word)
            good = True

            for ch in word_count:
                if word_count[ch] > char_count[ch]:
                    good = False
                    break

            if good:
                length += len(word)

        return length
