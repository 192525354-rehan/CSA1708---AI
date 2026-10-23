from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)

for p in permutations(range(10), len(letters)):
    d = dict(zip(letters, p))

    if d['S'] == 0 or d['M'] == 0:
        continue

    send = int(''.join(str(d[c]) for c in word1))
    more = int(''.join(str(d[c]) for c in word2))
    money = int(''.join(str(d[c]) for c in result))

    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
