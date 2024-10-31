class Solution:
    
    def containsDuplicate(self, nums: list[int]) -> bool:

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                   return True
        return False        
                
nums = [1,2,3,4,4]
sol = Solution()
resp = sol.containsDuplicate(nums)
if resp == True:
    print("True")
else:
    print("False")