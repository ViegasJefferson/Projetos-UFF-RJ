escala_richter = float(input())

if escala_richter < 0:
    print('Impossível')

elif escala_richter <= 1.9:
    print('Micro')

elif escala_richter <= 3.9:
    print('Pequeno')

elif escala_richter <= 4.9:
    print('Leve')

elif escala_richter <= 5.9:
    print('Moderado')

elif escala_richter <= 6.9:
    print('Forte')

elif escala_richter <= 8.9:
    print('Grande')

else:
    print('Muito Grande')