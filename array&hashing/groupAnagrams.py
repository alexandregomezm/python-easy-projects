from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in output:
                output[sorted_word] = []
                
            output[sorted_word].append(word)
            
            # output = {
            # "act": ["act", "cat"],
            # "opst": ["pots", "tops", "stop"],
            # "aht": ["hat"]}

        return list(output.values())
            

strs = ["act", "pots", "tops", "cat", "stop", "hat"]
solution = Solution()
print(solution.groupAnagrams(strs))