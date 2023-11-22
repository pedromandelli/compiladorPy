import sys
from lexer import Lexer
from syntax import SyntaxAnalyzer
from syntax_table import ANALISADOR_SINTATICO_TABELA

def main():
    # Caminho para o diretório onde os arquivos TXT estão armazenados
    diretorio = 'examples/'

    # Captura o nome do arquivo da linha de comando ou usa um padrão
    nome_do_arquivo = sys.argv[1] if len(sys.argv) > 1 else 'entrada.lcc'

    # Caminho completo para o arquivo
    caminho_completo = diretorio + nome_do_arquivo

    try:
        # Tenta abrir o arquivo para leitura
        with open(caminho_completo, 'r') as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_completo}' não foi encontrado.")
        return  # Encerra a execução da função main

    content = conteudo
    lexer = Lexer(content)

    # Cria o analisador sintático e inicia a análise
    analyzer = SyntaxAnalyzer(lexer, ANALISADOR_SINTATICO_TABELA)
    result = analyzer.analyze()
    print(f"Análise Sintática do arquivo '{nome_do_arquivo}' Bem-Sucedida!" if result else f"Análise Sintática do arquivo '{nome_do_arquivo}' Falhou")

if __name__ == "__main__":
    main()