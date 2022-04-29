



zenit, polar = 'zZeEnNiItT', 'pPoOlLaArR'
texto_final = ''
palavra = input().strip()
texto = input().strip()

letra = 0
for i in range(len(texto[0:])):
    x = texto[letra]
    if x in zenit: x = int(zenit.find(texto[letra]));texto_final += polar[x]
    elif x in polar: x = int(polar.find(texto[letra]));texto_final += zenit[x]
    else: texto_final += texto[letra]
    letra += 1

contar = 0
for i in texto_final.split():
    if str(i.lower().replace(',','')) == str(palavra.lower()): contar += 1

print(f'{palavra}: {contar}')
print(texto_final)