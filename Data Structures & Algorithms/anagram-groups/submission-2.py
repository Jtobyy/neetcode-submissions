class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            ang[sorted_str].append(str)
        
        return list(ang.values())
