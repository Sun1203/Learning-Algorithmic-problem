def solution(prices):
    n = len(prices)
    answer =[0] * n                         # 주식이 떨어진 시간
    for i in range(n):                      # i는 현재시간(초)이라고 생각함
        for j in range(i+1, n):             # J는 1초뒤 라고 생각함
            if prices[i] <= prices[j]:      # 만약 현재 주식가격이 1초뒤 주식 가격보다 작다면 
                answer[i]+=1                # answer 리스트의 i번째 인덱스 값에 1을 추가  
            else:   
                answer[i]+=1                # 만약 현재 주식가격이 1초뒤 주식 가격보다 크다면
                break                       # 멈춰!
    return answer