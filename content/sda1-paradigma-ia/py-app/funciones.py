# Función sumaT que devuelve el sumatorio de números desde 0 hasta sum
def sumaT_while (tope):
    suma=0
    i=0
    while i <= tope:
        suma += i
        i += 1
    return suma

def sumaT_for(tope):
    suma=0
    for i in range(1,tope+1):
        suma+=i
    return suma


#Función factorial

def fact_w(num):
    fact=1;
    i=1;
    while num>=2:
        fact*=num
        num-=1
    return fact

def fact_f(num):
    for i in range(1, num+1):
        fact*=i
    return fact


# Función sucesión de fibonacci(n). Siendo n el termino de la sucesión empezando por 0

def fibo1 (n): # devuelve una cadena con la sucesión
    str=""
    =0
    while i<n:


print(f"El sumatorio de 5 es {sumaT_while(5)}  {sumaT_for(5)}")
print(f"El factorial de 5 es {fact_w(5)}")