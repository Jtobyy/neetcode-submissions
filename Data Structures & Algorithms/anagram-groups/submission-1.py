class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for alpha in s:
                count[ord(alpha) - ord('a')] += 1

            anagrams[tuple(count)].append(s)

        return list(anagrams.values())
