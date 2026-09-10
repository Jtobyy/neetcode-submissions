class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = defaultdict(list)

        for str in strs:
            count = [0] * 26
            
            for alpha in str:
                count[ord(alpha) - ord('a')] += 1
            
            ang[tuple(count)].append(str)
        
        return list(ang.values())
