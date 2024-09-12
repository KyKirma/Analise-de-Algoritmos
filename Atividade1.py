'''
Atividade 1 Análise de Algorítmos - 17/09
Nome: Pedro Kourly
Turma: 6ºP Ciência da Computação
Professor: André Chaves

Criar dois programa para multiplicação de matrizes, o programa tradicional (utilizando duas estrutura de repetições) e o programa otimizado (utilizando apenas uma estrutura de repetição),  e executa-los para a mesma entrada n (n é a dimensões das matrizes. exemplo  matriz3x3 a dimensão é n= 3). 

Você deve pegar o tempo de execução de ambos os algoritmos para cada entrada n, fazer até n = 10 (ou seja matriz 10x10), e gerar uma tabela e um gráfico comparando as execução em relação de tempo x entrada.
'''

import numpy as np

def rand_matrix(n, min_val = 0, max_val = 20):
    #Essa função retorna uma matriz vazia de ordem 'n', com limites definidos como padrão 0 e 20.
    
    matrix = np.random.randint(min_val, max_val, size=(n, n))
    return matrix

# Inicializa as variáveis do algorítmo
n = 10

# Problema o(n²)
def multiplicacao_tradicional():
    pass