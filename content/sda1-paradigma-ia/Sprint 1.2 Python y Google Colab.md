---
title: Sprint 1.2 Python y Google Colab
sda: "Misión 1: El nuevo paradigma computacional"
tags:
criterios_evaluacion:
entregable:
---
# 1. Listas

**Lista de comprobació**
- [ ] Definición de variables de tipo *lista*
- [ ] Uso de listas en bucles
- [ ] Funciones `list`, `len`, `range`
- [ ] Segmentación de listas
- [ ] Inmutabilidad vs Mutabilidad
- [ ] Funciones relacionadas con listas

**Recursos:**
- [PY4E - Python List](https://www.py4e.com/lectures3/Pythonlearn-08-Lists.pdf)
- [W3School Python List](https://www.w3schools.com/python/python_lists.asp)

## 1.1Inmutabilidad vs Mutabilidad

En Python, todas las variables tienen tres propiedades:
1. **Identidad (`id`)**: Su dirección de memoria    
2. **Tipo (`type`)**: Qué clase de dato representa (`int`, `str`, `list`, etc.).
3. **Valor**: El dato que almacena en su interior.

La distinción entre **mutable** e **inmutable** determina si ese valor interno puede modificarse **sin alterar su identidad en memoria**.

| **Categoría**  | **Tipos integrados (Built-in)**        | **Comportamiento**                                                                                                                          |
| -------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inmutables** | `int`, `float`, `bool`, `str`, `tuple` | Su estado interno **no puede cambiar** tras la creación. Cualquier "modificación" crea un nuevo objeto en memoria.                          |
| **Mutables**   | `list`, `dict`, `set`                  | Su contenido interno **sí puede cambiar** mediante métodos (`append`, `pop`, `update`, etc.) conservando el mismo identificador de memoria. |

>[!example] Metáfora
> - **Con enteros (Inmutables / Valores simples):** Imagina que tienes una hoja de papel con el número `5` escrito y le haces una **fotocopia**. Si le das la copia a otra persona y esa persona tacha el número y escribe un `10`, tu hoja original sigue intacta.
>``` python
> # CASO 1: Enteros (Inmutables)
>b = 10
>a = b
>a = 20
>print(f"b = {b}")  # Imprime 10 (b no cambia)
>print(f"a = {a}")  # Imprime 20
>```
> - **Con listas (Mutables / Objetos complejos):** No entregas una copia física; compartes el **enlace editable a un Google Docs**. Si la otra persona entra y añade una línea, tú verás el cambio inmediatamente porque **ambos están editando el mismo documento original**.
>``` python
>b = [1, 2, 3]
>a = b
>a.append(4)
>print(f"b = {b}")  # ¡Imprime [1, 2, 3, 4]! (b ha cambiado)
>print(f"a = {a}")  # Imprime [1, 2, 3, 4]
>```


>[!example] Caso de estudio. `append`vs `+`
>Explica la diferencia entre mutar mediante `.append()` y reasignar con `+`
>``` python
>b = [1, 2, 3]
>a = b
>a = a + [4]
>print(f"b = {b}") # Imprime [1, 2, 3] (b no ha cambiado)
>print(f"a = {a}") # Imprime [1, 2, 3, 4]
>```
>**El operador `+` **crea una lista completamente nueva en memoria** al concatenar dos secuencias. Al asignarle a `a` la nueva lista, rompe el vínculo con `b`**

>[!question] ¿IP válida? (IPv4 / CIDR Validator)
>Implementa una función en Python denominada **`es_ip_valida(cadena)`** que reciba un texto con formato **`a.b.c.d/m`** y devuelva `True` si representa una dirección IPv4 con máscara CIDR bien formada, o `False` en cualquier otro caso.
>Para que una cadena represente una dirección IPv4 con prefijo CIDR válida, debe cumplir:
>1. **Estructura general:** La cadena debe contener exactamente una barra inclinada (`/`) que separe la dirección IP de la longitud del prefijo de subred (`m`).
>2. **Prefijo de subred (`m`):**
  >	- `m` debe ser un valor entero.
   >	- Su rango válido debe ser **$0 \le m \le 32$**.
>1. **Dirección IPv4 (`a.b.c.d`):**
  >	- La parte izquierda debe contener exactamente cuatro octetos (`a`, `b`, `c`, `d`) separados por un punto (`.`).        
 >	- Cada uno de los cuatro octetos debe ser un valor numérico entero compuesto únicamente por dígitos.        
  >	- Cada octeto debe encontrarse en el rango decimal de un byte: **$0 \le \text{octeto} \le 255$**.
  >**Utiliza la función `split` con la variabla `cadena`**

## 2. Arrays (numpy)



---


