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
risco_areas = [0, 0, 0, 0, 0]
riscos_ciclos = []
nome_missao = "Orion Test Alpha"
equipe = "Equipe Apollo"

print("============================================================")
print("MISSION CONTROL AI")
print("============================================================")
print(f"Missão: {nome_missao}")
print(f"Equipe: {equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")

for i in range(len(dados_missao)):

    print("\n============================================================")
    print(f"CICLO {i + 1}")
    print("------------------------------------------------------------")

    temperatura = dados_missao[i][0]
    comunicacao = dados_missao[i][1]
    bateria = dados_missao[i][2]
    oxigenio = dados_missao[i][3]
    estabilidade = dados_missao[i][4]

    if temperatura < 18:
        status_temp = "ATENÇÃO"
        msg_temp = "Temperatura abaixo do ideal"
        risco_temp = 1

    elif temperatura <= 30:
        status_temp = "NORMAL"
        msg_temp = "Temperatura estável"
        risco_temp = 0

    elif temperatura <= 35:
        status_temp = "ATENÇÃO"
        msg_temp = "Temperatura elevada"
        risco_temp = 1

    else:
        status_temp = "CRÍTICO"
        msg_temp = "Risco de superaquecimento"
        risco_temp = 2
        
    if comunicacao < 30:
        status_com = "CRÍTICO"
        msg_com = "Comunicação com a base em nível crítico"
        risco_com = 2
        
    elif comunicacao <= 59:
        status_com = "ATENÇÃO"
        msg_com = "Comunicação instável"
        risco_com = 1
        
    else:
        status_com = "NORMAL"
        msg_com = "Comunicação estável"
        risco_com = 0

    if bateria < 20:
        status_bat = "CRÍTICO"
        msg_bat = "Bateria em nível crítico"
        risco_bat = 2

    elif bateria <= 49:
        status_bat = "ATENÇÃO"
        msg_bat = "Bateria abaixo do recomendado"
        risco_bat = 1

    else:
        status_bat = "NORMAL"
        msg_bat = "Energia estável"
        risco_bat = 0
        
    if oxigenio < 80:
        status_oxi = "CRÍTICO"
        msg_oxi = "Oxigênio em nível crítico"
        risco_oxi = 2

    elif oxigenio <= 89:
        status_oxi = "ATENÇÃO"
        msg_oxi = "Oxigênio abaixo do ideal"
        risco_oxi = 1

    else:
        status_oxi = "NORMAL"
        msg_oxi = "Oxigênio adequado"
        risco_oxi = 0

    if estabilidade < 40:
        status_est = "CRÍTICO"
        msg_est = "Estabilidade operacional crítica"
        risco_est = 2

    elif estabilidade <= 69:
        status_est = "ATENÇÃO"
        msg_est = "Estabilidade operacional reduzida"
        risco_est = 1

    else:
        status_est = "NORMAL"
        msg_est = "Estabilidade operacional adequada"
        risco_est = 0
        
    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    riscos_ciclos.append(risco_total)

    risco_areas[0] += risco_temp
    risco_areas[1] += risco_com
    risco_areas[2] += risco_bat
    risco_areas[3] += risco_oxi
    risco_areas[4] += risco_est

    if risco_total <= 2:
        classificacao = "MISSÃO ESTÁVEL"

    elif risco_total <= 5:
        classificacao = "MISSÃO EM ATENÇÃO"

    else:
        classificacao = "MISSÃO CRÍTICA"

    if risco_total == 0:
    recomendacao = (
        "Manter operação normal e continuar monitoramento."
    )

elif risco_total <= 2:
    recomendacao = (
        "Verificar controle térmico da missão."
    )

elif risco_total <= 5:
    recomendacao = (
        "Monitorar sistemas em atenção e preparar plano de "
        "contingência."
    )
else:
    recomendacao = (
        "Ativar modo de segurança e priorizar suporte à vida,\n"
        "energia e comunicação."
    )
    
print(f"Temperatura: {temperatura} °C | {status_temp} | {msg_temp}")
print(f"Comunicação: {comunicacao}% | {status_com} | {msg_com}")
print(f"Bateria: {bateria}% | {status_bat} | {msg_bat}")
print(f"Oxigênio: {oxigenio}% | {status_oxi} | {msg_oxi}")
print(f"Estabilidade: {estabilidade}% | {status_est} | {msg_est}")
print(f"Pontuação de risco do ciclo: {risco_total}")
print(f"Classificação do ciclo: {classificacao}")
print(f"Recomendação: {recomendacao}")

print("\n============================================================")
print("RELATÓRIO FINAL DA MISSÃO")
print("============================================================")

soma_temp = 0
soma_com = 0
soma_bat = 0
soma_oxi = 0
soma_est = 0

for ciclo in dados_missao:
    soma_temp += ciclo[0]
    soma_com += ciclo[1]
    soma_bat += ciclo[2]
    soma_oxi += ciclo[3]
    soma_est += ciclo[4]

quantidade_ciclos = len(dados_missao)

media_temp = soma_temp / quantidade_ciclos
media_com = soma_com / quantidade_ciclos
media_bat = soma_bat / quantidade_ciclos
media_oxi = soma_oxi / quantidade_ciclos
media_est = soma_est / quantidade_ciclos

maior_risco = max(riscos_ciclos)
indice_ciclo_critico = riscos_ciclos.index(maior_risco)

ciclos_criticos = 0

for risco in riscos_ciclos:
    if risco >= 6:
        ciclos_criticos += 1

risco_medio = sum(riscos_ciclos) / quantidade_ciclos

if riscos_ciclos[-1] > riscos_ciclos[0]:
    tendencia = "A missão apresentou tendência de piora."

elif riscos_ciclos[-1] < riscos_ciclos[0]:
    tendencia = "A missão apresentou tendência de melhora."

else:
    tendencia = "A missão permaneceu estável."

maior_pontuacao_area = max(risco_areas)
indice_maior_area = risco_areas.index(maior_pontuacao_area)
