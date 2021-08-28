def solution(citations):
    citations.sort()
    lst1 = []
    for i in range(len(citations)):
        if citations[i] >= len(citations[i:]):
            lst1.append(i)

    return len(lst1)