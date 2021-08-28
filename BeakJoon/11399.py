# ATM

nums=int(input())
score=list(map(int,input().split()))

answer = 0
score.sort()
mins = []

for i in range(nums):

    answer = ( answer + score[i])
    mins.append(answer)
    
    
print(sum(mins))