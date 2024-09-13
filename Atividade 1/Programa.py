'''
Atividade 1 Análise de Algorítmos - 17/09
Nome: Pedro Kourly
Turma: 6ºP Ciência da Computação
Professor: André Chaves

Criar dois programa para multiplicação de matrizes, o programa tradicional (utilizando duas estrutura de repetições) e o programa otimizado (utilizando apenas uma estrutura de repetição),  e executa-los para a mesma entrada n (n é a dimensões das matrizes. exemplo  matriz3x3 a dimensão é n= 3). 

Você deve pegar o tempo de execução de ambos os algoritmos para cada entrada n, fazer até n = 10 (ou seja matriz 10x10), e gerar uma tabela e um gráfico comparando as execução em relação de tempo x entrada.

---------------------------------------------------

O código irá salvar um relatório no arquivo "relatório.txt", contendo informações de tempo e passo a passo das iterações
'''

import numpy as np
import time
from tqdm import tqdm

def rand_matrix(n, min_val = 0, max_val = 20):
    # Essa função retorna uma matriz vazia de ordem 'n', com limites definidos como padrão 0 e 20.
    
    matrix = np.random.randint(min_val, max_val, size=(n, n))
    return matrix


# Problema o(n³)
def traditional_multiplication(n):
    # Essa função retorna o produto entre 2 matrizes aleatórias de mesma ordem n

    with open(f"relatório.txt", "a") as file:
        file.write("""Multiplicação tradicional [O(n³)]\n==================================""")

    for ordem in tqdm(range(n), desc = 'Matriz tradicional'):
        # Criação das matrizes
        matrizA = rand_matrix(ordem)
        matrizB = rand_matrix(ordem)


        # Matriz resultado
        matrizRes = np.zeros((ordem, ordem))

        # O produto
        startTime = time.time()
        for i in range(ordem):
            for j in range(ordem):
                for k in range(ordem):
                    matrizRes[i][j] += matrizA[i][k] * matrizB[k][j]
        finalTime = time.time()

        # Generate report for each iteration
        report_content = f"""
Report for Matrix Size {ordem}x{ordem}
=====================================

Matrix A:
{matrizA}

Matrix B:
{matrizB}

Multiplication Result:
{matrizRes}

Execution Time: {finalTime - startTime:.2f} seconds\n
"""

        with open(f"relatório.txt", "a") as file:
            file.write(report_content)


def main():
    report_content = """
Relatório de atividade\n

Atividade 1 Análise de Algorítmos
Nome: Pedro Kourly
Turma: 6ºP Ciência da Computação
Professor: André Chaves
===================================
          """
    
    with open(f"relatório.txt", "w") as file:
        file.write(report_content)

    # Inicializa as variáveis do algorítmo
    n = 11

    traditional_multiplication(n)


if __name__ == '__main__':
    main()