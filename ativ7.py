# times = int(input())
#
# campeonato = []
#
# for i in range(times):
#     nome_time = input(f' {i + 1} ')
#     vitorias = int(input())
#     empates = int(input())
#     derrotas = int(input())
#     gols_pro = int(input())
#     gols_contra = int(input())
#     pontos = vitorias * 3 + empates
#     campeonato.append([nome_time,pontos, vitorias, empates, derrotas, gols_pro, gols_contra])
#
# def myFunc(e):
#   return e[1]
#
# campeonato.sort(reverse=True, key=myFunc)
#
# for linha in campeonato:
#     print(*linha, sep= ',')

# times = int(input())
#
# campeonato = []
#
#
#
# for i in range(times):
#     nome_time = input().split(',')
#     campeonato.append(nome_time)

# vitórias =
# empates =
# for l in campeonato:
#     for c in l:
#         campeonato[l][1] = campeonato.extend(pontos)

# for linha in campeonato:
#     print(*linha, sep= ',')
#
# print()


times_entrada = []
qtd_times = int(input())
for qtd in range(qtd_times):
  times_entrada.append(input())



def ranking(times):
  tabela = []
  for time in times:
    team = time.split(',')
    lst_int = [int(x) for x in team[1:]]
    team_list = [team[0]] + [(lst_int[0]*3 + lst_int[1])] + lst_int
    tabela.append(team_list)

  tabela.sort(key=lambda row: (-row[1], -row[2], -(row[5]-row[6]), -row[5], row[0]))
  return tabela

for linha in ranking(times_entrada):
    print(*linha, sep= ',')
