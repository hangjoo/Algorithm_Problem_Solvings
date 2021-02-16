from math import sqrt

ax, ay, bx, by, cx, cy = list(map(int, input().split()))

pos = [[ax, ay], [bx, by], [cx, cy]]
pos = sorted(pos, key=lambda x: x[0])
x_inc = pos[1][0] - pos[0][0]
y_inc = pos[1][1] - pos[0][1]

if (ax - bx) == (ax - cx) == 0 or (ay - by) == (ay - cy) == 0:
    print(-1.0)
elif (ay - by) * (ax - cx) == (ay - cy) * (ax - bx):
    print(-1.0)
else:
    line_1 = sqrt((ay - by) ** 2 + (ax - bx) ** 2)
    line_2 = sqrt((by - cy) ** 2 + (bx - cx) ** 2)
    line_3 = sqrt((cy - ay) ** 2 + (cx - ax) ** 2)

    ret_max = max(line_1 + line_2, line_2 + line_3, line_3 + line_1)
    ret_min = min(line_1 + line_2, line_2 + line_3, line_3 + line_1)
    ret = (ret_max - ret_min) * 2
    print(ret)
