

class SyntaxAnalyzer:
    def __init__(self, lexer, syntax_table):
        self.lexer = lexer
        self.syntax_table = syntax_table
        self.stack = ['$']  # Inicia a pilha com o símbolo '$'
        self.stack.append('PROGRAM')  # Símbolo inicial da gramática

    def analyze(self):
        token = self.lexer.get_next_token()
        print('Lista de tokens')
        # Imprime a tabela de símbolos
        while True:
            # Verifica o estado da pilha
            # print(f"Pilha: {self.stack}")

            top = self.stack.pop()  # Desempilha o elemento do topo
            current_token = token

            # Imprime o símbolo do topo e o token atual
            # print(f"Topo da pilha: {top}, Token atual: {current_token.type}")

            if top in self.syntax_table:
                if current_token.type in self.syntax_table[top]:
                    production = self.syntax_table[top][current_token.type]
                    # print(f"Produção: {production}")  # Imprime a produção encontrada
                    if production != "":
                        for symbol in reversed(production.split()):
                            self.stack.append(symbol)
                else:
                    # Erro sintático
                    error_message(current_token.type, ' '.join(self.stack[::-1]), top, current_token.type)
                    return False
            elif top == current_token.type:
                print(f'Tipo: {current_token.type}, Valor: {current_token.value}, Linha: {self.lexer.current_line}')
                token = self.lexer.get_next_token()
            elif top == "$" and token.type == "EOF":
                print('\n')
                print("Tabela de Símbolos:")
                print(self.lexer.symbol_table)
                return True
            else:
                error_message(current_token.type, ' '.join(self.stack[::-1]), top, current_token.type)
                return False


def error_message(token_type, sentencial, top, input):
    print('\n')
    print(f"Erro de análise sintática: Token inesperado '{token_type}'")
    print(f"Forma sentencial: {sentencial}")
    print(f"Símbolo não-terminal mais à esquerda: {top}")
    print(f"Token da entrada: {input}")