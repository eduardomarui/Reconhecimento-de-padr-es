# Dicionário para armazenar os resultados dos casos
resultados = {}
# Contador para o número do caso atual
caso = 1
# Abrindo arquivo para leitura
f = open("texto.txt", "r")

# Função para encontrar o centro da matriz
def centro():
    global caso
    matriz = f.readline()
    # Condição de parada: imprime os resultados e encerra o programa
    if matriz.strip() == "0 0":
        for idx, i in enumerate(resultados):
            print(f"caso {idx+1}:", resultados[i]) 
        exit()

    linhas, colunas = map(int, matriz.split())

    # Populando a matriz com dados do arquivo
    A = [list(map(float, f.readline().split())) for _ in range(linhas)]

    # Calcula a linha central
    somabaixo, mindiflinha = 0, None

    # Calcula a coluna central
    somadir, mindifcoluna = 0, None

    # Armazenando o resultado
    resultados[caso] = f"Centro ( {minlin}, {mincol} )"
    caso += 1
    
    # Processa a próxima matriz no arquivo
    centro()

# Inicia o processo
centro()
