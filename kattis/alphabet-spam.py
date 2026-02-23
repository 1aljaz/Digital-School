# https://open.kattis.com/problems/alphabetspam

l = input()

crke = [0, 0, 0, 0] # 0 - white space, 1 - lower case, 2 - upper case, 3 - simboli

for c in l:
    if ord(c) >= 65 and ord(c) <= 90:
        crke[2] +=1
    elif ord(c) == 95:
        crke[0] += 1
    elif ord(c) >= 97 and ord(c) <= 122:
        crke[1] += 1
    else:
        crke[3] += 1

for n in crke:
    print(n/len(l))
