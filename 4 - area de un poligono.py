#Crea una única función capaz de calcular y retornar el área de un polígono.
#La función recibirá por parámetro es un polígono a la vez.
#Debe soportar rectángulos, cuadrados y triángulos.

def calcular_area (tipo, base,altura):
    if tipo == "cuadrado":
        return base*base
    if tipo == "rectángulo":
        return base*altura
    if tipo == "triángulo":
        return (base*altura)/2
    
print(calcular_area ("cuadrado",5,0))
print(calcular_area("rectángulo",5,2))
print(calcular_area("triángulo",5,3))
    
    
    