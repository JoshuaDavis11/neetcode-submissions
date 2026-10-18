class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmS = {}
        hmT = {}

        for char in s:
            if char in hmS:
                hmS[char] +=1
            else:
                hmS[char] = 1

        for char in t:
            if char in hmT:
                hmT[char] += 1
            else:
                hmT[char] = 1
            
    
        return hmS == hmT
        