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

> [!exercise] Ejercicios
> **Salario bruto v2.** Calcula el salario bruto de un trabajador sabiendo que se paga la tarifa por hora hasta las 35 horas semanales. Para todas las horas trabajadas por encima de 35 se debe pagar 1'5 veces la tarifa asignada. No es necesario realizar la verificación de errores en la entrada de usuario.
>  ---
> **Salario bruto v2 a prueba de errores**. Modifica el programa anterior para que si el usuario introduce texto en lugar de dígitos numéricos, el programa intercepte el error y advierta el fallo y finalice el programa.
>  ---
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
> ---
