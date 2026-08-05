class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "empty"
        encoded = "vadapav".join(strs)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        decode = s.split("vadapav")
        return decode