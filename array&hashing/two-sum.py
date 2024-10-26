import random

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in values:
                return [values[diff], i]
            values[n] = i

nums = [3,4,5,6]
target = 7
sol = Solution()
ans = sol.twoSum(nums, target)
print(ans)