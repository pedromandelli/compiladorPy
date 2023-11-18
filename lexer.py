class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"


class Lexer:
    RESERVED_KEYWORDS = {
        'def': 'DEF',
        'void': 'VOID',
        'int': 'INT',
        'float': 'FLOAT',
        'str': 'STR',
        'return': 'RETURN',
        'if': 'IF',
        'else': 'ELSE',
        'while': 'WHILE',
        'for': 'FOR',
        'print': 'PRINT',
        'read': 'READ',
        'new': 'NEW',
        'break': 'BREAK',
        'null': 'NULL',
        'exec': 'EXEC'
    }

    def __init__(self, input):
        self.input = input
        self.position = 0
        self.current_char = self.input[self.position] if self.position < len(self.input) else None
        self.current_line = 1
        self.current_column = 0
        self.symbol_table = SymbolTable()


    def reset(self):
        self.position = 0
        self.current_char = self.input[self.position] if self.position < len(self.input) else None
        self.current_line = 1
        self.current_column = 1


    def advance(self):
        """ Avança para o próximo caracter. """
        if self.current_char == '\n':
            self.current_line += 1
            self.current_column = 0
        else:
            self.current_column += 1
        self.position += 1
        self.current_char = self.input[self.position] if self.position < len(self.input) else None

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
                continue

            # operadores artiméticos
            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return Token('MULTIPLY', '*')

            if self.current_char == '%':
                self.advance()
                return Token('PERCENT', '%')

            if self.current_char == '/':
                self.advance()
                return Token('DIVIDE', '/')

            # operadores de comparação
            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('MAIOROUIGUAL', '>=')
                return Token('MAIOR', '>')

            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('MENOROUIGUAL', '<=')
                return Token('MENOR', '<')

            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('DIFERENTE', '!=')
                else:
                    raise Exception('Erro léxico')
                # Tratar um '!' solitário como um erro

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token('IGUAL', '==')
                return Token('ATRIBUICAO', '=')

            # simbolos de pontuação
            if self.current_char == ';':
                self.advance()
                return Token('SEMICOLON', ';')

            if self.current_char == ',':
                self.advance()
                return Token('COMMA', ',')

            if self.current_char == '{':
                self.advance()
                return Token('LBRACE', '{')

            if self.current_char == '}':
                self.advance()
                return Token('RBRACE', '}')

            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')

            if self.current_char == '[':
                self.advance()
                return Token('LBRACKET', '[')

            if self.current_char == ']':
                self.advance()
                return Token('RBRACKET', ']')

            # constantes, numeros e identificadores
            if self.current_char == '"':
                return self.string_constant()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char.isalpha() or self.current_char == '_':
                return self.identifier()

        return Token('EOF', None)

    def number(self):
        """ Retorna um token de número (INT_CONSTANT ou FLOAT_CONSTANT). """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        if self.current_char == '.':
            result += self.current_char
            self.advance()
            if self.current_char is not None and self.current_char.isdigit():
                while self.current_char is not None and self.current_char.isdigit():
                    result += self.current_char
                    self.advance()
                return Token('FLOAT_CONSTANT', float(result))
            else:
                # Retrocedendo para tratar o ponto separadamente
                self.position -= 1
                self.current_char = '.'
                return Token('INT_CONSTANT', int(result))
        else:
            return Token('INT_CONSTANT', int(result))

    def identifier(self):
        """ Retorna um token de identificador ou palavra-chave reservada. """
        result = ''
        start_column = self.current_column
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()

        # Se for um identificador, atualizamos a tabela de símbolos
        token_type = self.RESERVED_KEYWORDS.get(result, 'IDENT')
        self.symbol_table.insert(token_type, self.current_line, start_column)
        return Token(token_type, result)

    # considera string_constant o que está escrito entre aspas dupla
    def string_constant(self):
        """ Retorna uma constante do tipo string. """
        result = ''
        self.advance()  # Pula a primeira aspa

        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()

        if self.current_char != '"':
            raise ValueError("String não fechada")

        self.advance()  # Pula a última aspa
        return Token('STRING_CONSTANT', result)


class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, identifier, line, column):
        if identifier not in self.symbols:
            self.symbols[identifier] = []
        self.symbols[identifier].append((line, column))

    def __str__(self):
        for i in self.symbols:
            print(f'{i}: {self.symbols[i]}')
        return str()
