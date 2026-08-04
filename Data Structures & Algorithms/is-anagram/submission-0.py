class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}
        for letter in s:
            if letter in letters1:
                letters1[letter] = letters1[letter] + 1
            else:
                letters1[letter] = 1
        for letter in t:
            if letter in letters2:
                letters2[letter] = letters2[letter] + 1
            else:
                letters2[letter] = 1
        if letters1 == letters2:
            return True
        return False