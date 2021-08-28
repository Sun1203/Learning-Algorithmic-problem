def solution(x):
    l1 = list(str(x))
    z = []
    for i in range(len(l1)):
        z.append(int(l1[i]))
    
    if x % sum(z) == 0:
        return True
    else:
        return False