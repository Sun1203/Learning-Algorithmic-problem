from itertools import permutations
def is_prime(x):
    
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    lst = list(map(str, numbers))
    lst1 = []
    
    for i in range(1, len(lst)+1):
        result = list(permutations(lst,i))
        print(result)
        for x in range(len(result)):
            lee = int("".join(map(str, result[x])))
            
            if lee != 0 and lee != 1:
                if is_prime(lee):
                    lst1.append(lee)

    return len(set(lst1))