num1 = int(input("Digite o primeiro Número: "))

maior = num1
menor = num1

num2 = int(input("Digite o segundo Número: "))
num3 = int(input("Digite o terceiro Número: "))

if maior < num2:
    maior = num2
elif maior < num3:
    maior = num3

if menor > num2:
    menor = num2
elif menor > num3:
    menor = num3

print(f"Os números digitados foram: {num1}, {num2}, {num3}")
print(f"O maior é: {maior}\nO menor é:{menor}")