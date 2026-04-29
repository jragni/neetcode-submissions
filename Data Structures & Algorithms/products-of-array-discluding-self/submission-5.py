class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize a res the smae length of nums 
        res = [1]*len(nums)
       
        # initialize the prod
        prod = 1

        # loop backwards to get postfix product
        for i in range(len(nums) - 1, -1, -1):
            # calculate res[i]
            res[i] = prod
            # update prod by multiplying nums
            prod *= nums[i]
        
        # reset prod to one
        prod = 1

        # loop forward
        for i in range(len(nums)):
            # calculate res
            res[i] *= prod
            # update prod
            prod *= nums[i]
        
        # return res
        return res