---
title: "Sprint 1.1: Introducción a Python"
sda: "Misión 1: Paradigma IA"
tags:
  - Python
criterios_evaluacion:
entregable: Archivo .sb3 o enlace Aules
---
## 1. ¿Por qué Python?

![https://www.youtube.com/watch?v=jsiVnOtqe6k&t=1s](https://www.youtube.com/watch?v=jsiVnOtqe6k&t=1s)

## 2. Variables, expresiones y declaraciones

**Recurso:** [PY4E - Variables, expresiones y declaraciones](https://www.py4e.com/lessons/memory)


> [!task] Ejercicios
> 1. Escribe un programa que solicite un nombre y cuya salida sea 'Hola \[nombre]'
> 2. Escribe un programa que solicite al usuario horas trabajadas y precio por hora, para obtener el salario bruto. Deberás usar `input` para leer la entrada del usuario y `float` para convertir la cadena a número.
> 3. Modifica el programa anterior para solicitar el porcentaje de retención que se aplica para calcular el salario neto.
> 

### 2.1 F-strings

```python
total = 15.67894
# Muestra 2 decimales
print(f"Total: {total:.2f}")  # Salida: Total: 15.68
# Muestra 1 decimal
print(f"Total: {total:.1f}")  # Salida: Total: 15.7
# Muestra 4 decimales
print(f"Total: {total:.4f}")  # Salida: Total: 15.6789
```
Las **f-strings** (_Formatted String Literals_), introducidas en Python 3.6, permiten incrustar expresiones arbitrarias de Python dentro de cadenas de texto prefijando la cadena con la letra `f` En tiempo de ejecución, cualquier contenido encerrado entre llaves `{}` se evalúa en el ámbito (_scope_) actual y se convierte a texto.

```python
nombre = "Lucía"
precio = 19.99
unidades = 3

# Variables directas
print(f"Cliente: {nombre}")

# Operaciones aritméticas y llamadas a métodos
print(f"Total: {precio * unidades} €")
print(f"Mayúsculas: {nombre.upper()}")
```

## 3. Condicionales

**Recurso:** [Py4E - Ejecución Condicional](https://www.py4e.com/lessons/logic)

>[!question] Condicionales 1
> **Salario bruto v2.** Calcula el salario bruto de un trabajador sabiendo que se paga la tarifa por hora hasta las 35 horas semanales. Para todas las horas trabajadas por encima de 35 se debe pagar 1'5 veces la tarifa asignada. No es necesario realizar la verificación de errores en la entrada de usuario.

>[!question] Condicionales 2
> **Salario bruto v2 a prueba de errores**. Modifica el programa anterior para que si el usuario introduce texto en lugar de dígitos numéricos, el programa intercepte el error y advierta el fallo y finalice el programa.

>[!question] Condicionales 3
> **Facturación dinámica con validación robusta de datos.** Se necesita un script de Python que calcule el coste de los servicios prestados por una determinada empresa donde se aplican descuentos según el perfil del cliente. 
> 1. Solicitar
> 	a. Número de horas realizadas.
> 	b. Tarifa base por hora (en euros).
> 	c. Código del cliente: `SOCIO`, `ESTUDIANTE`, `GENERAL`
> 2. Blindaje de entrada: Si las horas o la tarifa no son valores numéricos, el programa debe capturar el error y mostrar `Error: Se requiere un valor numérico para horas y tarifas.`
> 3. Validación de rango: Si las horas son menores o iguales a 0 o superan las 60 horas semanales, debe advertir: `Error El número de horas debe estar entre 1 y 60`
> 4. Cálculo de liquidación base y horas extra:
> 	a. Hasta 40 horas: se paga la tarifa regular.
> 	b. Por encima de 40 horas, el exceso se liquida a 1.5 veces la tarifa regular.
> 5. Modificador de perfil:
> 	a. Si el código es `SOCIO` se aplica un 10% de descuento.
> 	b. Si es `ESTUDIANTE`, se aplica un 15% de descuento.
> 	c. Si es `GENERAL`, no se aplica descuento.

![[recursos/Condicionales2026-09-25 12.13.04.excalidraw.light.svg]]


## 4. Funciones

**Recurso:** [Py4E - Funciones](https://www.py4e.com/lectures3/Pythonlearn-04-Functions.pdf)

>[!question] Función Salario_Bruto
>Crea una función que reciba dos parámetros, número de horas y tarifa, y devuelva el salario bruto que se deberá pagar, teniendo en cuenta que a partir de 35 horas se pagará 1,5 veces la tarifa.

>[!question] Función Descuento
>Crear una función que devuelva el porcentaje de descuento que se aplica a la tarifa dependiendo del cliente:
>a. Si el código es `SOCIO` se aplica un 10% de descuento.  
>b. Si es `ESTUDIANTE`, se aplica un 15% de descuento.  
>c. Si es `GENERAL`, no se aplica descuento.
## 5. Bucles

**Recurso:**[PY4E Bucles](https://www.py4e.com/lectures3/Pythonlearn-05-Iterations.pdf)

>[!question] Función Sumatorio
>Crear una función que devuelva el sumatorio de un número que recibe como parámetro.

>[!question] Función es Primo
>Crea una función que determine si un número es primo. La función debe devolver un booleano.

>[!question] Función Fibonacci
>Genera una función que devuelva el valor de Fibonacci que corresponde a la posición que se indica por parámetro.

## 6. Recursividad
La recursividad es una técnica en programación en la que una función se llama a sí misma para resolver un problema. **El problema se resuelve dividíendolo en subproblemas más pequeños y aplicando la misma función de manera repetitiva**.

Los elementos claves de la recursividad son:
1. **Caso base:** Es la condición que detiene la recursividad. Sin un caso base, la función seguiría llamándose indefinidamente, lo que llevaría a un desbordamiento de la pila de llamadas.
2. **Llamada recursiva:** Es el momento en que la función se llama a sí misma con un argumento modificado. Este argumento generalmente está diseñado para acercar el problema al caso base.

>[!example] Factorial de un número
>`n!=nx(n-1)x(n-2)x...x1`
>Podemos definir el factorial de forma recursiva: `n!=nx(n-1)!`
>En Python sería:
>```python
>def factorial(n):
>	#Caso base: si n es 0, devuelve 1
>	 if n==0:
>		 return 1
>	else:
>		return n*factorial(n-1)
>```


>[!question] Implementa las siguientes funciones de forma recursiva
>Previamente establece el caso base y el caso general. Por último, implementa la función.
>1. Sumatorio de un número `sumaT(num)`
>2. Inverso de un número `invertir(3452)=2543`
>3. Sucesión de Fibonacci. Debe visualizar por consola la lista de Fibonacci hasta la posición indicada
>	- `sucFibo(1) - 1`
>	- `sucFibo(2) - 1`
>	- `sucFibo(3) - 2`
>	- `sucFibo(4) - 3`
>	- `sucFibo(5) - 5`
>	- `sucFibo(6) - 8`

**Recurso:** [Actividades sobre cadenas](https://colab.research.google.com/drive/1Ych3o9W7XIDFCi0_0chhJO_DYBRqrSHo?usp=sharing)
