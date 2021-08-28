def solution(prices):
    answer =[0] * len(prices)
    for i in range(len(prices)):              
        for j in range(i+1, len(prices)):     
            if prices[i] <= prices[j]:     # 0 vs 1, 1 vs 2, 2 vs 3   
                answer[i]+=1                  
            else:
                answer[i]+=1
                break
    return answer