# Problem: Find the contiguous subarray with the maximum sum.

def max_subarray(nums):
    """
    Implements Kadane's Algorithm.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        max_global = max(max_global, max_current)
    
    return max_global
