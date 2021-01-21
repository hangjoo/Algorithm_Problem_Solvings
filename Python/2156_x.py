n = int(input())

num_list = []
max_list = []

for _ in range(n):
    num_list.append(int(input()))

for i in range(n):
    if i == 0:
        max_list.append((0, num_list[i], 0))
    elif i == 1:
        max_list.append((num_list[i - 1], num_list[i], num_list[i - 1] + num_list[i]))
    else:
        max_list.append((max_list[i - 1][2], max_list[i - 1][0] + num_list[i], max_list[i - 1][1] + num_list[i]))

print(max(max_list[-1]))
