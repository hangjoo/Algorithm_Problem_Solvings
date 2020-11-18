def gcd(numA: int, numB: int):
    if numB == 0:
        return numA
    else:
        return gcd(numB, numA % numB)


a, b = list(map(int, input().split()))
gcdNum = gcd(a, b) if a > b else gcd(b, a)
lcmNum = gcdNum * int(a / gcdNum) * int(b / gcdNum)
print(gcdNum)
print(lcmNum)