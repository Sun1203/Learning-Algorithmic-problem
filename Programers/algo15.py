import collections as cs

# (시간초과 X)
def solution(p, c):
    noCom = cs.Counter(p) - cs.Counter(c) 

    return list(noCom)[0]


# (시간초과)
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]