class Solution:
    def reverse(self, x: int) -> int:
        a = 2**31
        b = str(abs(x))
        c = ''
        for i in range(len(b)-1, -1, -1):
            c += b[i]
        if (not -a <= int(c) <= a-1) or (not -a <= x <= a-1):
            return 0
        else:
            return int(c) if x > 0 else int("-" + c)