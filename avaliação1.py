

numeros = input()
par = 0
impar = 0
apenasDigitos = []
for caractere in numeros:
  if caractere.isdigit():
    apenasDigitos.append(caractere)

codigo_produto = list(map(int, apenasDigitos))

for i in codigo_produto[0:5]:
    if i in codigo_produto[::2]:
        impar += i

    else:
        par += i

divisao_inteira = (impar * 3 + par) // 10

resto_divisao = (impar * 3 + par) % 10

if resto_divisao > 0:
    digito_verificador = 10 - resto_divisao

    if codigo_produto[5] == digito_verificador:
        print(True)

    else:
        print(False)

if resto_divisao == codigo_produto[5]:
    print(True)