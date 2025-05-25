import os

# Caminho do diretório que deseja listar
diretorio = "C:\\Users\\PABLO\\Downloads"

# Lista todos os arquivos e pastas no diretório
arquivos = os.listdir(diretorio)

# Exibe apenas os arquivos (ignora pastas)
for arquivo in arquivos:
    if os.path.isfile(os.path.join(diretorio, arquivo)):
        print(arquivo)