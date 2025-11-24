import math

def k67(n=67):
    return math.sqrt(n)

s = [1,2,3,4,5,6,7,8,9]

def k(sez:list):
    sez = sez.copy()
    sez[2] = 1

print(s)
k(s)
print(s)

print(k67())
