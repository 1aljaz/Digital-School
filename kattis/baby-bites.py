# https://open.kattis.com/problems/babybites

n = int(input())
words = input().split()

makes_sense = True

for i in range(n):
    if words[i] != "mumble":
        if int(words[i]) != i + 1:
            makes_sense = False
            break

if makes_sense:
    print("makes sense")
else:
    print("something is fishy")
