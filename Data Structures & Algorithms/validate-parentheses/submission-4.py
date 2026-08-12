class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        brackets = {'(':')', '{':'}', '[':']'}
        order = []
        for b in s:
            print(b)
            if b in brackets:
                order.append(brackets[b])
                print(order)
            else:
                if len(order) == 0:
                    return False
                elif b == order[-1]:
                    order.pop()
                else:
                    return False
        if len(order) == 0:
            return True
        else:
            return False