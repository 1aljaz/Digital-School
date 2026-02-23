# https://open.kattis.com/problems/aboveaverage

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    c = a[0]
    a = a[1:]
    p = sum(a)/c
    v = 0
    for ai in a:
        if ai > p:
            v += 1
    print(f"{v/c*100:.3f}%")
