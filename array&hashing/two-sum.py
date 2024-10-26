import random

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans
                else:
                    print("Não atingiu o target.")

# nums = [random.randint(1,10) for _ in range (5)]  #that array wil have 5 numbers, all sorted from 1 to 10.
nums = [3,4,5,6]
target = 7
sol = Solution()
twoSum = sol.twoSum(nums, target)
print(twoSum)