def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            if brown == (i + yellow // i) * 2 + 4:
                answer = [max(i, yellow // i) + 2, min(i, yellow // i) + 2]
                break

    return answer
