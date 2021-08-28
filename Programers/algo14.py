def solution(answer):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(0, len(answer)):
        if answer[i] ==p1[i%5]:
            c1 += 1
        if answer[i]==p2[i%8]:
            c2 += 1
        if p3[i%10]==answer[i]:
            c3 += 1

    lst = [0, c1, c2, c3]
    print(lst)
    top = max(lst)
    answers = []
    for i in range(len(lst)):
        if lst[i] == top:
            answers.append(i)
    return answers