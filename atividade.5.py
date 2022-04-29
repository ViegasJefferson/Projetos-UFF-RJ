import statistics

num_turmas, num_alunos, media_ap = [int(x) for x in input().split()]

lista_turmas = [[] for i in range(num_turmas)]

media = []
j = num_alunos
t = num_turmas
media_aprovada = 0

for i in range(t):
    nota = input().split()
    for v in nota:
        lista_turmas[i].append(float(v))
    media.append(statistics.mean(lista_turmas[i]))

for e in range(len(media)):

    if media[e] >= media_ap:
         media_aprovada += 1

percentual = (media_aprovada / num_turmas) * 100

for k in media:
    print(f'{k:.3f}')

print(f'{percentual:.2f}%')



