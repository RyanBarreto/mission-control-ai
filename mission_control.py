dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50]
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

nome_missao = "Orion Test Alpha"
equipe = "Equipe Apollo"

print("MISSION CONTROL AI")
print(nome_missao)

for i in range(len(dados_missao)):

    print("\nCICLO", i + 1)

    temperatura = dados_missao[i][0]
    comunicacao = dados_missao[i][1]
    bateria = dados_missao[i][2]
    oxigenio = dados_missao[i][3]
    estabilidade = dados_missao[i][4]

    print("Temperatura:", temperatura)
    print("Comunicação:", comunicacao)
    print("Bateria:", bateria)

    if temperatura < 18:
    status_temp = "ATENÇÃO"

elif temperatura <= 30:
    status_temp = "NORMAL"

elif temperatura <= 35:
    status_temp = "ATENÇÃO"

else:
    status_temp = "CRÍTICO"

print(status_temp)
    print("Oxigênio:", oxigenio)
    print("Estabilidade:", estabilidade)
