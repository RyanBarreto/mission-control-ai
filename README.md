# Sistema de Monitoramento Espacial

## Descrição do Projeto

Este projeto consiste em um sistema de monitoramento operacional de uma missão espacial fictícia chamada Nebula Explorer IX.

O programa foi desenvolvido em Python com o objetivo de simular o funcionamento de uma central de monitoramento responsável por acompanhar o estado de sistemas críticos de uma nave espacial durante diferentes ciclos operacionais.

Durante a execução, o sistema analisa indicadores importantes da missão, identifica possíveis falhas, calcula níveis de risco e gera relatórios detalhados sobre o estado da operação.

Além da análise individual de cada ciclo, o programa também produz um relatório final contendo médias gerais, tendências operacionais, quantidade de ciclos críticos e identificação do sistema mais afetado durante a missão.

## Objetivo do Sistema

O principal objetivo do sistema é monitorar continuamente dados operacionais da missão e transformar essas informações em análises de risco que auxiliem a tomada de decisões.

O programa busca simular cenários reais de monitoramento espacial, nos quais pequenas alterações em sistemas críticos podem comprometer toda a operação.

## Estrutura dos Dados

Os dados da missão são armazenados na variável:

```python
dados_missao = [
    [22, 95, 90, 98, 93],
    [26, 82, 76, 95, 88],
    [30, 68, 61, 90, 73],
    [35, 50, 44, 86, 60],
    [38, 35, 22, 79, 40],
    [33, 58, 37, 84, 57]
]
```

Cada lista interna representa um ciclo operacional da missão.

A ordem dos dados é:

```python
[
    temperatura,
    comunicacao,
    bateria,
    oxigenio,
    estabilidade
]
```
Exemplo:

```python
[22, 95, 90, 98, 93]
```
Significa:

| Indicador | Valor |
|---|---|
| Temperatura | 22 °C |
| Comunicação | 95% |
| Bateria | 90% |
| Oxigênio | 98% |
| Estabilidade | 93% |

## Sistemas Monitorados

O programa monitora cinco sistemas principais da nave espacial.

### Controle térmico

Responsável por monitorar a temperatura interna da nave.

Temperaturas muito altas podem causar superaquecimento dos sistemas eletrônicos. Temperaturas muito baixas podem comprometer equipamentos sensíveis.

### Comunicação

Responsável por verificar a qualidade do sinal de comunicação da nave.

Falhas na comunicação podem dificultar o envio de informações entre a missão e a central de controle.

### Reserva energética

Monitora o nível de bateria disponível para os sistemas da nave.

Níveis baixos de energia podem comprometer o funcionamento de equipamentos essenciais.

### Sistema de suporte vital

Controla o nível de oxigênio disponível.

Valores abaixo do seguro representam risco direto para a sobrevivência da tripulação.

### Controle estrutural

Monitora a estabilidade estrutural da nave.

Oscilações estruturais podem indicar danos físicos ou falhas mecânicas.

## Funcionamento do Programa

O sistema percorre todos os ciclos operacionais utilizando um laço de repetição:

```python
for i in range(len(dados_missao)):
```

A cada ciclo, o programa:

- Coleta os dados do ciclo atual
- Analisa cada sistema individualmente
- Define status operacionais
- Calcula pontuações de risco
- Classifica o estado geral da operação
- Exibe recomendações
- Armazena dados para o relatório final

## Sistema de Classificação

Cada indicador possui regras específicas de análise.

### Temperatura

```python
if temperatura < 18:
```
Temperaturas abaixo de 18 °C geram estado de atenção.
```python
elif temperatura <= 30:
```
Temperaturas entre 18 °C e 30 °C são consideradas normais.
```python
elif temperatura <= 35:
```
Temperaturas acima de 30 °C indicam aquecimento moderado.
```python
else:
```
Temperaturas acima de 35 °C representam risco crítico.

### Comunicação

A qualidade do sinal é analisada em porcentagem.

| Faixa | Status |
|---|---|
| Menor que 30% | CRÍTICO |
| 30% até 59% | ATENÇÃO |
| Acima de 59% | NORMAL |

### Bateria

O sistema verifica a quantidade de energia restante.

| Faixa | Status |
|---|---|
| Menor que 20% | CRÍTICO |
| 20% até 49% | ATENÇÃO |
| Acima de 49% | NORMAL |

### Oxigênio

O nível de oxigênio é essencial para manter condições seguras na nave.

| Faixa | Status |
|---|---|
| Menor que 80% | CRÍTICO |
| 80% até 89% | ATENÇÃO |
| Acima de 89% | NORMAL |

### Estabilidade Estrutural

Analisa a integridade física da nave.

| Faixa | Status |
|---|---|
| Menor que 40% | CRÍTICO |
| 40% até 69% | ATENÇÃO |
| Acima de 69% | NORMAL |

## Sistema de Pontuação de Risco

Cada sistema recebe uma pontuação baseada no seu estado.

| Status | Pontuação |
|---|---|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

Essas pontuações são somadas:

```python
risco_total = (
    risco_temp +
    risco_com +
    risco_bat +
    risco_oxi +
    risco_est
)
```
O resultado representa o nível geral de risco do ciclo operacional.

## Classificação Operacional

Com base na pontuação total, o ciclo recebe uma classificação.

| Pontuação | Classificação |
|---|---|
| 0 até 2 | OPERAÇÃO ESTÁVEL |
| 3 até 5 | OPERAÇÃO EM ALERTA |
| 6 ou mais | OPERAÇÃO CRÍTICA |

## Recomendações Automáticas

O sistema também gera recomendações automáticas.

Exemplo:

```python
if risco_total == 0:
```
A missão continua normalmente.
```python
elif risco_total <= 2:
```
O sistema sugere verificações preventivas.
```python
elif risco_total <= 5:
```
O programa recomenda reforçar o monitoramento.
```python
else:
```
O sistema ativa protocolos de emergência.

## Relatório Final

Após analisar todos os ciclos, o programa gera um relatório completo.

### Médias operacionais

O sistema calcula médias de:

- Temperatura
- Comunicação
- Bateria
- Oxigênio
- Estabilidade estrutural

Exemplo:

```python
media_temp = soma_temp / quantidade_ciclos
```
### Ciclo mais crítico

O programa identifica qual ciclo apresentou maior risco.

```python
maior_risco = max(riscos_ciclos)
```

### Quantidade de ciclos críticos

O sistema conta quantos ciclos tiveram risco elevado.

```python
if risco >= 6:
```

### Tendência operacional

O sistema verifica se a missão piorou ou melhorou ao longo do tempo.

Exemplo:

```python
if riscos_ciclos[-1] > riscos_ciclos[0]:
```

### Sistema mais afetado

O programa acumula pontuações de risco de cada sistema e identifica qual apresentou mais falhas.

```python
maior_pontuacao_area = max(risco_areas)
```

## Estruturas de Programação Utilizadas

O projeto utiliza diversos conceitos fundamentais da programação.

### Listas

Utilizadas para armazenar dados da missão.

### Estruturas condicionais

Utilizadas para classificação dos sistemas.

- if
- elif
- else

 ### Estruturas de repetição

Utilizadas para percorrer ciclos operacionais.

for

## Exemplo de Saída
 
```text
============================================================
CENTRAL DE MONITORAMENTO ESPACIAL
============================================================

Missão: Nebula Explorer IX
Equipe responsável: Equipe Horizon

============================================================
CICLO OPERACIONAL 1
------------------------------------------------------------

Temperatura: 22 °C | NORMAL | Temperatura controlada
Comunicação: 95% | NORMAL | Comunicação estável
Bateria: 90% | NORMAL | Energia operando normalmente
Oxigênio: 98% | NORMAL | Suporte vital estável
Estabilidade: 93% | NORMAL | Estrutura operacional estável

Pontuação de risco do ciclo: 0
Classificação do ciclo: OPERAÇÃO ESTÁVEL
```

## Objetivos Educacionais

Este projeto foi desenvolvido com foco em prática de:

- lógica de programação
- análise de dados
- monitoramento de sistemas
- estruturas condicionais
- estruturas de repetição
- cálculos estatísticos
- organização de código
- geração de relatórios

## Possíveis Melhorias Futuras
