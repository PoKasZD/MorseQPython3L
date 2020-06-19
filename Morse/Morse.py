import time
import sys
import androidhelper
droid = androidhelper.Android()
morse_code = {
            ' ': '/',
            'A': '.-', 'B': '-...',
            'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....',
            'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.',
            'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-',
            'U': '..-', 'V': '...-',
            'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '0': '-----', '1': '.----',
            '2': '..---', '3': '...--',
            '4': '....-', '5': '.....',
            '6': '-....', '7': '--...',
            '8': '---..', '9': '----.',
            '?':'..--..', '/':'-..-.', 
            '-':'-....-','(':'-.--.', 
            ')':'-.--.-', '.':'.-.-.-',
            ',': '--..--', "'": '.----.',
            '!': '-.-.--', '+': '.-.-.',
            '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.',
            '¿': '..-.-'
            
        
        }

 
def decode(morsecode):
    ''' Decodifica codigo morse '''
    code = morsecode.split(' ')
    text = ''
    for item in code:
        for key, value in morse_code.items():
            if item == value:
                text += key
                break
    return text.capitalize()
 
def encode(plaintext):
    ''' Codifica em codigo morse '''
    code = ''
    for char in plaintext.upper():
        if char in morse_code.keys():
            code += morse_code[char] + ' '
    return code
pokas = True
while pokas == True:
    time.sleep(2.0)
    print("*" * 30)
    frase = "C O D I G O M O R S E \n by: PoKasZD"
    for i in list(frase):
        print(i, end='')
        sys.stdout.flush()
        time.sleep(0.2)
    print("".join(''))
    print("*" * 30)

    escolha = int(input("Escolha uma Opção:\n 1.Codificar\n 2.Decodificar \n :"))

    if escolha == 1:
        time.sleep(0.3)
        texto = input("Digite o texto para ser Codificado:\n")
        cod = encode(texto)
        print(cod)
        droid.setClipboard(cod)
    elif escolha == 2:
        time.sleep(0.3)
        texto = input("Digite o Código para ser Decodificado:\n")
        decod = decode(texto)
        print(decod)
        droid.setClipboard(decod)
    elif escolha == 0:
        frase = "Obrigado!"
        for i in list(frase):
            print(i, end='')
            sys.stdout.flush()
            time.sleep(0.2)
        pokas = False
    print("".join(''))
        