<<<<<<< HEAD
num1 = int(input("Digite o primeiro Número: "))
num2 = int(input("Digite o segundo Número: "))
num3 = int(input("Digite o terceiro Número: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"Ordem: {num1}, {num2}, {num3}")
    else:
        print(f"Ordem: {num1}, {num3}, {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"Ordem: {num2}, {num1}, {num3}")
    else:
        print(f"Ordem: {num2}, {num3}, {num1}")
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f"Ordem: {num3}, {num1}, {num2}")
    else:
        print(f"Ordem: {num3}, {num2}, {num1}")
else:
    print("Os números são iguais")
=======
num1 = int(input("Digite o primeiro Número: "))
num2 = int(input("Digite o segundo Número: "))
num3 = int(input("Digite o terceiro Número: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"Ordem: {num1}, {num2}, {num3}")
    else:
        print(f"Ordem: {num1}, {num3}, {num2}")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"Ordem: {num2}, {num1}, {num3}")
    else:
        print(f"Ordem: {num2}, {num3}, {num1}")
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f"Ordem: {num3}, {num1}, {num2}")
    else:
        print(f"Ordem: {num3}, {num2}, {num1}")
else:
    print("Os números são iguais")
>>>>>>> 283b0bc2ac016cc337ecfbebc53bcf24a4698b7d
