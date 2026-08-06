class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        strip = ""
        for l in s:
            if l != " " and l.isalnum():
                strip += l
        for i in range(-1, (-1)*(len(s)+1), -1):
            if s[i] != " " and s[i].isalnum():
                pal += s[i]
        if pal.casefold() == strip.casefold():
            return True
        else:
            return False