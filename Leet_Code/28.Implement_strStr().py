class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0:
            return 0
        answer = -1
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
            else:
                answer *= 1
        return answer  