from itertools import combinations


def get_course_count(order, course):
    # 해당 order에서 course만큼의 가능한 조합 리스트를 반환함.
    if len(order) < course:
        return []
    else:
        combi = list(map(lambda x: "".join(sorted(x)), combinations(order, course)))
        return combi


def solution(orders, course):
    answer = []
    course_counts = {k: {} for k in course}

    # course_counts의 첫번째 키는 course, 두번째 키는 course만큼 가능한 조합.
    for order in orders:
        for k1 in course:
            for k2 in get_course_count(order, k1):
                if k2 not in course_counts[k1]:
                    course_counts[k1][k2] = 0
                course_counts[k1][k2] += 1

    # course마다 최대 값과 동일한 조합들을 answer에 담음. 이 때 최대 값이 2보다 작으면 무시되도록 설정.
    for course in course_counts.values():
        if len(course.values()) == 0:
            continue
        print(list(course.values()))
        max_count = max(course.values())
        if max_count < 2:
            continue
        for combi, count in course.items():
            if count == max_count:
                answer.append(combi)

    answer.sort()
    return answer
