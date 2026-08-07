class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        rec = {}
        for i, num in enumerate(numbers):
            rec[num] = i+1
        for j, num in enumerate(numbers):
            if target - num in rec:
                return [j+1, rec[target-num]]
        return