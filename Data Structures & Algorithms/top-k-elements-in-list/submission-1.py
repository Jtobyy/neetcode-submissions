class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        solution = {}
        
        c = 0
        for num in nums:
            map[num] += 1

            if solution.get(num):
                solution[num] += 1
            elif c < k:
                solution[num] = 1
                c += 1

        for num in map:
            # get the current minimum value in solutions
            min_v = (0, min(solution.values()))
            for n in solution:
                if solution[n] <= min_v[1]:
                    min_v = (n, solution[n])

            if map[num] > min_v[1] and num not in solution:
                del solution[min_v[0]]
                solution[num] = map[num]
		
        return list(solution.keys())

