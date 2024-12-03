'''
Trabalho 1 - Multiplicação de Matrizes Análise de Algorítmos - 16/10
Nome: Pedro Kourly
Turma: 6ºP Ciência da Computação
Professor: André Chaves

Implementar todos os algoritmos de ordenação visto em sala de aula.

Realizar analise empírica para cada algoritmo:
 - Gerar a entrada aleatório e aplicar a mesma  em algoritmo de ordenação;

 - pegar o tempo antes e de depois da execução do algoritmo;

 - calcular o tempo de execução;

 - gerar o gráfico de tempo de execução entre todos os algoritmos;

- apresentar os custos de cada algoritmo
---------------------------------------------------

O código irá gerar um PNG com o gráfico contendo as informações de performances
'''
#Variáveis
range_Numeros = 10

# Decorator de cálculo de tempo gasto
gasto = {}
def tempo_gastado(func):
    import time
    
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # Começa a contagem do tempo
        result = func(*args, **kwargs)  # Chama a função decorada
        fim = time.perf_counter()  # Para a contagem do tempo

        # Armazena o tempo gasto junto com o nome da função
        if func.__name__ not in gasto:
            gasto[func.__name__] = []  # Cria uma nova lista se a chave não existir
        gasto[func.__name__].append(fim - inicio)  # Adiciona o tempo à lista
        
        return result  # Retorna o resultado da função
    return wrapper



@tempo_gastado
def matriz_multiplicacao(A, B):
    # Verifica se as dimensões são compatíveis
    if A.shape[1] != B.shape[0]:
        raise ValueError("O número de colunas de A deve ser igual ao número de linhas de B.")

    # Inicializa a matriz resultante com zeros
    m, n = A.shape
    nB, p = B.shape
    C = np.zeros((m, p))

    # Realiza a multiplicação
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]

    return C



def pad_matrix(matriz):
    #Preenche a matriz com zeros para torná-la uma matriz quadrada de dimensão potência de 2.
    n = matriz.shape[0]
    m = matriz.shape[1]
    new_size = 1 << (max(n, m) - 1).bit_length()  # Encontrar a próxima potência de 2
    padded_matriz = np.zeros((new_size, new_size), dtype=matriz.dtype)
    padded_matriz[:n, :m] = matriz
    return padded_matriz

def strassen(A, B):
    # Caso base: se a matriz é 1x1, retorne o produto
    if A.shape[0] == 1:
        return A * B

    # Dividir as matrizes em submatrizes
    n = A.shape[0]
    mid = n // 2

    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]

    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]

    # Calcular as 7 multiplicações
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Combinar os resultados
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Juntar as submatrizes em uma matriz resultante
    C = np.zeros((n, n), dtype=A.dtype)
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

@tempo_gastado
def strassen_multiplicacao(A, B):
    # Realizar a multiplicação de Strassen
    C= strassen(A, B)

    # Retornar a parte relevante da matriz resultante
    return C


def gerarGrafico():
    # Gerar gráfico de custo
    fig, ax = plt.subplots()
    # Plota os dados para o algoritmo 1
    ax.plot([2, 4, 8, 16, 32, 64, 128, 256], gasto['matriz_multiplicacao'], marker='o', label='Método Tradicional', color='blue')

    # Plota os dados para o algoritmo 2
    ax.plot([2, 4, 8, 16, 32, 64, 128, 256], gasto['strassen_multiplicacao'], marker='o', label='Algorítmo de Strassen', color='orange')

    # Adicionando título e rótulos
    ax.set_title('Comparação de Eficiência entre Algoritmos')
    ax.set_xlabel('Tamanho da Matriz')
    ax.set_ylabel('Tempo Gasto (segundos)')

    ax.legend()
    ax.grid(True)
    fig.savefig(os.path.join(os.path.dirname(__file__), f"teste.png"))


if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_interactions import zoom_factory, panhandler
    from tqdm import tqdm
    import os

    for ordem in tqdm([2, 4, 8, 16, 32, 64, 128, 256], desc="Iterando sobre ordens"):
        # Criar ou abrir um arquivo para registrar os dados
        with open(f"{os.path.join(os.path.dirname(__file__))}/registro_multiplicacao_v2.txt", "a") as file:
            # Escrever a ordem
            file.write(f"Ordem: {ordem}\n")
            
            # Gerar as matrizes A e B
            matriz_A = np.random.randint(0, range_Numeros, (ordem, ordem))
            matriz_B = np.random.randint(0, range_Numeros, (ordem, ordem))
            
            # Escrever as matrizes A e B
            file.write(f"Matriz A:\n{matriz_A}\n")
            file.write(f"Matriz B:\n{matriz_B}\n")
            
            # Calcular os resultados
            resultado_tradicional = matriz_multiplicacao(matriz_A, matriz_B).astype(int)
            resultado_strassen = strassen_multiplicacao(matriz_A, matriz_B).astype(int)
            
            # Escrever os resultados
            file.write(f"Resultado (Método Tradicional):\n{resultado_tradicional}\n")
            file.write(f"Resultado (Algoritmo de Strassen):\n{resultado_strassen}\n")
            
            # Adicionar uma linha em branco para melhor legibilidade
            file.write("\n" + "="*40 + "\n\n")

    print(gasto)
    gerarGrafico()