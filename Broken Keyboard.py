t = int(input())
for _ in range(t):
    s = input().strip()
    working = set()
    
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        count = 1
        while i + 1 < n and s[i+1] == ch:
            count += 1
            i += 1
        if count % 2 == 1:
            working.add(ch)
        i += 1
    
    print(''.join(sorted(working)))
