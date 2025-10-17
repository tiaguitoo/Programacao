num= int(input("Introduza um número: "))
segundos = num % 60
minutos = segundos / 60
horas = minutos / 24
dias = horas / 24
print("dias: ",dias ,"minutos: ",minutos,"segundos: ",segundos)