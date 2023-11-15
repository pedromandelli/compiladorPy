

class SyntaxAnalyzer:
    def __init__(self, lexer, syntax_table):
        self.lexer = lexer
        self.syntax_table = syntax_table
        self.stack = ['$']  # Inicia a pilha com o símbolo '$'
        self.stack.append('PROGRAM')  # Símbolo inicial da gramática

    def analyze(self):
        token = self.lexer.get_next_token()
        while True:
            # Verifica o estado da pilha
            print(f"Pilha: {self.stack}")

            top = self.stack.pop()  # Desempilha o elemento do topo
            current_token = token

            # Imprime o símbolo do topo e o token atual
            print(f"Topo da pilha: {top}, Token atual: {current_token.type}")

            if top == "$" and token.type == "EOF":
                return True

            if top in self.syntax_table:
                if current_token.type in self.syntax_table[top]:
                    production = self.syntax_table[top][current_token.type]
                    print(f"Produção: {production}")  # Imprime a produção encontrada
                    if production != "":
                        for symbol in reversed(production.split()):
                            self.stack.append(symbol)
                else:
                    raise Exception(f"Erro de análise sintática: Token inesperado {current_token.type}")
            elif top == current_token.type:
                token = self.lexer.get_next_token()  # Solicita o próximo token
            else:
                raise Exception(f"Erro de análise sintática: Símbolo inesperado {top}")

            # Verifica se a análise foi concluída com sucesso
            if self.stack[-1] == "$" and current_token.type == 'EOF':
                return True
