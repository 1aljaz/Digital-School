# https://open.kattis.com/problems/attendance2

n = int(input())
l = []
bil = True
for i in range(n):
    a = input()
    
    if a != "Present!":
        bil = False
    
    