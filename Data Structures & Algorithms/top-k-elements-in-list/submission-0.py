class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for i in nums:
            count[i] = count.get(i,0) + 1
        if len(count) == 1:
            return [nums[0]]
        for j in range(1,k+1,1):
            m = next(k for k, v in count.items() if v == max(count.values()))
            result.append(m)
            del count[m]
        return result