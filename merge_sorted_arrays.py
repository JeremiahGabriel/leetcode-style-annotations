# Problem: Merge two sorted arrays into one sorted array (without using sort())

def merge_arrays(nums1, nums2):
    """
    Merges two sorted lists in linear time.
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    merged = []
    i = j = 0
    
    # Merge until one list is exhausted
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Add remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    return merged
