class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_str = {}
        for word in strs:
            x = ''.join(sorted(word))
            if x in dict_str:
                dict_str[x].append(word)
            else:
                dict_str[x] = [word]
        return list(dict_str.values())
