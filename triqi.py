import random

b = [[" "]*3 for _ in range(3)]
p = ["X", "O"]
while True:
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if b[x][y] == " ":
        b[x][y] = random.choice(p)
    for r in b:
        print(r)
    print("------")
    if all(c != " " for r in b for c in r):
        print("Fin del juego")
        break
