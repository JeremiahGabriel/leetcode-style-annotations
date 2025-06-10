# Problem: Check if a string of brackets is valid (each open has a matching close in correct order)

def is_valid(s):
    """
    Uses a stack to track opening brackets.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack  # True if stack is empty (all closed)
