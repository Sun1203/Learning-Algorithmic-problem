def solution(arr, div):
    
    lst = []
    lst1 = []
    for i in arr:
        if i % div == 0:
            lst.append(i)
            lst.sort()
        elif i % div != 0:
            lst1.append(i)
            if len(arr) == len(lst1): 
                lst.append(-1)
    return lst