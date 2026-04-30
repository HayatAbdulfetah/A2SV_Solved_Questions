from bisect import bisect_left

t = int(input())

for _ in range(t):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b.sort()

    prev = -10**18
    possible = True

    for x in a:

        best = 10**18

        if x >= prev:
            best = x

        need = prev + x

        idx = bisect_left(b, need)

        if idx < m:
            new_value = b[idx] - x
            best = min(best, new_value)

        if best == 10**18:
            possible = False
            break

        prev = best

    print("YES" if possible else "NO")



# problem link --> https://codeforces.com/problemset/problem/2065/C2
