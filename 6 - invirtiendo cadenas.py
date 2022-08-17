#Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
#- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

def invertir_cadena (cadena):
    letras = [x for x in cadena]
    reverso = []
    i = len(letras) - 1
    while i >= 0:
        reverso.append(letras[i])
        i -= 1
    return ''.join(reverso)

input = input("Escribe la cadena a transformar: ")
resultado = invertir_cadena(input)

print(resultado)

    
    