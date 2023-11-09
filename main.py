from lexer import Lexer


def main():
    # Caminho para o diretório onde os arquivos TXT estão armazenados
    diretorio = 'examples/'

    # Nome do arquivo que você quer ler (exemplo: 'arquivo.txt')
    nome_do_arquivo = 'exemplo1.txt'

    # Caminho completo para o arquivo
    caminho_completo = diretorio + nome_do_arquivo

    # Abrir o arquivo para leitura
    with open(caminho_completo, 'r') as arquivo:
        conteudo = arquivo.read()

    content = conteudo
    lexer = Lexer(content)
    token = lexer.get_next_token()
    while token.type != 'EOF':  # Supondo que você tenha um token de fim de arquivo
        print(token)
        token = lexer.get_next_token()

    # Agora, depois de tokenizar o conteúdo, vamos imprimir a tabela de símbolos
    print("Tabela de Símbolos:")
    print(lexer.symbol_table)


if __name__ == "__main__":
    main()
