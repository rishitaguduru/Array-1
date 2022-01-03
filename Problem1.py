import numpy as np

class Solution(object):
    def productExceptSelf(self, nums):
        # O(n**2) time complexity.. not ideal solution
#         output = [1] * (len(nums))
#         for i in range(0,len(nums)):
#             cur_val = nums[i]
#             self_val = output[i]
#             output = [element * cur_val for element in output]        
#             output[i] = self_val
#         return output
            
            
        #left array and right array
#         lp = 1
#         output =[1]*len(nums)
#         left_arr = [1]*len(nums)
#         right_arr = [1]*len(nums)
#         rp =1
#         for i in range(0,len(nums)) :
#             if(i==0):
#                 left_arr[0] = lp
#             else:
#                 lp = lp * nums[i-1]
#                 left_arr[i] = lp
#         for i in range(len(nums)-1,-1,-1):
#             if(i == len(nums)-1):
#                 right_arr[i]= rp
#             else:
#                 rp = rp*nums[i+1]
#                 right_arr[i] = rp
#         print(left_arr)
#         print (right_arr)
        
#         for i in range(0,len(nums)):
#             output[i] = left_arr[i]*right_arr[i]
        
#         return output
            
        #Optimising space complexity
        #TC - O(n)
        #SC - O(1)
        lp=1
        output =[1]*len(nums)
        rp =1
        for i in range(0,len(nums)) :
            if(i==0):
                output[0] = lp
            else:
                lp = lp * nums[i-1]
                output[i] = lp
        for i in range(len(nums)-1,-1,-1):
            if(i == len(nums)-1):
                output[i]= output[i]*rp
            else:
                rp = rp*nums[i+1]
                output[i] = output[i]*rp
        return output
        
            
 
        
