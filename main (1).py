
import ply.lex as lex


tokens = (
    'Def_funcion',
    'ID',
    'Numerador',
    'Par_left',
    'Par_right',
    'Suma',
    'Resta',
    'Division',
    'Multiplicacion',  
    'For',
    'While',
    'Puts',
    'If',
    'Else',
    'Igual',  
    'Signo_mayor',  
    'Signo_menor',  
    'Igual_doble',  
    'Texto',  
    'Int_var',  
    'Bool_var',  
    'Float_var',  
    'String_var', 
    'Boolean',  
    'Comentario',  
    'Llave_left',  
    'Llave_right',  
    'Mayor_igual',  
    'Menor_igual',  
    'And',  
    'Or',  
    'Chomp',  
    'Med_to_i',  
    'For_in',  
    'Gets_obt',  
    'Return_pal', 
    'End_pal',  
    'Ope_punto',  
    'Ope_puntos', 
    'Float',  
)


t_Suma = r'\+'
t_Resta = r'\-'
t_Multiplicacion = r'\*'
t_Division = r'/'


def t_Def_funcion(t):
    r'definir'
    return t

def t_Numerador(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_Puts(t):
    r'imprimir'
    return t

def t_While(t):
    r'mientras'
    return t
        
def t_Else(t):
    r'entonces'
    return t
        
def t_If(t):
    r'si'
    return t
        
def t_For(t):
    r'para'
    return t
    
def t_Par_left(t):
    r'\('
    return t
    
def t_Par_right(t):
    r'\)'
    return t
    
def t_Igual(t):
    r'='
    return t

def t_Signo_mayor(t):
    r'>'
    return t

def t_Signo_menor(t):
    r'<'
    return t

def t_Igual_doble(t):
    r'=='
    return t

def t_Texto(t):
    r'\".*"'
    return t

def t_Int_var(t):
    r'int'
    return t

def t_Bool_var(t):
    r'bool'
    return t

def t_Float_var(t):
    r'float'
    return t

def t_String_var(t):
    r'string'
    return t

def t_Boolean(t):
    r'true|false'
    return t

def t_Comentario(t):
    r'\#.*'
    pass


def t_Llave_left(t):
    r'{'
    return t

def t_Llave_right(t):
    r'}'
    return t

def t_Mayor_igual(t):
    r'>='
    return t

def t_Menor_igual(t):
    r'<='
    return t

def t_And(t):
    r'&&'
    return t

def t_Or(t):
    r'\|\|'
    return t

def t_Chomp(t):
    r'chomp'
    return t

def t_Med_to_i(t):
    r'to i'
    return t

def t_For_in(t):
    r'en'
    return t

def t_Gets_obt(t):
    r'gets'
    return t

def t_Return_pal(t):
    r'retornar'
    return t

def t_End_pal(t):
    r'fin'
    return t

def t_Ope_punto(t):
    r'\.'
    return t

def t_Ope_puntos(t):
    r'\.\.'
    return t

def t_Float(t):
    r'\[0-9].*'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    return t


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

def leer_archivo(filename):
    with open(filename, 'r') as file:
        data = file.read()
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break  
            print(tok)


leer_archivo('codigo.txt')