class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        strip = ""
        for l in s:
            if l.isalnum():
                strip += l.casefold()
        for i in range(-1, (-1)*(len(s)+1), -1):
            if s[i].isalnum():
                pal += s[i].casefold()
        if pal == strip:
            return True
        else:
            return False