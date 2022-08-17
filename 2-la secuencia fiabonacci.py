#Escribe un programa que imprima los 50 primeros números de la secuencia fiabonacci empezando en cero. Cada número es la suma de los anteriores.
#0,1,1,2,3,5,8,13...

secuencia = []
i = 0

while i<= 50:
    if len(secuencia) < 2:
        secuencia.append(i)
        print (secuencia[i])
    else:
        print (secuencia[i-1])
        secuencia.append(secuencia[i-2] + secuencia[i-1])
    i += 1
    
print (secuencia)
    