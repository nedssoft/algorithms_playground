"""
Problem statement#
Given an array of integers, move all the 0s to the back of the array while maintaining the relative order of the non-zero elements. 
Do this in-place using constant auxiliary space.
"""
from typing import List
def move_zeros(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

#Driver code
inputs = [[0,1,0,3,12], [0,0,1]]
for i in range(len(inputs)):
    print("Move zeros :",move_zeros(inputs[i]))
    
