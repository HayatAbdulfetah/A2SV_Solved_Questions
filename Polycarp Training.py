n = int(input())
a = [int(n) for n in input().split()]
a.sort()
total = 0

for i in a:
    if i >= total + 1:
        total += 1
    else:
        continue

print(total)
