# https://open.kattis.com/problems/acappellarecording

n, d = map(int, input().split())
k = 1
s = set()
for _ in range(n):
    a = int(input())
    s.add(a)

s = sorted(list(s))
a=0
for i in range(1, len(s)):
    if abs(s[a] - s[i]) > d:
        a=i
        k+=1

print(k) 


