# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

numero_inicial = int(input("Escribe aquí el número a transformar."))
cociente_parcial = ""
numero_binario = ""

while numero_inicial != 0:
    cociente = numero_inicial % 2
    numero_inicial = numero_inicial // 2
    cociente_parcial += str(cociente)
    
    for cociente in cociente_parcial:
        numero_binario += cociente
        
print (numero_binario)


