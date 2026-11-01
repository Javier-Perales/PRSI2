---
title: Sprint 1.3 Deconstrucción de un Perceptrón
sda: El nuevo paradigma computacional
tags:
criterios_evaluacion:
entregable:
---
# 1. Introducción al Machine Learning

El **aprendizaje automático**, conocido en inglés como _Machine Learning_ (**ML**), es un subcampo de la **inteligencia artificial (IA)** que se centra en el desarrollo de algoritmos y modelos capaces de aprender patrones a partir de los datos para realizar predicciones, clasificaciones o tomar decisiones, sin necesidad de programar explícitamente todas las reglas que deben seguir.

Podemos considerar el _Machine Learning_ como un **nuevo paradigma de programación**. En la programación tradicional, los desarrolladores escriben instrucciones y reglas que el ordenador ejecuta para obtener un resultado. En cambio, en el aprendizaje automático, proporcionamos datos a un algoritmo para que, mediante un proceso de entrenamiento, aprenda las relaciones y patrones que le permitan resolver un problema.

Esto no significa que desaparezca la programación: seguimos necesitando algoritmos y código, pero ahora el sistema puede aprender determinadas reglas de decisión a partir de ejemplos, en lugar de tener que definirlas manualmente.

## 1.1 Los principales paradigmas del aprendizaje automático

Dentro del _Machine Learning_, podemos distinguir tres paradigmas principales de aprendizaje:

1. **Aprendizaje supervisado (**_**Supervised Learning**_**):** En este paradigma, el modelo se entrena utilizando un conjunto de datos etiquetados, es decir, ejemplos en los que conocemos tanto los datos de entrada como la salida esperada. El objetivo es que el modelo aprenda la relación entre las entradas y sus correspondientes salidas para poder realizar predicciones sobre datos nuevos que no ha visto durante el entrenamiento.
	Por ejemplo, podemos entrenar un modelo para distinguir imágenes de perros y gatos utilizando fotografías previamente etiquetadas. Durante el entrenamiento, el modelo compara sus predicciones con las respuestas correctas y ajusta sus parámetros para reducir los errores.
    
    El aprendizaje supervisado se utiliza principalmente para resolver problemas de **clasificación**, cuando queremos asignar una categoría a un dato, y de **regresión**, cuando queremos predecir un valor numérico.
    
2. **Aprendizaje no supervisado (**_**Unsupervised Learning**_**):** En este caso, el modelo trabaja con datos que no tienen etiquetas asociadas a una respuesta conocida. Su objetivo es descubrir patrones, relaciones o estructuras que puedan existir en los datos.
    
    Una de las técnicas más conocidas es el _clustering_ o **agrupamiento**, que permite identificar conjuntos de elementos que comparten características similares.
    
    Por ejemplo, una plataforma de comercio electrónico puede analizar los hábitos de navegación y compra de sus clientes para agruparlos en segmentos con intereses semejantes. Estos grupos pueden utilizarse posteriormente para personalizar recomendaciones de productos o diseñar campañas comerciales, sin necesidad de haber definido previamente a qué grupo pertenece cada cliente.
    
3. **Aprendizaje por refuerzo (**_**Reinforcement Learning**_**):** En este paradigma, un agente aprende a tomar decisiones mediante la interacción con un entorno. Cada vez que realiza una acción, el entorno puede proporcionarle una recompensa o una penalización, que le sirve como señal para mejorar su comportamiento.
    
    El objetivo no consiste necesariamente en obtener la mayor recompensa inmediata, sino en **aprender una estrategia que maximice la recompensa acumulada a lo largo del tiempo**.
    
    Este paradigma se utiliza, por ejemplo, en sistemas de inteligencia artificial capaces de aprender a jugar al ajedrez, al Go o a determinados videojuegos mediante la experiencia. También tiene aplicaciones en robótica, donde un robot puede aprender a desplazarse o manipular objetos mediante procesos de prueba, evaluación y mejora.
    

## 1.2 Del aprendizaje supervisado a las redes neuronales

Una de las familias de modelos más importantes dentro del aprendizaje automático es la de las **redes neuronales artificiales (**_**Artificial Neural Networks**_**, ANN)**.

Las **redes neuronales** son un conjunto de algoritmos inspirados en la estructura y funcionamiento del cerebro humano, diseñados para reconocer patrones y aprender de los datos. Están compuestas por capas de nodos (o "neuronas") que procesan la información y transmiten señales a través de conexiones ponderadas.

![[recursos/red_neuronal.png]]


Las redes neuronales artificiales de más de una capa se conocen como **redes neuronales profundas** o **Deep Learning**. Estas redes son capaces de aprender representaciones jerárquicas de los datos, lo que las hace especialmente efectivas para tareas complejas como el reconocimiento de imágenes, el procesamiento del lenguaje natural y la traducción automática.

Podríamos pensar que la red neuronal es como una red de filtros. Pensando en el reconocimiento de datos, y siguiendo la analogia de la red de filtros, una primera capa detectaría formas simples (líneas, colores), la siguiente combinaría esas formas para detectar patrones más complejos (círculos, cuadrados), y las últimas capas identificarían un objeto completo (un gato, una persona).

Para entender mejor cómo funcionan las redes neuronales, es útil conocer algunos conceptos clave, empecemos con el **perceptrón, desarrollado por Frank Rosenblatt a finales de la década de 1950.**

### 1.2.1 El Perceptrón

El perceptrón no es otra cosa que la red neuronal más simple. Su función es actuar como un algoritmo de clasificación binaria, es decir, un sistema que toma una decisión y da una respuesta de "si" o "no" (representado por 1 o 0).

![[recursos/perceptron 1.png]]
Imaginemos que el Perceptrón debe decidir si vamos a la playa o no, basándose en tres factores:

- **_x1_**: ¿Está soleado? (1 para sí, 0 para no)
- **_x2_**: ¿Es fin de semana? (1 sí, 0 no)
- **_x3_**: ¿Tenemos trabajo pendiente? (1 sí, 0 no)

Cada entrada tiene un peso (**w1**​,**w2**​,**w3**​) que representa su importancia. Por ejemplo, "hace sol" (w1​=0.6) puede ser más importante que "ser fin de semana" (w2​=0.4). "Tener trabajo" sería un inhibidor, así que tendría un peso negativo (w3​=−0.8). 

*El **Bias (b)***, también conocido como **sesgo o umbral**, se podría entender como la predisposición de la persona a ir a la playa, por ejemplo, si le encanta la playa, el sesgo sería un valor muy alto, ya que iría a la playa aunque no se den las condiciones ideales. Si es una persona *anti-playa*, el bias sería un número negativo, ya que no iría a la playa aunque se den las condiciones ideales.

Una vez conocidos los pesos y el sesgo, el Perceptrón realiza una suma ponderada de las entradas: $z = (x_1 \cdot w_1) + (x_2 \cdot w_2) + (x_3 \cdot w_3) + b$ Finalmente, una **función de activación** (en el Perceptrón simple, sería una **función escalón**), decide si vamos o no a la playa:,

- Si $z > 0$, entonces la salida es 1 (vamos a la playa).
- Si $z \le 0$, entonces la salida es 0 (no vamos a la playa).

>[!tip] Perceptrón para decidir si vamos a la playa
> Copia el siguiente código para calcular la salida del perceptrón en función de las entradas, pesos y sesgo que hemos visto en el ejemplo anterior. Ejecútalo y observa el resultado.
>``` python
 >Definición de entradas
  >  x1 = 1  # Está soleado
  >  x2 = 1  # Es fin de semana
  >  x3 = 0  # No tenemos trabajo pendiente
  >  # Definición de pesos
  >  w1 = 0.6  # Peso para "Está soleado"
  >  w2 = 0.4  # Peso para "Es fin de semana"
  >  w3 = -0.8 # Peso para "No tenemos trabajo pendiente"
  >  # Definición del sesgo
  >  b = 0.2   # Sesgo
  >  # Cálculo de la suma ponderada
  >  z = (x1 * w1) + (x2 * w2) + (x3 * w3) + b
  >  # Función de activación (función escalón)
  >  output = 1 if z > 0 else 0
  >  print("Salida del perceptrón (1: Vamos a la playa, 0: No vamos a la playa):", output)
>```
>

# 2. Perceptrón en Python

**Recursos:**
- [w3School numpy](https://www.w3schools.com/python/numpy/default.asp)
- [w3schools matplotlib](https://www.w3schools.com/python/matplotlib_intro.asp) 

Vamos a implementar un perceptrón simple en Python utilizando _Numpy_ y _Matplotlib_ para visualizar los resultados. El perceptrón será capaz de aprender a clasificar puntos en un espacio bidimensional, por lo que recibirá como entrada _x1_ y _x2_, que corresponderán a las coordenadas de los puntos en un plano cartesiano.

![[recursos/perceptron_coord.png]]

Si el perceptrón devuelve un valor negativo, clasificaremos el punto en la clase 0 (por ejemplo, color azul). Si devuelve un valor positivo, lo clasificaremos en la clase 1 (color naranja).

![[recursos/grafica_coord.png|400]]

Como vimos anteriormente, para que el perceptrón tome una decisión, deberá ajustar los parámetros de los pesos(_w1 , w2_) y el sesgo (_b_). Esto es es la idea del problema a resolver y a continuación vamos a ver como funciona internamente el perceptrón.

>[!example] Fase 1: Perceptron en Python 1.
>- Crea un nuevo cuaderno en Google Colab y nómbralo "Perceptron en Python".
>- Importa las bibliotecas necesarias: `numpy` como `np` para cálculos numéricos y `matplotlib.pyplot` como `plt` para visualización.
>- Copia y pega el siguiente código y ejecutalo.
>``` python
># Datos estáticos para la Clase 0
>    class_0 = np.array([
>        [0.1745, 0.6976], [0.2799, 0.7828], [0.4983, 1.2015], [0.8281, 1.0315],
>        [0.7770, 1.5834], [0.4316, 0.8576], [0.4897, 1.2523], [0.6931, 1.3653],
>        [0.8953, 1.6119], [1.0863, 1.8986], [1.2721, 1.8596], [1.3435, 2.4287],
>        [1.7224, 2.3023], [1.7081, 2.4461], [1.9125, 2.7663], [0.9785, 1.7225],
>        [1.1105, 1.9444], [1.4924, 2.2265], [1.7377, 2.4571], [-0.0123, 0.7481]
>    ])
>
>    # Clase 1 (roja)
>    class_1 = np.array([
>        [0.2869, -0.9575], [0.1711, -0.4289], [0.4639, -0.4998], [0.6413, -0.1982],
>        [0.7431, 0.0401], [0.1584, -0.9995], [0.452, -0.5633], [0.7490, -0.2185],
>        [0.7854, -0.0175], [1.0898, -0.0683], [1.1785, 0.4474], [1.6701, 0.7713],
>        [1.6723, 1.3858], [1.8800, 1.2988], [1.1344, 0.2818], [1.2138, 0.6139],
>        [1.3835, 0.5055], [1.5458, 1.0895], [1.9452, 1.3496], [-0.0134, -1.0373]
>    ])
>
>
>    # Dibuja los puntos de cada clase
>    plt.scatter(class_0[:, 0], class_0[:, 1], label='Clase 0')
>    plt.scatter(class_1[:, 0], class_1[:, 1], label='Clase 1')
>
>    # Añade una leyenda para identificar las clases
>    plt.legend()
>
>    # Muestra la gráfica
>    plt.show()
>```
>
> - Los datos de los arrays `class_0` y `class_1` representan las coordenadas (x1, x2) de los puntos en el espacio bidimensional. Cada punto en `class_0` pertenece a la clase 0 (color azul) y cada punto en `class_1` pertenece a la clase 1 (color naranja).
>- La función `plt.scatter()` se utiliza para dibujar los puntos en la gráfica. Recuerda que `class_0[:, 0]` obtiene los valores de la primera columna (x1) y `class_0[:, 1]` obtiene los valores de la segunda columna (x2). Igualmente para `class_1`.
>- La función `plt.legend()` añade una leyenda a la gráfica para identificar las clases.
>- Finalmente, `plt.show()` muestra la gráfica con los puntos de ambas clases.

Una vez entendida la estructura de datos para almacenar los puntos de cada clase, vamos a implementar la lógica del perceptrón.

>[!example] Fase 2: Perceptrón en Python 2
>Continuando con el cuaderno "Perceptron en Python", añade una nueva celda de código y copia el siguiente código para implementar la lógica del perceptrón. Ejecuta la celda para ver los resultados.
>- **Modifica los parámetros , hasta obtener una buena clasificación de los puntos.**
>
>``` python
># Funcion activación  
>    def f_activacion(x1, x2, w1, w2, b):
>        z = w1 * x1 + w2 * x2 + b
>        # Función de activación  if z >= 0, devolver 1, sino devolver 0
>        return 1 if z >= 0 else 0
>
>
>    # Modifica las variables a valores deseados
>    w1 = 1
>    w2 = 1
>    b = 0
>
>    # Evalua la clasificación para la class_0
>    aciertos_class_0 = 0
>    for punto in class_0:
>        z = f_activacion(punto[0], punto[1], w1, w2, b)
>        if z == 0:  # Class 0 cuando f_activación devuelve 0
>            aciertos_class_0 += 1
>
>    # Evalua la clasificación para la class_1
>    aciertos_class_1 = 0
>    for punto in class_1:
>        z = f_activacion(punto[0], punto[1], w1, w2, b)
>        if z == 1: # Class 1 cuando f_activación devuelve 1
>            aciertos_class_1 += 1
>
>    # Cálculo de porcentajes de aciertos
>    total_class_0 = len(class_0)
>    total_class_1 = len(class_1)
>    tasa_aciertos_class_0 = aciertos_class_0 / total_class_0
>    tasa_aciertos_class_1 = aciertos_class_1 / total_class_1
>
>
>    print(f"-Tasa aciertos para clase 0: {aciertos_class_0} ({tasa_aciertos_class_0 *100}%)")
>    print(f"-Tasa aciertos para clase 0: {aciertos_class_1} ({tasa_aciertos_class_1*100}%)")
>```


>[!example] Fase 3: Perceptrón en Python 3
>Vamos a representar gráficamente la frontera de decisión del perceptrón representando los valores de _z_. Modificaremos los valores por medio de un deslizador (_slider_), para ver cómo afecta a la clasificación de los puntos cada uno de los puntos.
>
>Añade una celda nueva y copia el siguiente código. Ejecuta la totalidad de las celdas del cuaderno.
> - **Analiza el código. Comenta las líneas donde se calcula `w`, `X` y `z`**
> - **Utiliza los sliders para que el perceptrón converja en una solución. **
> 
>``` python
>from ipywidgets import interact
>@interact(
>    w0=(-4.0, 4.0, 0.1),
>    w1=(-4.0, 4.0, 0.1),
>    b=(-3.0, 3.0, 0.1)
>)
># --- 3. Definimos la función que se ejecutará con cada cambio ---
>def actualizar_grafica(w0= 0, w1= 0, b= 0):
>    """
>    Esta función recalcula 'z' y redibuja la gráfica
>    cada vez que se mueve un slider.
>    """
>    w = np.array([w0, w1])
>    X = np.vstack((class_0, class_1))
>    z = np.dot(X, w) + b
>   
>    z_class_0 = z[:len(class_0)]
>    z_class_1 = z[len(class_0):]
>
>    # Creamos una figura nueva para la gráfica
>    plt.figure(figsize=(10, 2))
>
>    # Dibuja los puntos
>    plt.scatter(z_class_0, np.zeros_like(z_class_0), label='Clase 0', zorder=3, c='skyblue')
>    plt.scatter(z_class_1, np.zeros_like(z_class_1), label='Clase 1', zorder=3, c='salmon')
>
>    # Dibuja la línea de referencia en el cero
>    plt.axvline(0, color='grey', linestyle='--', alpha=0.8)
>
>    # Estilo
>    plt.yticks([])
>    plt.xlabel("Dimensión z")
>    plt.title(f"Proyección en z para w=[{w0:.1f}, {w1:.1f}] y b={b:.1f}")
>    plt.legend()
>    plt.grid(axis='x', linestyle=':', alpha=0.5)
>    plt.xlim(z.min() -1, z.max() + 1) # Ajusta los límites para que no salten tanto
>    plt.show()
>```

# 3. Entrenamiento automático del perceptrón

Nuestro objetivo es modificar el código del perceptrón desarrollado en las fases anteriores para conseguir que aprenda automáticamente a clasificar los puntos, sin necesidad de modificar los pesos o el sesgo.

Hasta ahora hemos ajustado los parámetros `w1`, `w2` y `b` mediante prueba y error. Sin embargo, la principal característica del aprendizaje automático es que un algoritmo puede aprender estos parámetros a partir de ejemplos.

En nuestro caso, utilizaremos un algoritmo de **aprendizaje supervisado**, ya que conocemos de antemano la clase correcta a la que pertenece cada punto.

El procedimiento consiste en:

1. **Realizar una predicción:** el perceptrón recibe las coordenadas de un punto y determina a qué clase pertenece.
2. **Calcular el error:** se compara la predicción con la clase correcta.
3. **Actualizar los parámetros:** si el perceptrón se equivoca, se modifican los pesos y el sesgo para corregir su comportamiento.
4. **Repetir el proceso:** se continúa utilizando los ejemplos de entrenamiento para mejorar la clasificación.

De esta forma, el perceptrón puede aprender progresivamente una frontera de decisión que permita separar ambas clases.

## 3.1 La regla de aprendizaje del perceptrón

Recordemos que nuestro perceptrón recibe dos entradas, `x1` y `x2`, correspondientes a las coordenadas de un punto, y calcula una suma ponderada:
$$
z=w_1x_1+w_2x_2+b  
$$
A continuación, aplica una función de activación de tipo escalón para obtener una predicción:
$$
\hat{y}=  
\begin{cases}  
1 & \text{si }z\geq 0\\  
0 & \text{si }z<0  
\end{cases}  
$$
Donde ($\hat{y}$) representa la clase predicha por el perceptrón.

Durante el entrenamiento conocemos también la clase correcta, que representaremos mediante ($y$). Por tanto, podemos calcular el error de predicción:
$$
error=y-\hat{y}  
$$
Como estamos trabajando con un problema de clasificación binaria, el error únicamente puede tomar tres valores:

|Error|Significado|
|---|---|
|0|El perceptrón ha clasificado correctamente el punto.|
|1|El punto pertenece a la clase 1, pero el perceptrón ha predicho la clase 0.|
|-1|El punto pertenece a la clase 0, pero el perceptrón ha predicho la clase 1.|
Cuando el perceptrón comete un error, necesitamos modificar sus parámetros. Para ello, utilizaremos la **regla de aprendizaje del perceptrón**:
$$ 
w_1 \leftarrow w_1+\eta\cdot error\cdot x_1  
$$
$$
w_2 \leftarrow w_2+\eta\cdot error\cdot x_2  
$$
$$
b\leftarrow b+\eta\cdot error  
$$
La letra griega ($\eta$) (_eta_) representa la **tasa de aprendizaje**, un valor que controla la magnitud de las modificaciones realizadas sobre los parámetros.

>[!tip] Observa
>Cuando el error es cero, los parámetros no cambian. Por tanto, el perceptrón únicamente necesita corregir su comportamiento cuando realiza una clasificación incorrecta.

>[!example] Aprendiendo de los errores
>Antes de automatizar el entrenamiento completo, vamos a comprobar cómo funciona la regla de aprendizaje con un único punto.
>Supongamos que tenemos un perceptrón con los siguientes parámetros iniciales:
>- `w1 = 0`
>- `w2 = 0`
>- `b = 0`
>- Tasa de aprendizaje `η = 0.1`
>
>Y queremos clasificar el punto `(0.5, 1.2)`, que pertenece a la clase 0
>
>**Realiza las siguientes tareas:**
>1. Calcula manualmente el valor de `z` y determina la predicción inicial del perceptrón. 
>2. Calcula el error cometido, sabiendo que la clase correcta es 0.
>3. Aplica la regla de aprendizaje para obtener los nuevos valores de `w1`, `w2` y `b`.
>4. Comprueba los resultados utilizando Python.
>5. Vuelve a clasificar el mismo punto utilizando los nuevos parámetros. ¿Ha cambiado la predicción?
>
>**Reflexiona:** ¿Por qué hemos tenido que modificar los parámetros? ¿Qué ocurriría si el perceptrón hubiera clasificado correctamente el punto desde el principio?

## 3.2 Los hiperparámetros del entrenamiento

Antes de implementar el entrenamiento automático, debemos conocer algunos conceptos que nos permitirán configurar su funcionamiento.

En el aprendizaje automático es importante distinguir entre **parámetros** e **hiperparámetros**:
- **Parámetros:** son los valores internos del modelo que se modifican automáticamente durante el entrenamiento. En nuestro perceptrón son los pesos `w1`, `w2` y el sesgo `b`.
- **Hiperparámetros:** son valores que establecemos para configurar cómo se realiza el entrenamiento. No se ajustan mediante la regla de aprendizaje del perceptrón.

Vamos a conocer tres conceptos fundamentales.
### Épocas (_epochs_)

Una **época** es una pasada completa por todos los ejemplos que forman el conjunto de entrenamiento.

En nuestro ejercicio disponemos de 40 puntos: 20 pertenecientes a la clase 0 y otros 20 a la clase 1.

Por tanto, completar una época significa procesar los 40 puntos una vez.

Si establecemos un máximo de 100 épocas, el algoritmo podrá recorrer el conjunto de entrenamiento hasta 100 veces.

Sin embargo, no siempre será necesario completar todas las épocas. Si el perceptrón consigue clasificar correctamente todos los puntos, podemos detener el entrenamiento.

### Tasa de aprendizaje (_learning rate_)

La **tasa de aprendizaje** determina la magnitud de las correcciones realizadas sobre los parámetros cuando el perceptrón comete un error.

En nuestro algoritmo utilizaremos inicialmente:

`learning_rate = 0.1`

Este valor interviene directamente en la regla de actualización de los pesos y el sesgo.

### Tamaño del lote (_batch size_)

El **tamaño del lote** indica cuántos ejemplos se agrupan para calcular una actualización de los parámetros.

Podemos distinguir tres formas habituales de organizar el entrenamiento:

- **Entrenamiento en línea (**_**online**_**):** los ejemplos se procesan individualmente y se actualizan los parámetros después de cada uno cuando corresponde realizar una corrección.
- **Entrenamiento por mini-lotes (**_**mini-batch**_**):** los ejemplos se procesan en pequeños grupos y se calcula una actualización a partir de cada grupo.
- **Entrenamiento por lotes completos (**_**batch**_**):** se utiliza todo el conjunto de entrenamiento para calcular cada actualización.

En nuestro caso utilizaremos el **entrenamiento en línea**, característico del perceptrón clásico, en el que los parámetros pueden actualizarse después de cada ejemplo.

## 3.3. Implementación del entrenamiento automático en Python

Ahora que conocemos la regla de aprendizaje y los principales conceptos relacionados con el entrenamiento, vamos a modificar nuestro código para conseguir que el perceptrón aprenda automáticamente.

Para ello, seguiremos utilizando el cuaderno de Google Colab creado en el apartado anterior.

>[!question] A102.1(CE1) Implementación del algoritmo de entrenamiento
>Vamos a desarrollar un algoritmo que recorra todos los puntos, realice una predicción y actualice automáticamente los pesos y el sesgo cuando exista un error.
>
>Para ello, utilizaremos la función `f_activacion()` que implementamos anteriormente.
>Instrucciones:
>
>1. Inicializa los parámetros `w1`, `w2` y `b` a cero.  
>2. Establece una tasa de aprendizaje de `0.1` y un máximo de `1000` épocas.
>3. Utiliza un bucle para recorrer las épocas de entrenamiento.
>4. Dentro de cada época, utiliza otro bucle para recorrer los puntos del conjunto de entrenamiento mediante sus índices.
>5. Obtén las coordenadas del punto y su clase correcta a partir de los arrays `X` e `y`.
>6. Calcula la predicción de cada punto y compárala con su clase correcta.
>7. Implementa la regla de aprendizaje para actualizar los parámetros cuando se produzca un error.
>8. Contabiliza los errores cometidos durante cada época.
>9. Detén el entrenamiento cuando se complete una época sin errores.
>
>``` python
>
># Inicialización de los parámetros
>w1 = 0.0
>w2 = 0.0
>b = 0.0
>
># Hiperparámetros
>learning_rate = 0.1
>max_epocas = 1000
>
># Entrenamiento del perceptrón
>for epoca in range(max_epocas):
>
>    errores = 0
>
>    # Recorremos todos los puntos de entrenamiento
>    for i in range(len(X)):
>
>        # Obtenemos las coordenadas del punto
>        x1 = X[i, 0]
>        x2 = X[i, 1]
>
>        # Obtenemos la clase correcta
>        clase_correcta = y[i]
>
>        # TODO 1: Calcular la predicción
>        prediccion = ...
>
>        # TODO 2: Calcular el error
>        error = ...
>
>        # TODO 3: Actualizar los parámetros
>        # utilizando la regla de aprendizaje
>
>        # TODO 4: Contabilizar los errores
>        # cuando la clasificación sea incorrecta
>
>    print(f"Época {epoca + 1}: {errores} errores")
>
>    # TODO 5: Detener el entrenamiento
>    # cuando no se haya cometido ningún error
>
>```

