# Escribe un programa que se encargue de comprobar si es un número o no primo. Imprime los números del 1 al 100.
def isPrimo (numero):
    if numero <= 2:
        return True
    elif numero % 2 == 0 or numero % 3 ==0 or numero % 4 == 0 or numero % 5 == 0 or numero % 6 == 0 or numero % 7 == 0 or numero % 8 == 0 or numero % 9 == 0:
        return False
    else:
        return True

for i in range(101):
    primo = isPrimo(i)
    print (f"{i} - {primo}")