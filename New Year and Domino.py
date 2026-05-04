h, w = map(int, input().split())
grid = [input() for _ in range(h)]

hor = [[0]*w for _ in range(h)]

for i in range(h):
    for j in range(w-1):
        if grid[i][j] == '.' and grid[i][j+1] == '.':
            hor[i][j] = 1

ver = [[0]*w for _ in range(h)]

for i in range(h-1):
    for j in range(w):
        if grid[i][j] == '.' and grid[i+1][j] == '.':
            ver[i][j] = 1

def build_ps(arr):
    ps = [[0]*(w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            ps[i+1][j+1] = arr[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
    return ps

hor_ps = build_ps(hor)
ver_ps = build_ps(ver)

def get(ps, r1, c1, r2, c2):
    return ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    r1 -= 1; c1 -= 1

    ans = 0

    if c1 < c2:
        ans += get(hor_ps, r1, c1, r2, c2-1)

    if r1 < r2:
        ans += get(ver_ps, r1, c1, r2-1, c2)

    print(ans)
