Para funcionamento do programa, instale uma venv. ou instale as bibliotecas do arquivo "requirements.txt". Isso pode ser feito através do seguinte código:
- pip install -r requirements.txt

só após isso o programa poderá ser executado corretamente.

O programa funciona da seguinte forma:

Temos o arquivo principal, o main.py, que tem implementado os algorítmos e suas análises.

O programa gera 3 outputs:
 - Terminal: o tempo exato de execução de cada algorítmo
 - PNG: um gráfico com a relação de tempo entre os algorítmos
 - PDF: um relatório com a análise de custo de cada algorítmo

Todos os 3 outputs são gerados automaticamente após a execução do programa, e a única variável que influencia e pode ser mudada é a "n", que representa o tamanho da array aleatória a ser passada para os algorítmos. O mesmo pode ser encontrado na linha 177 em "main.py".

o arquivo pdf.py é o auxiliar que gera o relatório, não é necessário mexer.