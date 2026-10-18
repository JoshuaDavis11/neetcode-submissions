class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequencyS, frequencyT = {},{}

        for i in range(len(s)):
            frequencyS[s[i]] = 1 + frequencyS.get(s[i],0)
            frequencyT[t[i]] = 1 + frequencyT.get(t[i],0)

        return frequencyS == frequencyT
        