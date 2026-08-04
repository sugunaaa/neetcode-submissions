class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op = []
        dicts = {}
        l = {}
        for word in strs:
            l = {}
            for i in word:
                l[i] = l.get(i, 0) + 1
            if l in dicts.values():
                idx = next((k for k, v in dicts.items() if v == l), None)
                op[idx].append(word)
            else:
                dicts[len(op)] = l
                op.append([word])
        return op