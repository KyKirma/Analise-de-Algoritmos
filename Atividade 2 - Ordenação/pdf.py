from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # Adiciona um cabeçalho
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório Atividade 2', 0, 1, 'C')

    def footer(self):
        # Adiciona um rodapé
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# Cria uma instância do PDF
pdf = PDF()
pdf.add_page()

# Define a font
pdf.set_font('Arial', '', 12)

def gerarRelatorio(n):
    # Informações a serem adicionadas
    nome = "Pedro Henrique Assis Kourly"
    professor = "André Cháves"
    disciplina = "Análise de Algorítmos"
    data = "16/10/24"  # Formata a data como DD/MM/AAAA

    # Adiciona as informações ao PDF
    pdf.cell(0, 10, f'Nome: {nome}', 0, 1)
    pdf.cell(0, 10, f'Professor: {professor}', 0, 1)
    pdf.cell(0, 10, f'Disciplina: {disciplina} | Ciência da Computação', 0, 1)
    pdf.cell(0, 10, f'Data: {data}', 0, 1)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Adiciona uma linha preta

    # Adiciona texto
    texto = "Este é um relatório gerado automaticamente a cada vez que o programa é rodado. As informações são geradas de acordo com as variáveis escolhida no programa."
    pdf.multi_cell(0, 10, texto)

    # Informações sobre os algoritmos de ordenação
    algoritmos = [
        {
            "nome": "Bubble Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n²) ({n}² = {n**2} operações)",
                "Caso Médio": f"O(n²) ({n}² = {n**2} operações)",
                "Melhor Caso": f"O(n) ({n} operações, se já estiver ordenado)"
            },
            "complexidade_espacial": "O(1) (in-place)"
        },
        {
            "nome": "Selection Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n²) ({n}² = {n**2} operações)",
                "Caso Médio": f"O(n²) ({n}² = {n**2} operações)",
                "Melhor Caso": f"O(n²) ({n}² = {n**2} operações)"
            },
            "complexidade_espacial": "O(1) (in-place)"
        },
        {
            "nome": "Insertion Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n²) ({n}² = {n**2} operações)",
                "Caso Médio": f"O(n²) ({n}² = {n**2} operações)",
                "Melhor Caso": f"O(n) ({n} operações, se já estiver ordenado)"
            },
            "complexidade_espacial": "O(1) (in-place)"
        },
        {
            "nome": "Merge Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n log n) ({n} log({n}) ~ {int(n * (n ** 0.5))} operações)",
                "Caso Médio": f"O(n log n) ({n} log({n}) ~ {int(n * (n ** 0.5))} operações)",
                "Melhor Caso": f"O(n log n) ({n} log({n}) ~ {int(n * (n ** 0.5))} operações)"
            },
            "complexidade_espacial": "O(n) (não é in-place)"
        },
        {
            "nome": "Quick Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n²) ({n}² = {n**2} operações, se o pivô for mal escolhido)",
                "Caso Médio": f"O(n log n) ({n} log({n}) ~ {int(n * ( n ** 0.5))} operações)",
                "Melhor Caso": f"O(n log n) ({n} log({n}) ~ {int(n * (n ** 0.5))} operações)"
            },
            "complexidade_espacial": "O(log n) (in-place)"
        },
        {
            "nome": "Counting Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n + k) (onde k é o intervalo dos números, se k for pequeno, por exemplo, 100)",
                "Caso Médio": f"O(n + k) ({n} + 100 = {n + 100} operações)",
                "Melhor Caso": f"O(n + k) ({n} + 100 = {n + 100} operações)"
            },
            "complexidade_espacial": "O(k) (dependente do intervalo)"
        },
        {
            "nome": "Bucket Sort",
            "complexidade_tempo": {
                "Pior Caso": f"O(n²) (se todos os elementos caírem em um único balde)",
                "Caso Médio": f"O(n + k) ({n} + k, onde k é o número de baldes)",
                "Melhor Caso": f"O(n + k) ({n} + k, se os elementos estiverem uniformemente distribuídos)"
            },
            "complexidade_espacial": "O(n + k) (dependente do número de baldes)"
        }
    ]

    # Adiciona as informações sobre os algoritmos de ordenação
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Algoritmos de Ordenação', 0, 1)
    pdf.ln(5)
    for algoritmo in algoritmos:
        pdf.set_font('Arial', '', 12)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, f'Nome: {algoritmo["nome"]}', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f'Complexidade de Tempo:', 0, 1)
        for caso, complexidade in algoritmo["complexidade_tempo"].items():
            pdf.cell(0, 10, f'  {caso}: {complexidade.replace("≈", "~")}', 0, 1)
        pdf.cell(0, 10, f'Complexidade Espacial: {algoritmo["complexidade_espacial"]}', 0, 1)
        pdf.ln(5)

    # Salva o PDF
    pdf.output(os.path.join(os.path.dirname(__file__), "relatorio.pdf"), 'F')