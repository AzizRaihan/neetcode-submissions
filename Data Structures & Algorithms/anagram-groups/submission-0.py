class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s="".join(sorted(i))
            if s not in d:
                d[s]=[]
                d[s].append("".join(i))
            else:
                d[s].append("".join(i))

        return list(d.values())


        