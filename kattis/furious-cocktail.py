# https://open.kattis.com/problems/cocktail

n, t = map(int, input().split())

a = []

for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)
b = True
for i in range(n):
    for j in range(i):
        a[j]-=t
        if sum(a) > 0 and a[0] == 0:
            b = False
            break 
print("YES" if b else "NO")