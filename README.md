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
