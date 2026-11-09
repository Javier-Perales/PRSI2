---
title: "Sprint 1.4: IA Generativa. Del modelo al control del dato"
sda: "Misión 1: El nuevo paradigma computacional"
tags:
criterios_evaluacion:
entregable:
---
<!--
Bloque	Contenido	Actividad principal
4.1	Panorama actual de la IA generativa	Explorar los principales proveedores y sus modelos
4.2	Comparación y evaluación de modelos	Organizar una competición de IA con pruebas comunes
4.3	Personalización y herramientas	Crear un asistente especializado
4.4	Agentes de IA	Diseñar un flujo de trabajo que utilice herramientas y tome decisiones
4.5	IA abierta y modelos locales	Explorar Hugging Face y ejecutar un modelo local
4.6	Sesgos, huella digital y soberanía	Auditar un sistema de IA y elaborar recomendaciones
-->

# 1. Panorama actual de la IA generativa
## 1.1 IA vs IA Generativa

Hemos visto que la **Inteligencia Artificial** es un conjunto de técnicas que permiten desarrollar sistemas capaces de realizar tareas que normalmente relacionamos con capacidades humanas, como reconocer imágenes, comprender lenguaje, encontrar patrones, hacer predicciones o resolver problemas.

Una **IA generativa** es un sistema de inteligencia artificial capaz de **producir contenido nuevo** a partir de las instrucciones que recibe y de los patrones que ha aprendido durante su entrenamiento. Puede generar texto, imágenes, audio, vídeo o código informático.

>[!warning] Idea clave
>La IA generativa es una parte de la inteligencia artificial, no un sinónimo de toda la IA. Por ejemplo:
>- Un **filtro de correo no deseado** clasifica mensajes como spam o legítimos.
>- Un **recomendador de música** estima qué canciones pueden interesarnos.
>- Un **sistema de visión artificial** puede identificar objetos en una fotografía.
>- Una **IA generativa** puede redactar una historia, producir una imagen o escribir código nuevo a partir de una instrucción. 

Esto **no significa necesariamente que el sistema comprenda el mundo como una persona**, ni que todo lo que genere sea verdadero u original en el sentido legal o artístico. También puede repetir fragmentos aprendidos, cometer errores o generar contenido muy parecido al existente.

## 1.2 ¿Cómo funciona una IA Generativa?

La **IA generativa utiliza diferentes tipos de redes neuronales artificiales**, dependiendo del tipo de información que se quiere generar: texto, imágenes, audio, vídeo o incluso estructuras tridimensionales.

Vamos a centrarnos en la arquitectura de red neuronal de los grandes modelos de lenguaje (LLM).

Tenemos que distinguir entre dos momentos: **entrenamiento** y **uso o inferencia**.

### 1.2.1 Entrenamiento
Durante el entrenamiento, un modelo procesa grandes cantidades de datos y ajusta los parámetros de su red neuronal para identificar patrones y relaciones.

>[!tip] ¿Sabías que...? La IA ha leído una parte gigantesca de Internet
>Los grandes modelos de IA generativa, se entrenan utilizando enormes grandes cantidades de información procedente de páginas web, libros, artículos, código y otras fuentes.
>Para hacernos una idea:
>- [Common Crawl](https://www.commoncrawl.org/) uno de los grandes archivos públicos de Internet utilizados para entrenar modelos de IA, contiene más de **10 petabytes de información** y recopila miles de millones de páginas web.
>- **Llama 3 (Meta, 2024)** [Meta](https://ai.meta.com/blog/meta-llama-3) se entrenó con más de **15 billones de tokens**, pequeñas unidades de texto equivalentes aproximadamente a palabras o fragmentos de palabras.
>
> **Una precisión importante**: procesar un texto varias veces no significa necesariamente que el modelo lo memorice. Durante el entrenamiento ajusta millones o miles de millones de parámetros para aprender patrones y relaciones estadísticas.
> 
> **Lo sorprendente:** una IA puede aprender patrones lingüísticos y relaciones entre conceptos a partir de una cantidad de texto que ninguna persona podría leer a lo largo de su vida.

### 1.2.2 ¿Qué es un LLM?

Un **LLM** (_Large Language Model_, o **gran modelo de lenguaje**) es un modelo de IA entrenado con grandes cantidades de texto y, en muchos casos, también código, para procesar y generar lenguaje. Puede redactar, resumir, traducir, responder preguntas y ayudar a programar.

**No debemos confundir LLM con la aplicación** el LLM es el modelo; el chat que permite conversar con él  es una aplicación. Un mismo LLM puede utilizarse desde una web, una aplicación móvil o un programa informático.

Para procesar texto, un LLM lo divide primero en unidades denominadas **tokens** mediante un procedimiento llamado **tokenización**. Un token puede corresponder a una palabra, parte de una palabra, un número, un signo de puntuación o una secuencia de caracteres.

>[!info] 
>El tokenizador no es una red neuronal, sino un algoritmo que transforma texto en una secuencia de tokens y sus correspondientes identificadores numéricos (*token ID*)

**¿Por qué importan los tokens?**

- **Entrada:** la pregunta, las instrucciones y parte del historial utilizan tokens.
- **Salida:** la respuesta generada también utiliza tokens.
- **Límites:** los modelos tienen límites de contexto y de salida expresados habitualmente en tokens.
- **Coste:** cuando se utiliza una API, el consumo puede cobrarse según los tokens procesados y generados. En los servicios de suscripción, la facturación y los límites pueden ser diferentes.

**Por ejemplo**: pedir «resume este documento de 80 páginas» suele requerir más tokens de entrada que preguntar «¿qué es una variable?». Una respuesta de 3.000 palabras suele requerir más tokens de salida que una de 100 palabras.

>[!example] Experimenta: ¿Cuántos tokens tiene una frase?
>
>Accede a [MLHive Token Counter](https://www.mlhive.com/tools/token-counter) y selecciona el tokenizador `o200k_base`, utilizado por determinados modelos de OpenAI.
>
>1. Introduce la siguiente frase: `La inteligencia artificial está transformando nuestra sociedad.`
>2. Observa el número de palabras, caracteres y tokens.  
>3. Identifica alguna palabra que se haya dividido en varios tokens.
>4. Traduce la frase al inglés y repite el experimento.
>5. Prueba con una frase que contenga números, emojis y palabras con tildes.
>
>**Reflexiona:**
>
>- ¿Coincide el número de palabras con el de tokens?
>- ¿Una palabra siempre equivale a un token?
>- ¿Se obtiene el mismo número de tokens en español y en inglés?
>- ¿Por qué crees que los modelos de IA utilizan tokens en lugar de palabras completas?
>
>**Conclusión:** Los modelos de IA no procesan palabras completas, sino unidades denominadas _tokens_. Una palabra puede dividirse en varios tokens, y un token también puede representar una palabra completa, un signo de puntuación o una secuencia de caracteres.

#### Token ID

El tokenizador divide el texto en tokens y asigna a cada uno un identificador numérico.

![[recursos/tokenID.png]]

En el caso del gato duerme, la secuencia de números enteros que le modelo utilizará es:
`[125, 8472, 3916, 13]`

Cada tokenizador tiene un **vocabulario**, que es una tabla donde se relaciona cada token con su identificador.

>[!info]
>El token ID es simplemente una etiqueta numérica, no representa el significado. Para representar características propias de los token, el modelo utiliza los **embeddings**;  son vectores aprendidos durante el entrenamiento y utilizados como punto de partida para construir representaciones contextualizadas.

![[recursos/embeddings.png]]


#### Embeddings

Los Token ID son etiquetas arbitrarias. El número 8472 no contiene por sí mismo información sobre qué es un gato, qué características tiene o qué relación guarda con otros animales.

Necesitamos otra representación numérica: **los embeddings**.

Un embedding es una representación numérica de un elemento mediante un vector de números reales. ([¿Qué son los embeddings?](https://www.youtube.com/watch?v=h4GNDHC-s50))

En los LLM, los embeddings iniciales de los tokens son vectores cuyos **valores se aprenden durante el entrenamiento**.

Por ejemplo, imaginemos estas representaciones ficticias:
```
gato  = [0.9, 0.8, 0.1]
perro = [0.8, 0.9, 0.2]
coche = [0.1, 0.2, 0.9]
```
En este ejemplo, los vectores de «gato» y «perro» tienen significados distintos, pero aparecen en contexto lingüísticos similares, por eso sus representaciones pueden ser próximas.

![[recursos/embedding3D.png|350]]

>[!example] TensorFlow Embedding Projector
> [TensorFlow Embedding Projector](https://projector.tensorflow.org/) es una herramienta gratuita que permite visualizar embeddings como puntos en un espacio de dos o tres dimensiones y explorar las relaciones entre palabras.
> 1. Selecciona el conjunto de datos Word2Vec 10K, que contiene representaciones vectoriales de 10.000 palabras.
> 2. Busca una palabra en el panel de búsqueda, por ejemplo, `king`, `cat` o `computer`.
> 3. Observa qué palabras aparecen próximas a ella en el espacio vectorial.
> 4. Cambia entre proyecciones como PCA y t-SNE para observar cómo varía la distribución visual.
### 1.2.3 ¿Qué es la arquitectura Transformer?

**Transformer** es una arquitectura de redes neuronales presentada en **2017** que ha sido fundamental para el desarrollo de numerosos modelos de lenguaje actuales. No es una aplicación ni una empresa: es una forma de organizar los cálculos de un modelo.

Una de sus ideas centrales es el **mecanismo de atención** (_attention_). Permite que el modelo considere qué partes del texto son especialmente relevantes para interpretar otras partes.

Compara estas dos frases:

1. «Me **siento** en el **banco** del parque».
2. «Pido un **préstamo** al **banco**».

La palabra «banco» es la misma, pero las palabras «siento» y «prestamo» ayudan a interpretar su significado. Los Transformers calculan relaciones entre representaciones de tokens mediante mecanismos de atención. No siguen literalmente las reglas de un diccionario, sino que han aprendido patrones complejos durante su entrenamiento.

![[recursos/embedding_transformer.png]]

>[!warning] Podriamos decir que...
>la red transformer modifica el embedding para obtener una representación contextual, teniendo en cuenta el resto de tokens de la secuencia.
> 
>Esta es una de las razones por las que los Transformers pueden trabajar con palabras ambiguas.

#### 1.2.4 Esquema de entrenamiento de un LLM

![[recursos/entrenamientoLLM.png]]