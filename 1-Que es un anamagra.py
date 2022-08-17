#Escribe una función que reciba dos palabras y retorne verdadero y falso si son anagramas.
#Dos palabras iguales no son un anagrama.


def isAnagram (palabra1,palabra2):
    if palabra1 == palabra2 or len(palabra1) != len(palabra2):
        return False
    else:
        for letra in palabra1:
            if palabra2.count(letra) == 0:
                return False
            else:
                return True
            

anagrama = isAnagram("amor","roma")
print(anagrama)

anagrama2 = isAnagram("soga","ganso")
print(anagrama2)

anagrama3 = isAnagram("pan","sal")
print(anagrama3)