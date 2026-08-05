class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        total_p = 1
        flag = 0
        for i in nums:
            if i != 0:
                total_p *= i
            else:
                flag += 1
        for i in nums:
            if flag == 0:
                prod.append(total_p//i)
            elif flag == 1 and i != 0 or flag > 1:
                prod.append(0)
            elif flag == 1 and i == 0:
                prod.append(total_p)
        return prod
        