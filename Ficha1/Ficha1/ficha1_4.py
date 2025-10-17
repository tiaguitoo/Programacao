distancia = int(input("Insira a distancia percorrida em km: "))
tempo = int(input("Insira a tempo em minutos: "))
resultado_km = (distancia / (tempo/60))
distancia_metro = distancia * 1000
resultado_ms = (distancia_metro / (tempo*60))
print("A distância em km/h é: ",resultado_km)
print("A distância em m/s é: ",resultado_ms)