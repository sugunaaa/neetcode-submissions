class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for ind, i in enumerate(nums):
            if target - i in idx:
                return [idx[target-i], ind]
            else:
                idx[i] = ind
        return 