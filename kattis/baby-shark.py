# https://open.kattis.com/problems/babyshark

besede = input().split()

zap = ("", 0)
trenutno = ("", 0)
for b in besede:
    if b != trenutno[0]:
        if trenutno[1] > zap[1]:
            zap = trenutno
        trenutno = (b, 1)
    else:
        trenutno = (b, trenutno[1]+1)
    
if trenutno[1] > zap[1]:
    zap = trenutno   

print(zap[0])