import sys
t = int(input())
my_phone_book = dict()
for _ in range(t):
    info = input().split()
    my_phone_book[info[0]] = info[1]
    

for line in sys.stdin:
    name = line.strip()
    if not name:
        break
    elif name in my_phone_book :
        print(name+"="+ my_phone_book[name])
    else:
        print("Not found")
