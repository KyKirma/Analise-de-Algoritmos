'''
Atividade 2 Análise de Algorítmos - 16/10
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
# Decorator de cálculo de tempo gasto
gasto = {}

def tempo_gastado(func):
    import time
    
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()  # Começa a contagem do tempo
        result = func(*args, **kwargs)  # Chama a função decorada
        fim = time.perf_counter()  # Para a contagem do tempo
        # Armazena o tempo gasto junto com o nome da função
        gasto[func.__name__] = fim - inicio
        return result  # Retorna o resultado da função
    return wrapper

@tempo_gastado
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@tempo_gastado
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

@tempo_gastado
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

@tempo_gastado
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

@tempo_gastado
def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(arr) - 1)
    return arr

@tempo_gastado
def counting_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Encontra o valor máximo no array
    max_val = max(arr)
    
    # Cria um array de contagem com tamanho max_val + 1
    count = [0] * (max_val + 1)

    # Conta a ocorrência de cada elemento no array
    for num in arr:
        count[num] += 1

    # Cria um array de saída para armazenar os elementos ordenados
    output = []
    
    # Preenche o array de saída com os elementos ordenados
    for i in range(len(count)):
        output.extend([i] * count[i])  # Adiciona o número i, count[i] vezes

    return output

@tempo_gastado
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Encontrar o valor máximo no array
    max_val = max(arr)
    # Definir o número de baldes
    bucket_count = 10  # Você pode ajustar o número de baldes conforme necessário
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir os elementos nos baldes
    for num in arr:
        index = num * bucket_count // (max_val + 1)  # Mapeia o número para um balde
        buckets[index].append(num)

    # Ordenar os baldes e concatená-los
    sorted_array = []
    for bucket in buckets:
        insertion_sort(bucket)  # Ordena o balde
        sorted_array.extend(bucket)  # Adiciona o balde ordenado ao array final

    return sorted_array


if __name__ == "__main__":
    import random
    from tqdm import tqdm
    import matplotlib.pyplot as plt
    import os

    n = 1000 # Valor base
    arr = [random.randint(0, 1000) for _ in range(n)]
    algorithms = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, counting_sort, bucket_sort]

    # Usar tqdm para mostrar o progresso na execução dos algoritmos
    for alg in tqdm(algorithms, desc="Algoritmos de Ordenação", unit="algorithm"):
        alg(arr.copy())

    for alg, tempo in gasto.items():
        print(f"{alg}: {tempo:.8f} s")
    
    # Gerar gráfico de custo
    plt.bar(gasto.keys(), gasto.values())
    plt.xlabel("Algoritmo")
    plt.ylabel("Tempo Gasto (s)")
    plt.title("Gráfico de Custo dos Algoritmos de Ordenação")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.text(6.5, max(gasto.values()), f"Comparação de Algoritmos de Ordenação\nBaseado em um array de {n} elementos", fontsize=10, ha='right', va='top')
    plt.savefig(os.path.join(os.path.dirname(__file__), "grafico_custo_algoritmos.png"))
    plt.show()

    from pdf import gerarRelatorio
    gerarRelatorio(n)