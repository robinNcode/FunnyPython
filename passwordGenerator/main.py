import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
symbol = "(){[}]_/*@"

all = lower + upper + digit + symbol
passwordLen = 16

generate = int(input("how many password: "))

while generate > 0:
    password = "".join(random.sample(all, passwordLen))
    print(password)
    generate -= 1