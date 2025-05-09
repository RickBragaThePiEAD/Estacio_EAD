#Definir a função principal
def main():
    print("Digite suas frases. Digite 'sair' para terminar e salvar o arquivo.")
    frases = []
    while True:
        entrada = input("> ")
        if entrada.lower() == 'sair':
            break
        frases.append(entrada)
    
    # Abre o arquivo em modo de escrita
    with open('frases.txt', 'w') as arquivo:
        # Escreve cada frase no arquivo
        for frase in frases:
            arquivo.write(frase + '\n')

    print("Arquivo original criado. Agora vamos manipular os dados.")
    dados_modificados = []
    # Abre o arquivo em modo de leitura
    with open('meu_arquivo.txt', 'r') as arquivo:
        # Lê cada linha do arquivo
        for linha in arquivo:
            # Remove espaços em branco e converte para maiúsculas
            dados_modificados.append(linha.strip().upper())
    
    # Abre o arquivo em modo de escrita
    with open('meu_arquivo.txt', 'w') as arquivo:
        # Escreve cada linha modificada no arquivo
        for linha in dados_modificados:
            arquivo.write(linha + '\n')
    print("O arquivo foi sobrescrito com os dados modificados.")

# Chama a função principal
if __name__ == "__main__":
    main()
# Este código cria um arquivo de texto com frases digitadas pelo usuário e depois lê esse arquivo,
# modifica os dados (remove espaços em branco e converte para maiúsculas) e sobrescreve o arquivo original.
# O arquivo 'frases.txt' é criado com as frases do usuário, e o arquivo 'meu_arquivo.txt' é sobrescrito com os dados modificados.
# O código é um exemplo simples de manipulação de arquivos em Python, utilizando funções básicas de leitura e escrita.
# O código é útil para entender como trabalhar com arquivos de texto em Python, incluindo a criação, leitura e escrita de dados.
# O código pode ser expandido para incluir mais funcionalidades, como tratamento de erros, validação de entrada e manipulação de diferentes formatos de arquivo.
# O código é um exemplo básico, mas pode ser adaptado para atender a necessidades mais complexas de manipulação de dados.
# O código pode ser utilizado em diversos contextos, como processamento de dados, geração de relatórios e automação de tarefas.
# O código é um exemplo prático de como utilizar Python para manipulação de arquivos e pode ser utilizado como base para projetos mais complexos.
# O código é um exemplo simples, mas pode ser expandido para incluir mais funcionalidades, como tratamento de erros, validação de entrada e manipulação de diferentes formatos de arquivo.
