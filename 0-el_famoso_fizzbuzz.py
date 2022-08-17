# El reto consiste en crear un programa que cuente los números del 1 al 100 con un salto de línea para cada número sustituyendo:
#- múltiplos de 3 por "fizz"
#- múltiplos de 5 por "buzz"
#- múltiplos de 3 y 5 por "fizzbuzz"

i = 1
while i <= 100:
    if i%3 == 0 and i%5== 0:
        print ("fizzbuzz\n")
    elif i%3 == 0 and i%5 != 0:
        print("fizz\n")
    elif i%3 !=0 and i%5 ==0:
        print("buzz\n")
    else:
        print (f"{i}\n")
    i +=1