order = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
sentence = [sign for sign in input()]
oper_stack = []
for sign in sentence:
    # if sign is an alphabet.
    if sign.isalpha():
        print(sign, end="")
    # if operation stack is empty.
    elif not oper_stack:
        oper_stack.append(sign)
    # if sign is ")".
    elif sign == ")":
        while True:
            if oper_stack[-1] == "(":
                oper_stack.pop()
                break
            print(oper_stack.pop(), end="")
    # if sign is "(".
    elif sign == "(":
        oper_stack.append(sign)
    else:
        while True:
            if oper_stack and order[oper_stack[-1]] >= order[sign]:
                print(oper_stack.pop(), end="")
            else:
                break
        oper_stack.append(sign)

while oper_stack:
    print(oper_stack.pop(), end="")
