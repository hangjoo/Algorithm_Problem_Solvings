peopleDict = {old: [] for old in range(1, 201)}

countNum = int(input())
for _ in range(countNum):
    old, name = input().split()
    peopleDict[int(old)].append(name)

for old in peopleDict.keys():
    if len(peopleDict[old]) > 0:
        for name in peopleDict[old]:
            print("%d %s" % (old, name))