# https://open.kattis.com/problems/acquirehardware
n, m = map(int, input())
row = [0 for _ in range(m)]
lst = [row for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(m):
        lst[i][j] = 1 if line[j] == "I" else 0
    