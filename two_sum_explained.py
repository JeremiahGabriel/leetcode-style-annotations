# Problem: Given an array of integers and a target value, return indices of two numbers that add up to the target.

def two_sum(nums, target):
    """
    Uses a hash map to find the two indices in a single pass.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}  # Maps number → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]  # Found the pair
        seen[num] = i  # Store current number's index
    return []  # No valid pair found
