class Solution:
    def isValid(self, s: str) -> bool:

        
        lst = ['{([']
        stack = []
        for i in s:
            if i in lst[0]:
                stack.append(i)
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if i == ')':
                    if curr != "(":
                        return False    
                if i == ']':
                    if curr != "[":
                        return False
                if i == '}':
                    if curr != "{":
                        return False
                        
        if len(s) == 1 or len(stack) != 0:
            return False
        return True
        