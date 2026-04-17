n, k = map(int, input().split())
a = list(map(int, input().split()))

freq = {}
l = 0

max_len = 0
best_l = 0
best_r = 0

for r in range(n):
    # add element
    freq[a[r]] = freq.get(a[r], 0) + 1
    
    # shrink if too many distinct
    while len(freq) > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            del freq[a[l]]
        l += 1
    
    # update answer
    if r - l + 1 > max_len:
        max_len = r - l + 1
        best_l = l
        best_r = r

# convert to 1-based
print(best_l + 1, best_r + 1)

# codeforce link --> https://codeforces.com/problemset/problem/616/D
