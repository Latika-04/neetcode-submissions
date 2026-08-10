class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sdict = {}
        tdict = {}
        for letter in s:
            sdict[letter] = sdict.get(letter, 0) + 1
        for lettert in t:
            tdict[lettert] = tdict.get(lettert, 0) + 1
        return sdict == tdict

        