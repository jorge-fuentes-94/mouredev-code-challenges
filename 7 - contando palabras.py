#Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# * - Los signos de puntuación no forman parte de la palabra.
# * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

mensaje = "Mi nombre es Jorge. Mi nombre completo es Jorge Fuentes."
palabras = mensaje.replace(".","").split(" ")
contador = {}

for palabra in palabras:
    if palabra == "." or palabra == " ":
        palabras.remove(palabra)
    elif palabra not in contador:
        contador[palabra] = 1
    else:
        contador[palabra] += 1
        
print (contador)
