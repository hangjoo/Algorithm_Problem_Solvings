def solution(gems):
    gem_num = len(set(gems))
    s_i = 0
    e_i = 0
    answer = [0, 100_000]
    gem_counts = {gems[0]: 1}
    while s_i < len(gems) and e_i < len(gems):
        if len(gem_counts) == gem_num:
            if e_i - s_i < answer[1] - answer[0]:
                answer[0] = s_i
                answer[1] = e_i
            if gem_counts[gems[s_i]] == 1:
                del gem_counts[gems[s_i]]
            else:
                gem_counts[gems[s_i]] -= 1
            s_i += 1
        else:
            e_i += 1
            if e_i == len(gems):
                break
            if gems[e_i] in gem_counts:
                gem_counts[gems[e_i]] += 1
            else:
                gem_counts[gems[e_i]] = 1

    return answer[0] + 1, answer[1] + 1
