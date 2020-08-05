num1 = int(input("Digite o primeiro Número: "))
num2 = int(input("Digite o segundo Número: "))
num3 = int(input("Digite o terceiro Número: "))

if num1 > num2 and num1 > num3:
    print(f"O maior número é o {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é o {num2}")
elif num3 > num1 and num3 > num1:
    print(f"O maior número é o {num3}")
else:
    print(f"os números {num1}, {num2}, {num3} são iguais")