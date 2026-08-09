class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        l, r = 0, 1
        win = [s[0]]
        max_l = 0
        idx = 0
        while r < len(s):
            if not s[r] in win:
                win.append(s[r])
            else:
                idx = win.index(s[r])
                l = idx+1
                win.append(s[r])
                del win[:idx+1]
            r+=1
            max_l = max(max_l, len(win))
        return max_l