def solution(arr, comm):
    
    lst = []
    for i in range(len(comm)):
        arr1 = arr[comm[i][0]-1:comm[i][1]]
        arr1.sort()
        lst.append(arr1[comm[i][2]-1])
    return lst