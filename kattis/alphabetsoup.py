# https://open.kattis.com/problems/alphabetsoup

s = input()
st = set(s)
alph = set("ABCDEFGHIJKLMNOPRSTUWVZQYX")
if len(st) == 26:
    print("ALPHABET SOUP!")
else:
    print(''.join(sorted(c for c in list(alph - st))))
