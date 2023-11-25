

class SyntaxAnalyzer:
    def __init__(self, lexer, syntax_table):
        self.lexer = lexer
        self.syntax_table = syntax_table
        self.stack = ['$']  # Inicia a pilha com o símbolo '$'
        self.stack.append('PROGRAM')  # Símbolo inicial da gramática

    def analyze(self):
        token = self.lexer.get_next_token()
        token_list = []
        sentence_form = ""
        while True:
            # Verifica o estado da pilha
            # print(f"Pilha: {self.stack}")

            # Desempilha o elemento do topo
            top = self.stack.pop()
            current_token = token

            if current_token:
                # Imprime o símbolo do topo e o token atual
                #print(f"Topo da pilha: {top}, Token atual: {current_token.type}")
                if top in self.syntax_table:
                    if current_token.type in self.syntax_table[top]:
                        production = self.syntax_table[top][current_token.type]
                        # Imprime a produção encontrada
                        # print(f"Produção: {production}")
                        if production != "":
                            for symbol in reversed(production.split()):
                                self.stack.append(symbol)
                    else:
                        # Erro sintático
                        error_message(token_list, self.lexer.symbol_table, sentence_form, top, current_token.type)
                        return False
                elif top == current_token.type:
                    # Imprime o token reconhecido
                    sentence_form = sentence_form + f' {current_token.value}'
                    token = self.lexer.get_next_token()
                    token_list.append(
                        f'Tipo: {current_token.type}, Valor: {current_token.value}, Linha: {self.lexer.current_line}')
                elif top == "$" and token.type == "EOF":
                    #
                    print('Lista de tokens')
                    for t in token_list:
                        print(t)
                    print('\n')
                    print("Tabela de Símbolos (Linha, Coluna):")
                    print(self.lexer.symbol_table)
                    return True
                else:
                    # Erro sintático
                    error_message(token_list, self.lexer.symbol_table, sentence_form, top, current_token.type)
                    return False
            else:
                raise Exception(f'Erro léxico no caracter: "{self.lexer.current_char}", Linha {self.lexer.current_line}, Coluna: {self.lexer.current_column}')

def error_message(tokens_list, symbol_table, sentence, top, input):
    print('\n')
    print('Lista de tokens')
    for t in tokens_list:
        print(t)

    print('\n')
    print('Tabela de Símbolos Parcial (Linha, Coluna):')
    print(symbol_table)

    print('\n')
    print('Forma sentencial:')
    print(sentence)

    print('\n')
    print(f"Símbolo não-terminal mais à esquerda: {top}")
    print(f"Token da entrada: {input}")