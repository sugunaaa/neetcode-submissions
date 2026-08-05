class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ''
        for i in strs:
            encoded_str = str(len(i)) + "#" + i
            encoded_s += encoded_str
        return encoded_s

    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])+1
            decoded.append(s[j+1:length+j])
            i = length+j
        return decoded