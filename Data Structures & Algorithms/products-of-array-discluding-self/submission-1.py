class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate it forwards
        sol = [1]*len(nums)
        for i in range(len(nums)):
            sol[i] = self.getProduct([*nums[0:i], *nums[i+1:]])
        return sol
    
    
    def getProduct(self, nums):
        product = 1
        for n in nums:
            product *= n
        return product


            

