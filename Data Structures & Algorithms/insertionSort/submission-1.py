# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sorted_pairs = []

        i = 0
        while i < len(pairs):
            j = i - 1
            curr_pos = i
            while j >= 0:
                if pairs[curr_pos].key < pairs[j].key:
                    pairs[j], pairs[curr_pos] = pairs[curr_pos], pairs[j]
                    curr_pos = j
                j -= 1
            
            i += 1
            sorted_pairs.append(list(pairs))
        
        return sorted_pairs


        