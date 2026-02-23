# https://open.kattis.com/problems/akcija

n = int(input())
l = []
s = 0

for _ in range(n):
    l.append(int(input()))
    
l = sorted(l, reverse=True)

for i in range(n):
    if (i+1) % 3 == 0: continue
    s += l[i]
print(s)