# https://open.kattis.com/problems/bottleopening

m = int(input())
n = int(input())

if n >= m:
    print("impossible")
else:
    for i in range(n):
        print(f"open {i+1} using {m}")