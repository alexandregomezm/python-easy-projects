class Solution():

    def isAnagram(self, s: str, t:str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} # hashmaps -> dictionaries

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # the function get defines 0 if its the first occurancy of that character
            countT[t[i]] = 1 + countT.get(t[i], 0)  

            # this part creates a hashmap that counts the characters in a word, for example: anagram -> {a:3, n:1, g:1, r:1, m:1}, and if the other word is an anagram, the count will be the same.  

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
            
        return True
    

s="anagram"
t="aaagmnr"
sol = Solution()
output = sol.isAnagram(s,t)
print(output)