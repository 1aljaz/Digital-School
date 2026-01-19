# https://open.kattis.com/problems/abc

a = list(map(int, input().split()))
s = input()
a.sort()
t = ""
for c in s:
    if c == "A":
        t +=str(a[0]) + " "
    elif c == "B":
        t +=str(a[1]) + " "
    elif c == "C":
        t +=str(a[2]) + " "

print(t.strip())