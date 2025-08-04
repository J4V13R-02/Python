class Solution:
    s = "pataca"
    t = "tiburcio"

    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False
        return True
    if isAnagram(s, t) == False:
        print("no es anagrama")
    else:
        print("es anagrama")