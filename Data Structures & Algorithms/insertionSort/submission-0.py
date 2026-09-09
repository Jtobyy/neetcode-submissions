# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output_list = []

        for i in range(0, len(pairs)):
            curr_pos = i
  
            j = i - 1
            while j >= 0:
                if pairs[j].key > pairs[curr_pos].key:
                    temp1 = pairs[j]
                    temp2 = pairs[curr_pos]
                    pairs[curr_pos] = temp1
                    pairs[j] = temp2
                    curr_pos = j
                j -= 1

            new_pairs = pairs.copy()
            output_list.append(new_pairs)

        return output_list

        