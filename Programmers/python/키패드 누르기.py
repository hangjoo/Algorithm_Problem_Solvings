def solution(numbers, hand):
    answer = ""

    l_col = 0
    l_row = 3

    r_col = 2
    r_row = 3

    for number in numbers:
        if number in [1, 4, 7]:
            l_col = 0
            l_row = number // 3
            answer += "L"

        elif number in [3, 6, 9]:
            r_col = 2
            r_row = number // 3 - 1
            answer += "R"

        else:
            m_col = 1
            if number in [2, 5, 8]:
                m_row = number // 3
            else:
                m_row = 3

            l_diff = abs(m_col - l_col) + abs(m_row - l_row)
            r_diff = abs(m_col - r_col) + abs(m_row - r_row)

            if l_diff < r_diff:
                l_col = m_col
                l_row = m_row
                answer += "L"
            elif l_diff > r_diff:
                r_col = m_col
                r_row = m_row
                answer += "R"
            elif l_diff == r_diff:
                if hand == "right":
                    r_col = m_col
                    r_row = m_row
                    answer += "R"
                elif hand == "left":
                    l_col = m_col
                    l_row = m_row
                    answer += "L"

    return answer
