n, k = map(int, input().split())
a = list(map(int, input().split()))

diffs = [a[i+1] - a[i] for i in range(n-1)]

diffs.sort()

min_cost = sum(diffs[:n-k]) if k < n else 0

print(min_cost)


# problem's link --> https://codeforces.com/problemset/problem/1197/C
