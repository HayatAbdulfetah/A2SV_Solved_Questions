t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    # count W in first window
    count_w = s[:k].count('W')
    ans = count_w
    
    for i in range(k, n):
        if s[i] == 'W':
            count_w += 1
        if s[i - k] == 'W':
            count_w -= 1
        
        ans = min(ans, count_w)
    
    print(ans)
