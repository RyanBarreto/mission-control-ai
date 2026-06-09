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
