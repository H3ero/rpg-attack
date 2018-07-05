import random

strg = 10
weapon = 36

maxAttack = int("%.0f"%((weapon*5)+strg))
minAttack = int("%.0f"%((weapon*2)+strg))

for i in range(1):
    value = random.randint(minAttack, maxAttack)
    print(value)
