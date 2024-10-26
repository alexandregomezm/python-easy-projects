import random

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in values:
                return [values[diff], i]  # return the index of the diff value, and the index that gets that especifficaly diff value
            values[n] = i # values = {3:0, 4:1, 5:2, 6:3}   {n : i}

nums = [3,4,5,6]
target = 7
sol = Solution()
ans = sol.twoSum(nums, target)
print(ans)