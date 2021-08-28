class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = []
        for i in range(len(x)):
            y.append(x[i])
        if y[::-1] == y:
            return True
        else:
            return False