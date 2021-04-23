from itertools import permutations


def get_value(expression, op_idx, op_len, ops):
    if op_idx == op_len:
        return int(expression)
    elif "*" not in expression and "+" not in expression and "-" not in expression:
        return int(expression)
    else:
        cur_op = ops[op_idx]
        exp = expression.split(cur_op)

        result = get_value(exp[0], op_idx + 1, op_len, ops)
        for i in range(1, len(exp)):
            if cur_op == "*":
                result *= get_value(exp[i], op_idx + 1, op_len, ops)
            elif cur_op == "+":
                result += get_value(exp[i], op_idx + 1, op_len, ops)
            elif cur_op == "-":
                result -= get_value(exp[i], op_idx + 1, op_len, ops)
        return result


def solution(expression):
    answer = 0

    expression = expression

    operands_set = ["*", "+", "-"]
    operands_set = permutations(operands_set, len(operands_set))

    for operands in operands_set:
        value = get_value(expression, 0, 3, operands)
        if abs(value) > answer:
            answer = abs(value)

    return answer
