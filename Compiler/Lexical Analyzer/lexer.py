import sys
import re

TOKEN_TYPES = {
    'COMMENT': r'->([^"\\]|\\.)*',
    'KEYWORD': r'take|show|either|whatif|or|var|skip|try|catch|finally|from|func|while|do|skip|to|num|bool|str|stop|carryon|give',
    'NUMBER': r'\d+',
    'STRING': r'"([^"\\]|\\.)*"',
    'BOOL': r'on|off',
    'IDENTIFIER': r'[a-zA-Z][a-zA-Z0-9_]*',
    'OPERATOR': r'<=|>=|==|<|>|\+|-|!=|\*|/|=',
    'LEFT_PAREN': r'\(',
    'RIGHT_PAREN': r'\)',
    'LEFT_BRACE': r'{',
    'RIGHT_BRACE': r'}',
    'LEFT_SQUARE_BRACKET': r'\[',
    'RIGHT_SQUARE_BRACKET': r'\]',
    'COMMA': r',',
    'COLON': r':',
    'ENDOFSTMT': r';',
}

TOKEN_REGEX = '|'.join(f'(?P<{token_type}>{pattern})' for token_type, pattern in TOKEN_TYPES.items())

def lexer(filename):
    tokens = []
    with open(filename, 'r') as file:
        for line in file:
            for match in re.finditer(TOKEN_REGEX, line):
                for name, value in match.groupdict().items():
                    if value is not None:
                        tokens.append((name.upper(), value))
                        break  
    return tokens

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python lexer.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    tokens = lexer(filename)

    output_tokens = []
    for token_type, token_value in tokens:
        output_tokens.append(f'<{token_type}, "{token_value}">')

    output_string = ',\n'.join(output_tokens)
    print('[' + output_string + "]")