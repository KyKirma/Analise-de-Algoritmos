import os

# Decorator de cálculo de tempo gasto
gasto = {}

def tempo_gastado(func):
    import time
    
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # Começa a contagem do tempo
        result = func(*args, **kwargs)  # Chama a função decorada
        fim = time.perf_counter()  # Para a contagem do tempo

        if func.__name__ not in gasto:
            gasto[func.__name__] = {'tempo': []} 

        gasto[func.__name__]['tempo'].append(fim - inicio)
        return result 
    return wrapper


import random

def gerar_tempos(n):
    a = [[random.randint(1, 10) for _ in range(n)],  # Linha 1
         [random.randint(1, 10) for _ in range(n)]]  # Linha 2
    t = [[random.randint(1, 10) for _ in range(n - 1)],  # Transferência da linha 1 para 2
         [random.randint(1, 10) for _ in range(n - 1)]]  # Transferência da linha 2 para 1
    return a, t

@tempo_gastado
def linha_de_montagem(n, a, t, e, x):
    """
    n  -> Número de estações por linha
    a  -> Tempo nas estações (matriz 2xN)
    t  -> Tempo de transferência entre linhas (matriz 2x(N-1))
    e  -> Tempo de entrada nas linhas (lista de tamanho 2)
    x  -> Tempo de saída das linhas (lista de tamanho 2)
    """

    f1 = [0] * n
    f2 = [0] * n

    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]

    for j in range(1, n):
        f1[j] = min(f1[j-1] + a[0][j], f2[j-1] + t[1][j-1] + a[0][j])
        f2[j] = min(f2[j-1] + a[1][j], f1[j-1] + t[0][j-1] + a[1][j])

    return min(f1[n-1] + x[0], f2[n-1] + x[1])

@tempo_gastado
def linha_de_montagem_forca_bruta(n, a, t, e, x):
    
    tempo_minimo = float('inf')  # Inicializar o tempo mínimo como infinito
    total_combinacoes = 2 ** n   # Número total de combinações (2^n)

    # Gerar todas as combinações usando números binários de 0 a 2^n - 1
    for combinacao in range(total_combinacoes):
        caminho = []  # Caminho atual (lista de linhas)
        num = combinacao

        # Gerar o caminho binário correspondente ao número
        for _ in range(n):
            caminho.append(num % 2)  # Adiciona 0 (linha L1) ou 1 (linha L2)
            num //= 2
        caminho.reverse()  # Reverter para ter a ordem correta das estações

        tempo_total = 0
        linha_atual = caminho[0]

        # Adicionar o tempo de entrada
        tempo_total += e[linha_atual] + a[linha_atual][0]

        # Percorrer as estações
        for j in range(1, n):
            proxima_linha = caminho[j]
            tempo_total += a[proxima_linha][j]
            if linha_atual != proxima_linha:
                tempo_total += t[linha_atual][j-1]
            linha_atual = proxima_linha

        # Adicionar o tempo de saída
        tempo_total += x[linha_atual]

        # Atualizar o tempo mínimo se necessário
        tempo_minimo = min(tempo_minimo, tempo_total)

    return tempo_minimo

def gerarGrafico(ordem):
    # Gerar gráfico de custo
    fig, ax = plt.subplots()
    # Plota os dados para o algoritmo 1
    ax.plot(range(1, ordem + 1), gasto['linha_de_montagem']['tempo'], marker='o', label='Algorítmo Por Programação Dinamica', color='blue')

    # Plota os dados para o algoritmo 2
    ax.plot(range(1, ordem + 1), gasto['linha_de_montagem_forca_bruta']['tempo'], marker='o', label='Algoritmo de Força Bruta', color='orange')

    # Adicionando título e rótulos
    ax.set_title('Comparação de Eficiência entre Algoritmos')
    ax.set_xlabel('Tamanho de n')
    ax.set_ylabel('Tempo Gasto (segundos)')

    ax.legend()
    ax.grid(True)
    fig.savefig(os.path.join(os.path.dirname(__file__), f"grafico_custo_algoritmos_{ordem}_test.png"))

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    import os

    N_max = 20  # Valor máximo de N para testar
    e = [10, 15]  # Tempos de entrada nas linhas
    x = [15, 10]   # Tempos de saída das linhas

    print("Resultados para diferentes valores de N:")
    for n in range(1, N_max + 1):
        a, t = gerar_tempos(n)  # Gerar tempos aleatórios para cada valor de N
        tempo_pd = linha_de_montagem(n, a, t, e, x)
        tempo_fb = linha_de_montagem_forca_bruta(n, a, t, e, x)
        print(f"Com {n} estações: PD = {tempo_pd}, Força Bruta = {tempo_fb}")

    # Gerar gráfico de custo
    gerarGrafico(N_max)