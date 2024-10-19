# Simulador de Modelo SIR

Este script Python implementa um modelo Suscetível-Infeccioso-Recuperado (SIR) para simular a propagação de uma doença infecciosa em uma população ao longo do tempo.

## Visão Geral

O modelo SIR é um modelo epidemiológico fundamental que divide uma população em três compartimentos:

- Suscetível (S): Indivíduos que podem ser infectados
- Infeccioso (I): Indivíduos que estão infectados e podem espalhar a doença
- Recuperado/Removido (R): Indivíduos que se recuperaram da infecção ou foram removidos da população

O modelo simula a progressão desses compartimentos ao longo do tempo com base em parâmetros especificados.

## Características

- Tamanhos iniciais de população personalizáveis para cada compartimento
- Taxa de infecção (β) e taxa de recuperação (γ) ajustáveis
- Simulação para um número especificado de dias
- Gera um DataFrame pandas com resultados diários
- Plota os resultados usando matplotlib
- Salva automaticamente o gráfico como um arquivo PNG com timestamp

## Requisitos

- Python 3.x
- pandas
- matplotlib

## Uso

1. Importe a classe `SIR` do script:

```python
from modelo import SIR
```

2. Crie uma instância do modelo SIR com os parâmetros desejados:

```python
modelo = SIR(dias=1000, Suscetiveis=1571, Infectados=99, Retirados=0, beta=0.05, gamma=0.01)
```


Parâmetros:
- `dias`: Número de dias para simular (padrão: 1000)
- `Suscetiveis`: População inicial suscetível (padrão: 950)
- `Infectados`: População inicial infectada (padrão: 50)
- `Retirados`: População inicial recuperada/removida (padrão: 0)
- `beta`: Taxa de infecção (padrão: 0.05)
- `gamma`: Taxa de recuperação (padrão: 0.01)

3. Execute a simulação:

```python
modelo.executar()
```

4. Plote os resultados:

```python
modelo.plotar_resultados()
```

Isso exibirá o gráfico e o salvará como um arquivo PNG com timestamp no diretório atual.

## Saída

- O método `executar()` preenche um DataFrame pandas (`modelo.resultados`) com contagens diárias para cada compartimento.
- O método `plotar()` gera um gráfico de linhas mostrando a progressão de cada compartimento ao longo do tempo.
- Um arquivo PNG do gráfico é salvo no diretório atual com o formato de nome `grafico_<timestamp>.png`.

## Personalização

Você pode ajustar os parâmetros do modelo ao criar a instância SIR para simular diferentes cenários. Por exemplo:

```python
#Alta taxa de infecção, baixa taxa de recuperação
modelo = SIR(dias=1000, Suscetiveis=1571, Infectados=99, Retirados=0, beta=0.05, gamma=0.01)
```

```python
#Baixa taxa de infecção, alta taxa de recuperação
modelo = SIR(dias=1000, Suscetiveis=1571, Infectados=99, Retirados=0, beta=0.01, gamma=0.05)
```

