import sys

m = int(sys.stdin.readline().split())
bit = 0
for _ in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "add":
        bit |= int(cmd[1])
    elif cmd[0] == "remove":
        pass
    elif cmd[0] == "check":
        pass
    elif cmd[0] == "toggle":
        pass
    elif cmd[0] == "all":
        pass
    elif cmd[0] == "empty":
        pass
