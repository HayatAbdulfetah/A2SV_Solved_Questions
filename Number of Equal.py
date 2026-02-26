from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

countA = Counter(a)
countB = Counter(b)

total = 0

for value in countA:
    if value in countB:
        total += countA[value] * countB[value]

print(total)
