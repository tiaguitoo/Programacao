num1 = int(input("Introduza o seu primeiro número: "))
num2 = int(input("Introduza o seu segundo número: "))
num3 = int(input("Introduza o seu terceiro número: "))
if num1 > num2 and num1 > num3:
    print("O seu primeiro número é maior!")
if num2 > num1 and num2 > num3:
    print("O seu segundo número é maior!")
if num3 > num1 and num3 > num2:
    print("O seu terceiro número é maior!")