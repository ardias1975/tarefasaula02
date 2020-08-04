produto1 = float(input("Digite o preço do primeiro Produto: "))
produto2 = float(input("Digite o preço do segundo Produto: "))
produto3 = float(input("Digite o preço do terceiro Produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O produto 1 é o mais barato e custa R${produto1}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"O produto 2 é o mais barato e custa R${produto2}")
elif produto3 < produto1 and produto3 < produto2:
    print(f"O produto 3 é o mais barato e custa R${produto3}")
else:
    print(f"Os preços são iguais")