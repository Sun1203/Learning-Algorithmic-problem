# (시간초과)
def solution(n):
    lst = [ x for i in range(1, n+1) for x in range(2, n+1) if x % i ==0]
    lst1 = [ lst[z] for z in range(len(lst)) if lst.count(lst[z]) < 3]
    return len(set(lst1))