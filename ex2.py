carro = int(input("Digite a velocidade do carro: "))

if carro < 80:
    print("Você está dentro do limite")
else:
    multa = (carro - 80) * 7
    print(f"Você ultrapassou o limite! Sua multa será de R${multa:.2f}")