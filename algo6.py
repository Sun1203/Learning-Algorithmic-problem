'''
문제 - 서울에서 김서방 찾기

String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, 
"김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.

입출력 예
    seoul	                  return
["Jane", "Kim"]	        "김서방은 1에 있다"
'''

def soultion(seoul):
    
    for i in range(len(seoul)):                         # soultion함수의 매개변수값 리스트 값의 길이를 구함 
        if seoul[i]=="Kim":                             # 리스트의 인덱스값과 Kim이 일치하면
            return "김서방은 {}에 있다".format(i)        # 리턴값 출력



print(soultion(["a","b","c","Kim"]))    #    김서방은 3에 있다



