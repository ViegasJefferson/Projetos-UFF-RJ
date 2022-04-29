import numpy as np

preco_laptop = int(input())
poupanca_inicial = int(input())
primeiro_valor = int(input())

semana_valor = np.zeros(7)
semana_valor[0] = primeiro_valor
soma = poupanca_inicial + primeiro_valor
dias = 0
while (preco_laptop - soma) > 0:
  for indice in range(1,7):
    dias = dias + 1
    semana_valor[indice] = semana_valor[indice -1] + 1
    soma = soma + semana_valor[indice]
    if soma > preco_laptop:
      break
      print(dias)

  semana_valor[0] += 1
  soma = soma + semana_valor[0]
  semana_valor[1:] = 0
  dias = dias + 1

print(dias)