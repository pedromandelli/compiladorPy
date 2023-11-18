from lexer import Lexer
from syntax import SyntaxAnalyzer
from syntax_table import ANALISADOR_SINTATICO_TABELA


def main():
    # Caminho para o diretório onde os arquivos TXT estão armazenados
    diretorio = 'examples/'

    # Nome do arquivo que você quer ler (exemplo: 'arquivo.txt')
    nome_do_arquivo = 'entrada.txt'
    # Caminho completo para o arquivo
    caminho_completo = diretorio + nome_do_arquivo

    # Abrir o arquivo para leitura
    with open(caminho_completo, 'r') as arquivo:
        conteudo = arquivo.read()

    content = conteudo
    lexer = Lexer(content)

    # Cria o analisador sintático e inicia a análise
    analyzer = SyntaxAnalyzer(lexer, ANALISADOR_SINTATICO_TABELA)
    result = analyzer.analyze()
    print("Análise Sintática Bem-Sucedida!" if result else "Análise Sintática Falhou")


if __name__ == "__main__":
    main()
