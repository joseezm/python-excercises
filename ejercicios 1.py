def retornar(x):
    lista=[]
    for i in range(0,x+1):
        lista.append(i)
    return lista

print retornar(5)


def retornar2(x):
    lista=[]
    if x==-1:
        return lista
    else:
        lista=retornar2(x-1)
        lista.append(x)
        return lista

print retornar2(5)
    
        
def suma(x):
    suma=0
    for i in range(0,x+1):
        suma=suma+i
    return suma

print suma(5)


def suma2(x):
    suma=0
    if x==-1:
        return suma
    else:
        suma=suma2(x-1)
        suma=suma+x
        return suma

print suma2(5)