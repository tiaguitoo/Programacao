
horas = float(input("Digite o número de horas trabalhadas na semana: "))
salario_hora = float(input("Digite o salário por hora: "))

if horas <= 40:
    ordenado = horas * salario_hora
else:
    horas_extras = horas - 40
    ordenado = (40 * salario_hora) + (horas_extras * salario_hora * 2)

print(f"O ordenado semanal é: ",ordenado," euros")