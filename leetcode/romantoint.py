import random

class Solution: 
    def generate_roman(self):
        roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        size = random.randint(1,5)

        random_roman = ''.join(random.choice(roman_numerals) for _ in range(size)) # chatgpt made it, feeling useless :(

        return random_roman

    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V' : 5, 'X': 10, 'l' : 50, 'C': 100, 'D' : 500, 'M' : 1000}

        #CMXCVIII - example
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i+1]]:
                res -= roman_values[s[i]]
            else:
                res += roman_values[s[i]]
        
        return res
    
sol = Solution()
resp = sol.romanToInt("CMXCVIII")
print(resp)