def solution(name):
    answer = 0
    min_move = len(name) -1
    next = 0
    for x, i in enumerate(name):
        answer += min(ord(name[x]) - ord('A'), ord("Z") - ord(name[x]) + 1)

        next = x + 1
        while next < len(name) and name[next] == 'A':
            next += 1

            min_move = min(min_move, x + x + len(name) - next)
    answer += min_move
    return answer