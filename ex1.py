import random

pc = random.randint(1, 6)

user = int(input("Digite um número: "))

if user == pc:
    print("Você ganhou!")
else:
    print(f"Você perdeu! O computado pensou no {pc}")
