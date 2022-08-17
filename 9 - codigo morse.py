#Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

diccionario_morse = {
    "a": "·-",
    "b": "-···",
    "c": "-·-·",
    "d": "-··",
    "e": "·",
    "f": "··-·",
    "g": "--·",
    "h": "····",
    "i": "··",
    "j": "·---",
    "k": "-·-",
    "l": "·-··",
    "m": "--",
    "n": "-·",
    "ñ": "--·--",
    "o": "---",
    "p": "·--·",
    "q": "--·-",
    "r": "·-·",
    "s": "···",
    "t": "-",
    "u": "··-",
    "v": "···-",
    "w": "·--",
    "x": "-··-",
    "y": "-·--",
    "z": "--··",
    "0": "-----",
    "1": "·----",
    "2": "··---",
    "3": "···--",
    "4": "····-",
    "5": "·····",
    "6": "-····",
    "7": "--···",
    "8": "---··",
    "9": "----·",
    ".": "·-·-·-",
    ",": "--··--",
    "?": "··--··",
    '"': "·-··-·",
    "/": "-··-·"
}
diccionario_latino = {value: key for key, value in diccionario_morse.items()}

def traducir_a_morse (texto):
    frase_traducida = ""
    
    for letra in texto.lower():
        letra_morse = diccionario_morse.get(letra)
        if letra == " ":
            frase_traducida += " "
        else:
            frase_traducida += f"{letra_morse}"
    print (f"La frase traducida es: {frase_traducida}")
    
def traducir_a_natural(texto):
    frase_traducida = ""
    for letra in texto.split(" "):
        for letra_morse in letra.split():
            letra_latina = diccionario_latino.get(letra_morse)
            if letra_morse == "....--.....---..-...-.." or letra_latina is None:
                frase_traducida += "*"
            else:
                frase_traducida += letra_latina
        frase_traducida += " "

    print(f"La frase traducida es: {frase_traducida}")
    
def isMorse(texto):
    for letra in texto.lower().split():
        if letra  [0] == "." or letra [0] == "-":
            return True
        else:
            return False
   
input = input("Escribe aquí la frase en letras o en código morse y te la traduciré: ")

if isMorse(input):
    traducir_a_natural(input)
else:
    traducir_a_morse(input.lower())