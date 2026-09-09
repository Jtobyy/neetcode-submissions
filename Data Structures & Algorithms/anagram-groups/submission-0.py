class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            ang[sorted_word] = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            ang[sorted_word].append(word)

        groups = []
        for words in ang.values():
            anagrams = []
            for word in words:
                anagrams.append(word)
            
            groups.append(anagrams.copy())

        return groups
