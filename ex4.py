dis = float(input("Digite a distancia em KM: "))

if dis <= 200:
    preço = 0.5 * dis
    print(f"O preço da passagem será de R${preço}")
else:
    preço = 0.45 * dis
    print(f"O preço da passagem será de R${preço}")