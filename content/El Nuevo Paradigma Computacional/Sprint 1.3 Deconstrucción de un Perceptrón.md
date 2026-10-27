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
