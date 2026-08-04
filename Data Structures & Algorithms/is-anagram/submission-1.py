class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters1 = {}
        letters2 = {}
        for letter in s:
            letters1[letter] = letters1.get(letter,0) + 1
        for letter in t:
            letters2[letter] = letters2.get(letter,0) + 1
        return letters1 == letters2