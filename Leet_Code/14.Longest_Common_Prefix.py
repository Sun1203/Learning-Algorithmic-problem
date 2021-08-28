class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=len)
        answer = ''

        for i in range(len(strs[0])):
            lst = []
            for x in strs:
                lst.append(x[i])
                
            if lst.count(strs[0][i]) == len(strs):
                answer += strs[0][i]
                
            elif lst.count(strs[0][0]) != len(strs):
                return answer
            
            else:
                break

        return answer