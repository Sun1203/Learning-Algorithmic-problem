class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        answer = 0
        if len(s) == 1:
            return dic[s[0]]
        for idx, i in enumerate(s):
            if idx != len(s)-1:
                next = dic[s[idx+1]]

            if dic[i] >= next:
                answer += dic[i]
            else:
                answer += (-1 * dic[i])

        return answer