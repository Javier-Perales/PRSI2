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