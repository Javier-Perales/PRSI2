---
title: Sprint 1.5 Aplicación Sesgada
sda: "Misión 1: El nuevo paradigma computacional"
tags:
criterios_evaluacion:
entregable:
---
# 1. La teoría del sesgo

Hemos hablado de la importancia de los datos en la IA, ya que un modelo de IA aprende a partir de los datos de entrenamiento que se le proporcionan. Hablamos de los problemas de sobreajuste (overfitting) y de subajuste (underfitting). Recordemos:

- **Sobreajuste (overfitting)**: ocurre cuando un modelo aprende demasiado bien los datos de entrenamiento, incluyendo el ruido y las anomalías, lo que resulta en un rendimiento deficiente en datos nuevos.
- **Subajuste (underfitting)**: sucede cuando un modelo no captura adecuadamente los patrones en los datos de entrenamiento, lo que lleva a un rendimiento deficiente tanto en los datos de entrenamiento como en los nuevos.

Sin embargo, hay otro gran problema, la discriminación silenciosa que está incrustada en las montañas de datos con los que se entrenan la IA. Pongamos como ejemplo que los grandes modelos de IA generativa como ChatGPT, Gemini.., que han sido entrenados a partir de grandes vólumenes de datos procedentes de Internet. Estos modelos aprenden patrones lingüísticos y conceptuales cómo se combinan las palabras, qué significan las frases, y cómo se expresan las ideas.

Sin embargo, **no distinguen entre los correcto y lo incorrecto**. Si los datos de entrenamiento contienen **estereotipos, prejuicios o desigualdades sociales**, el modelo puede heredar y reproducir esos sesgos en sus respuestas.

Por ejemplo, si los textos de entrenamiento contiene como estereotipo de género, los hombres son programadores y las mujeres son enfermeras, el modelo puede generar respuestas que refuercen estos estereotipos, como asociar automáticamente ciertos roles o profesiones con un género específico.

## 1.1 Concepto del sesgo

La RAE define sesgado/da como relacionado con información 'tendenciosa' y ésta a su vez como "**que manifiesta parcialidad, obedeciendo a una tendencia o idea determinadas**".

En el contexto de la IA, existen diferentes definiciones de sesgo:
- La Organización Internacional de Normalización (**ISO**) define sesgo en la IA como "**el grado en que un valor de referencia se desvía de la verdad**".
- A su vez, en los estándares ISO/IEC 22989 se define a los sesgos como la "**diferencia sistemática de trato de determinados objetos, personas o grupos en comparación con otros**"

Cuando vemos un resultado inexacto puede ser que este se derive bien de un sesgo o bien de un error. **Los sesgos en Inteligencia Artificial no son simples errores aleatorios, sino que obedecen a patrones sistemáticos**.

Como dice el NIST: "**El sesgo es un efecto que priva a un resultado estadístico de representatividad al distorsionarlo, a diferencia de un error aleatorio, que puede distorsionarlo en cualquier ocasión, pero se equilibra en promedio**".

## 1.2 Los tres efectos del sesgo

Igual que no debemos de confundir los errores con los sesgos tampoco debemos de confundir los sesgos con la discriminación, que es una de las posibles consecuencias de los sesgos.

La desviación de la verdad que se produce en los sesgos puede contribuir a resultados diversos: **discriminatorios, ser neutra, o incluso puede ser positivo**.

- **Sesgo discriminatorio:** Ocurre cuando **la IA toma decisiones injustas basadas en estereotipos**. 
  Imagina una IA para contratar ingenieros que solo ha visto fotos de hombres en ese puesto durante los últimos 40 años. La IA "aprenderá" que para ser ingeniero hay que ser hombre. Si una mujer muy brillante se presenta, la IA podría rechazarla solo por su género.
- **Sesgo neutro:** Es una preferencia que no ayuda ni perjudica a ningún grupo de personas en especial; simplemente es una "manía" rara de la máquina.  
  Ejemplo: Una IA analiza currículums y nota que los empleados que mejor trabajan usan mucho la palabra "organigrama". La IA empieza a preferir a gente que usa esa palabra. No es que usar esa palabra te haga mejor trabajador, es solo una coincidencia que la IA ha detectado. No discrimina a nadie por su género o edad, es solo un estilo de escritura aleatorio.
  
  Este sesgo es neutro porque la probabilidad de usar la palabra "organigrama" no está sistemáticamente ligada a ningún grupo demográfico protegido (como género, etnia, edad, etc.). Simplemente refleja una cierta jerga o estilo de redacción de currículums que es aleatorio entre la población de candidatos.
  
- **Sesgo beneficioso:** A veces, tener una preferencia ayuda a encontrar lo mejor.
  Si entrenamos a la IA para que busque solo a personas que tengan muchísima experiencia y estudios específicos, la IA tendrá un "sesgo" hacia los más preparados. En este caso, el resultado es positivo porque nos ayuda a encontrar a los mejores candidatos para un trabajo difícil.
### 1.3 Exclusión

Un concepto relacionado con la discriminación, pero diferente es el de exclusión.

Un ejemplo de **sesgo discriminatorio y excluyente en una IA** es un sistema de selección de personal entrenado con datos históricos que penaliza los currículums que incluyen un vacío laboral por "permiso de maternidad".

Este sesgo es discriminatorio porque se dirige y perjudica injustamente a un grupo específico: las mujeres. Aunque un hombre puede tomar un permiso de paternidad, históricamente está más ligado a las mujeres. Al aprender de datos pasados donde las pausas en la carrera (especialmente por motivos familiares) eran vistas negativamente o eran menos comunes en los perfiles contratados (que históricamente eran hombres), la IA asocia el "permiso de maternidad" con un menor rendimiento o compromiso, penalizando a las candidatas por una razón directamente ligada a su género.

A la vez, es excluyente porque el resultado práctico de esta discriminación es que a un grupo de candidatas perfectamente cualificadas se les niega sistemáticamente la oportunidad de avanzar en el proceso de selección.

Por otro lado, un ejemplo de **sesgo discriminatorio pero no excluyente** sería un algoritmo de IA de publicidad de préstamos que muestra anuncios con tasas de interés más altas a usuarios que viven en códigos postales de bajos ingresos.

El sesgo es discriminatorio porque se dirige y perjudica a un grupo de personas basándose en un factor socioeconómico indirecto: su lugar de residencia. El algoritmo ha aprendido de los datos que ciertos códigos postales se correlacionan con un mayor riesgo crediticio o con una mayor probabilidad de aceptar condiciones menos favorables. Al mostrar sistemáticamente peores ofertas a este grupo, la IA perpetúa y amplifica una desventaja económica basada en la geografía, lo cual es una forma de discriminación.

Este sesgo no es excluyente porque no niega por completo el acceso al producto o servicio. Los residentes de estas áreas todavía ven los anuncios y tienen la oportunidad de solicitar el préstamo. No se les bloquea ni se les impide participar. Sin embargo, se les ofrece la oportunidad en condiciones peores que a otros grupos, lo que constituye una discriminación en la calidad del acceso, pero no en el acceso en sí mismo.

## 1.4 Equidad

Finalmente hay otro concepto diferente y relacionado que es la equidad o justicia.

En el contexto de la IA, la injusticia puede entenderse como el "trato diferencial injustificado que beneficia preferentemente a ciertos grupos sobre otros", "la equidad, por lo tanto, es la ausencia de tal trato diferencial injustificado o prejuicio hacia cualquier individuo o grupo".

La equidad no significa que deba de tratarse de forma distinta a diferentes personas o grupos pero que sí que es posible que deba de hacerse ese trato diferente para precisamente **conseguir corregir desequilibrios o una representación incorrecta que suponen una injusticia**.

![[recursos/IgualdadvsEquidad.png]]

Supongamos un sistema IA de asistente de aprendizaje adaptativo en una plataforma educativa.

En lugar de ofrecer el mismo contenido y los mismos ejercicios a todos por igual (lo que sería un enfoque de igualdad), el sistema de IA trabaja para alcanzar la equidad de la siguiente manera:

- Diagnóstico Inicial: La IA primero evalúa el nivel de competencia de cada estudiante con una serie de preguntas iniciales. Detecta que Ana domina la multiplicación, pero Pedro tiene dificultades con las tablas del 7 y del 8, mientras que Lucía comete errores cuando hay que llevar cifras en la suma.
- Personalización de Recursos (Aquí está la Equidad): Basándose en ese diagnóstico, el sistema no les da a todos la misma lección.

>[!task] El veredicto de la IA
>Para cada sistema de IA descrito, completa la tabla de análisis que se encuentra al final. 
>
>- **Caso 1: El Clasificador de CVs "Veterano"** 🧐 Una empresa tecnológica utiliza una IA para hacer una primera criba de currículums para un puesto de "Jefe de Innovación". La IA ha sido entrenada con los perfiles de los empleados que más tiempo llevan en la empresa (la mayoría hombres de entre 45 y 55 años). El sistema puntúa muy alto los CVs que mencionan tecnologías de hace 15 años (como "servidores Java EE") y descarta automáticamente a candidatos que mencionan exclusivamente tecnologías muy modernas (como "Rust" o "WebAssembly"), aunque sean más relevantes para el puesto.
>    
>- **Caso 2: El Asistente de Voz Inconsistente** Un nuevo altavoz inteligente a veces confunde la orden "Pon la alarma a las 7 de la mañana" con "Llama a mi mamá". Este fallo ocurre de manera impredecible, aproximadamente una vez cada doscientas peticiones, y no parece afectar más a un tipo de voz que a otro.
>    
>- **Caso 3: La Plataforma de Becas "Niveladora"** Una fundación utiliza una IA para asignar becas de estudio a estudiantes con alto potencial pero con recursos limitados. El sistema, además de analizar las notas, está programado para dar una puntuación extra a los candidatos que provienen de centros educativos en zonas rurales con bajo presupuesto, para compensar la falta de acceso a actividades extraescolares y cursos avanzados que sí tienen los estudiantes de zonas urbanas más ricas.
>    
>- **Caso 4: El Seguro de Coche Predictivo**  Una compañía de seguros utiliza una IA para calcular el precio de las pólizas de coche. El sistema ha sido entrenado con datos históricos de siniestralidad de la última década y ha detectado un patrón: los conductores varones de entre 18 y 25 años tienen, como grupo, una frecuencia de accidentes significativamente mayor. Basándose en esta correlación, la IA establece de forma automática una prima un 40% más cara para todos los solicitantes de este colectivo, sin tener en cuenta su historial de conducción individual o el tipo de vehículo.
>    
>- **Caso 5: El Recomendador de Noticias "Clickbait"**  Un portal de noticias utiliza una IA para personalizar la portada de cada usuario. El sistema aprende que los titulares que contienen palabras como "escándalo", "secreto" o "increíble" generan muchos más clics. Como resultado, la IA empieza a priorizar y mostrar de forma sistemática este tipo de noticias, sin importar su veracidad o relevancia, a todos los usuarios por igual, porque su único objetivo es maximizar la interacción.
>
|**Caso Nº**|**¿Sesgo o Error?**|**Justificación (¿Por qué es uno u otro?)**|**Si es un sesgo, ¿de qué tipo es?**  <br>_(Discriminatorio, Neutro, Positivo/Equidad)_|**Si es discriminatorio, ¿es excluyente?**  <br>_(Sí / No / No Aplica)_|**Justificación Final (Explica tus dos últimas respuestas)**|
|---|---|---|---|---|---|
|**1**||||||
|**2**||||||
|**3**||||||
|**4**||||||
|**5**||||||



## Sesión 2: Diseño del Modelo Sesgado