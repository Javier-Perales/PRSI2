def importeBruto(nH, tarifa):
    return nH*tarifa if (nH<35) else 35*tarifa+(nH-35)*tarifa*1.5



def sumaT(num):
    n=1
    suma=0
    while n<=num:
        suma+=n
        n+=1
    return suma


def esPrimo(num):
    if num==1: return True
    div=2
    while div<num-1:
        if num%div==0: return False
        div+=1
    return True

valor=int(input("Introduce valor> "))
print(f"{sumaT(valor)}")
print(f"{valor} es primo") if esPrimo(valor) else print(f"{valor} no es primo")

#print (f"{importeBruto(10,5)}")
#print (f"{importeBruto(40,10)}")

#if 3<5: print ("3 es menor que 5")