import os

# Abrindo arquivos em modo escrita
arquivo = open('arquivo.txt', 'w', encoding='utf-8')
# Exibindo os atributos do arquivo
print(arquivo.name)  # Nome do arquivo
print(arquivo.mode)  # Modo de abertura
print('O arquivo está fechado?', arquivo.closed)  # Verifica se o arquivo está fechado

# Escrevendo no arquivo
arquivo.write('Olá, mundo!\n')

# Fechando o arquivo
arquivo.close()

# Verificando se o arquivo está fechado
print('O arquivo está fechado agora?', arquivo.closed)  # Verifica se o arquivo está fechado

# Exibindo os caminhos relativos e absolutos
relpath = os.path.relpath('arquivo.txt')
abspath = os.path.abspath('arquivo.txt')

print(f'Caminho relativo: {relpath}')
print(f'Caminho absoluto: {abspath}')
