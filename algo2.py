'''
 progress = 작업 진도율
 speed = 스피드!!
progresses [93, 30, 55]
speed      [1,  30,  5]
걸린시간    [7    3   9]
return[2, 1] -> 7일째에 2개의기능 배포, 9일째에 1개의 기능배포
'''


def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer



'''
1) 첫번째가 100이 될때까지 loop 를 돌며 time 을 늘린다. 

    else --> time+=1

2) (time =7) 이 되면  첫번째 값이93인놈이 100이 되어 if에 따라 pop 되고 count +=1

3) 현재 time 이 7이기 때문에 두번째 값(30)도 if에 따라 pop 되고 count +=1 
4) 세번째 값은 100이 안되기 때문에 loop를 돌며 time 을 늘리는데 
    2번과 달리 그전에 완성된 친구들 count 값이 있기 때문에 이 친구들을 출시해줘야함 
    따라서 answer 리스트에 append하고 count 초기화!!! 
    그후에 loop를 돌며 time 을 늘림
    여기까지 answer의 리스트 값은 [2] 이상태


5) 세번째 값(55)이 100을 넘으면 count +=1 하고 
    이 count 를 다시한번 answer 리스트에 append 해줌으로써 마지막 제품까지 출시 !
    마지막 count 1 을 answer 리스트에 넣으면 answer = [2, 1]!!!!!
'''