# 

def frogger(a:int):
    if a<0 or a > n: return "death"
    if arr[a] == m: return "magical"
    if a == st: return "cycle"
    return 0


n, s, m = map(int, input().split())
st = s

arr = [0]*n
s1 = input().split()

for i in range(n):
    arr[i] = int(s1[i])

i = 0

while True:
    if arr
    r = frogger(s+arr[i])
    if r != 0:
        print(r,s+arr[i])
        break
    i = (i + 1) % n
