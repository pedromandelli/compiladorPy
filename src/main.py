import sys
from lexer import Lexer
from syntax import SyntaxAnalyzer
from syntax_table import SYNTAX_TABLE

def main():
    # Caminho para o diretório onde as entradas estão
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

    # Analisador léxico recebe a entrada
    lexer = Lexer(conteudo)

    """O analisador sintático utiliza a tabela de reconhecimento sintático que foi construida com uma planilha e transformada em um dicionário"""
    # Cria o analisador sintático e inicia a análise
    analyzer = SyntaxAnalyzer(lexer, SYNTAX_TABLE)
    result = analyzer.analyze()
    if result:
        print(f"O arquivo '{nome_do_arquivo}' Passou na análise sintática ")
    else:
        print(f"O arquivo '{nome_do_arquivo}' Falhou na análise sintática")

if __name__ == "__main__":
    main()