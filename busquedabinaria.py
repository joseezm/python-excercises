from random import randrange
def insertionM(L1,L2):
    R=[]
    cont=0
    while L1!=[] and L2!=[]:
        cont=cont+1
        if L1[0]<L2[0]:
            R.append(L1.pop(0))
        else:
            R.append(L2.pop(0))
    R=R+L1+L2
    return R,cont
#a=[1,4,5,23,24,26,48,59,60]
#b=[0,3,4,6,7,8,13,15,26,27,38,49,50,60,68,78,90]
#print insertionM(a,b)

def insertionMej(L1,L2):
    cont=0
    i=0
    if len(L2)<len(L1):
        aux=L2
        L2=L1
        L1=aux
    while i<len(L1) and L2!=[]:
        cont=cont+1
        if L2[0]<=L1[i] and i==0:
            L1.insert(0,L2.pop(0))
        if L2[0]<=L1[i] and L2[0]>=L1[i-1]:
            L1.insert(i,L2.pop(0))
        i=i+1
    L1=L1+L2
    return cont,L1
a=[]
b=[]

for i in range(0,1000):
    a.append(randrange(0,200))
for i in range(0,1000):
    b.append(randrange(0,200))

a.sort()
b.sort()
print insertionMej(a,b)

def busquedaBin(L,e,inicio=-1,fin=-1,cont=0):
    cont=cont+1
    print inicio,fin
    if inicio==-1 and fin ==-1:
        inicio=0
        fin=len(L)-1
    if inicio==fin:
        if L[inicio]==e:
            return inicio,cont
        return False,cont
    m=(inicio+fin)//2
    if e==L[m]:
        return m,cont
    elif m==inicio:
        if e==L[fin]:
            return fin,cont
    elif e>L[m]:
        inicio=m+1
    else:
        fin=m-1
    return busquedaBin(L,e,inicio,fin,cont)

#print busquedaBin(b,0)


def iBin(L,e,inicio,fin,cont):
    cont=cont+1
    if inicio==fin:
        if L[inicio]>e:
            return inicio+1
        return inicio
    m=(inicio+fin)//2
    if e==L[m]:
        return m
    elif m==inicio:
        if e<L[inicio]:
            return inicio
        elif e>L[inicio] and e<=L[fin]:
            return fin
        return fin+1
    elif e>L[m]:
        inicio=m
    else:
        fin=m
    return iBin(L,e,inicio,fin,cont)

def insertionBin(L):
    cont=0
    for i in range(1,len(L)):
        aux=iBin(L,L[i],0,i,cont)
        L.insert(aux,L.pop(i))
        print L
    return L

#print insertionBin([4,5,3,7,6,9,23,24,12,36,43,12,34,25,634,457,43,63,546,74,865,999])


def merge(L,cont=0):
    if len(L)<2:
        return L
    mitad=len(L)//2
    der=merge(L[mitad:])
    izq=merge(L[:mitad])
    res=[]
    while len(der)>0 and len(izq):
        if izq[0]<der[0]:
            res.append(izq.pop(0))
        else:
            res.append(der.pop(0))
    return res+der+izq
#print merge(a)
