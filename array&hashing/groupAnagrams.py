class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if len(strs[i]) == len(strs(j)):    
                    countX, countY = {}, {}

                    countX[strs[i]] = 1 + countX.get(strs[i], 0)  # the function get defines 0 if its the first occurancy of that character
                    countY[strs[j]] = 1 + countY.get(strs[j], 0) 

                    for c in countX:
                        if countX[c] != countY.get(c, 0):
                            output.append(strs[i])
                        else:
                            output.append(strs[i], strs[j])

        return output

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]