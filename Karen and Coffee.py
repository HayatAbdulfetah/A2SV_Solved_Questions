n, k, q = map(int, input().split())

maxx = 200002

diff = [0] * maxx

for _ in range(n):
    l, r = map(int, input().split())

    diff[l] += 1
    diff[r + 1] -= 1

count = [0] * maxx

running = 0

for i in range(maxx):
    running += diff[i]
    count[i] = running

good = [0] * maxx

for i in range(maxx):
    if count[i] >= k:
        good[i] = 1

pref = [0] * maxx

for i in range(1, maxx):
    pref[i] = pref[i-1] + good[i]

for _ in range(q):
    a, b = map(int, input().split())

    print(pref[b] - pref[a-1])


# problem link -->  https://codeforces.com/contest/816/problem/B
