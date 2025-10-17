ano_bissexto = int(input("Indique o seu determinado ano: "))
if ano_bissexto % 4 and ano_bissexto % 100 != 0 or ano_bissexto % 400 == 0:
    print("O seu ano ",ano_bissexto," é bissexto!")
else:
    print("O seu ano não é bissexto!")
