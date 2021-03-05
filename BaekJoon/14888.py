from collections import deque

n = int(input())
nums = deque(map(int, input().split()))
operator = ["+", "-", "*", "/"]
operator_container = [operator[idx] for idx, num in enumerate(list(map(int, input().split()))) for _ in range(num)]

max_num = -1_000_000_000
min_num = 1_000_000_000

# helper function to calculate operator character
def calculate(num_1, num_2, operator):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        if num_1 < 0:
            return -(abs(num_1) // num_2)
        else:
            return num_1 // num_2


def func(cur_num, nums, operators):
    global min_num
    global max_num
    # Base Case
    if len(nums) == 1 and len(operators) == 1:
        final_num = calculate(cur_num, nums[0], operators[0])

        if final_num < min_num:
            min_num = final_num
        if final_num > max_num:
            max_num = final_num
    else:
        for operator in operators:
            # remove operator that used to calculate now.
            next_operators = operators.copy()
            next_operators.remove(operator)
            # hold current operand for next loop.
            next_num = nums.popleft()
            # call recursion.
            func(calculate(cur_num, next_num, operator), nums, next_operators)
            # save holding operand to nums variable.
            nums.appendleft(next_num)


func(nums.popleft(), nums, operator_container)

print(max_num, min_num)
