n,k = map(int,input().split())
a = list(map(int,input().split()))
seen = {}
check = 0
left = 0
ans = 0

for right in range(len(a)):
    if a[right] not in seen:
        seen[a[right]] = 0
    seen[a[right]] += 1

    while len(seen) > k:
        seen[a[left]] -= 1
        if seen[a[left]] == 0:
            del seen[a[left]]
        left += 1
    ans += right - left + 1

print(ans)
