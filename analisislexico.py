# Definición de tipos de tokens
class TipoToken:
    IDENTIFICADOR = 1
    PARENTESIS_IZQUIERDO = 2
    CADENA = 3
    PARENTESIS_DERECHO = 4
    PUNTO_Y_COMA = 5
    FIN = 6
    
# Estructura para representar un token
class Token:
    def __init__(self, tipo, lexema):
        self.tipo = tipo
        self.lexema = lexema

# Función para escanear el código fuente y generar tokens
def obtener_siguiente_token(codigo, indice):
    token = Token(TipoToken.FIN, "")

    while indice[0] < len(codigo):
        if codigo[indice[0]] == ' ':
            indice[0] += 1
            continue
        elif codigo[indice[0]] == '(':
            token.tipo = TipoToken.PARENTESIS_IZQUIERDO
            token.lexema = "("
            indice[0] += 1
            break
        elif codigo[indice[0]] == '"':
            token.tipo = TipoToken.CADENA
            indice[0] += 1
            lexema = ""
            while codigo[indice[0]] != '"' and indice[0] < len(codigo):
                lexema += codigo[indice[0]]
                indice[0] += 1
            token.lexema = lexema
            indice[0] += 1
            break
        elif codigo[indice[0]] == ')':
            token.tipo = TipoToken.PARENTESIS_DERECHO
            token.lexema = ")"
            indice[0] += 1
            break
        elif codigo[indice[0]] == ';':
            token.tipo = TipoToken.PUNTO_Y_COMA
            token.lexema = ";"
            indice[0] += 1
            break
        else:
            token.tipo = TipoToken.IDENTIFICADOR
            lexema = ""
            while codigo[indice[0]] != ' ' and codigo[indice[0]] != '(' and codigo[indice[0]] != '"' and \
                    codigo[indice[0]] != ')' and codigo[indice[0]] != ';' and indice[0] < len(codigo):
                lexema += codigo[indice[0]]
                indice[0] += 1
            token.lexema = lexema
            break

    return token

# Código fuente
codigo = 'print("Hola Mundo!");'
indice = [0]

print("Código fuente:", codigo)
print("Tokens generados:")

while True:
    token = obtener_siguiente_token(codigo, indice)
    if token.tipo == TipoToken.IDENTIFICADOR:
        print("Tipo: IDENTIFICADOR, Lexema:", token.lexema)
    elif token.tipo == TipoToken.PARENTESIS_IZQUIERDO:
        print("Tipo: PARENTESIS_IZQUIERDO, Lexema:", token.lexema)
    elif token.tipo == TipoToken.CADENA:
        print("Tipo: CADENA, Lexema:", token.lexema)
    elif token.tipo == TipoToken.PARENTESIS_DERECHO:
        print("Tipo: PARENTESIS_DERECHO, Lexema:", token.lexema)
    elif token.tipo == TipoToken.PUNTO_Y_COMA:
        print("Tipo: PUNTO_Y_COMA, Lexema:", token.lexema)
    elif token.tipo == TipoToken.FIN:
        print("Tipo: FIN")
        break