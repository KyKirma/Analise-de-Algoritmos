import itertools


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

@tempo_gastado
def worst_fit(items, bin_capacity):
    # Lista para armazenar os bins
    bins = []

    for item in items:
        # Encontra o bin com o maior espaço livre que pode acomodar o item
        worst_bin_index = -1
        max_space_left = -1

        for i, bin in enumerate(bins):
            space_left = bin_capacity - sum(bin)
            if item <= space_left and space_left > max_space_left:
                worst_bin_index = i
                max_space_left = space_left

        # Se nenhum bin existente pode acomodar o item, cria um novo bin
        if worst_bin_index == -1:
            bins.append([item])
        else:
            bins[worst_bin_index].append(item)

    return bins

@tempo_gastado
def brute_force_bin_packing(items, bin_capacity):
    n = len(items)
    best_solution = None
    min_bins = float('inf')

    # Gerar todas as possíveis alocações dos itens
    for partition in itertools.product(range(n), repeat=n):
        bins = [[] for _ in range(n)]
        valid = True

        # Alocar os itens nos bins conforme a partição
        for item_index, bin_index in enumerate(partition):
            bins[bin_index].append(items[item_index])

        # Verificar se todos os bins estão dentro da capacidade
        for bin in bins:
            if sum(bin) > bin_capacity:
                valid = False
                break

        # Atualizar a melhor solução se válida e usar menos bins
        if valid:
            used_bins = [bin for bin in bins if bin]
            if len(used_bins) < min_bins:
                min_bins = len(used_bins)
                best_solution = used_bins

    return best_solution

# Exemplo de uso
if __name__ == "__main__":

    items = [5, 6, 2, 7, 1, 3, 8, 4]  # Lista de itens com diferentes tamanhos
    bin_capacity = 10  # Capacidade de cada bin

    print("Resultado com Worst Fit:")
    result_wf = worst_fit(items, bin_capacity)
    for i, bin in enumerate(result_wf):
        print(f"Bin {i + 1}: {bin} (Espaço usado: {sum(bin)}/{bin_capacity})")

    print("\nResultado com Força Bruta:")
    result_bf = brute_force_bin_packing(items, bin_capacity)
    for i, bin in enumerate(result_bf):
        print(f"Bin {i + 1}: {bin} (Espaço usado: {sum(bin)}/{bin_capacity})")

    print("\n")

    for key, value in gasto.items():
        total_time = sum(value['tempo'])
        print(f"Tempo gasto com {key}: {total_time:.6f} segundos")
