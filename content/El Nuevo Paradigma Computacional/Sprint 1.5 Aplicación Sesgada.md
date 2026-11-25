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
- La Organización Internacional de Normalización (**ISO**) define sesgo en la IA como "**el grado en que un valor de referencia se desvía de la verdad**.
- A su vez, en los estándares ISO/IEC 22989 se define a los sesgos como la "**diferencia sistemática de trato de determinados objetos, personas o grupos en comparación con otros**"

Cuando vemos un resultado inexacto puede ser que este se derive bien de un sesgo o bien de un error. **Los sesgos en Inteligencia Artificial no son simples errores aleatorios, sino que obedecen a patrones sistemáticos**.

Como dice el NIST: "**El sesgo es un efecto que priva a un resultado estadístico de representatividad al distorsionarlo, a diferencia de un error aleatorio, que puede distorsionarlo en cualquier ocasión, pero se equilibra en promedio**".

## 1.2 Discriminación

Igual que no debemos de confundir los errores con los sesgos tampoco debemos de confundir los sesgos con la discriminación, que es una de las posibles consecuencias de los sesgos.

La desviación de la verdad que se produce en los sesgos puede contribuir a resultados diversos: **discriminatorios, ser neutra, o incluso puede ser beneficiosa**.

Como hemos expuesto antes, en el caso del sistema IA entrenado con estereotipos de género (por ejemplo, la búsqueda de un perfil que ha desempeñado históricamente mayormente un sexo) utilizará ese sesgo en la fase de inferencia y, por tanto, producirá **resultados discriminatorios hacia ese sexo** puesto que el hecho de que históricamente hayan desempeñado ese rol en un sexo no significa que lo vayan o deban desempeñar mejor en el futuro las personas de ese sexo.

Pero, si el sistema de IA se ha entrenado con perfiles muy cualificados, el resultado (desde esa óptica) puede ser positivo pues ofrece a los candidatos más capacitados. En este caso, el **sesgo es beneficioso (positivo)**

Un ejemplo de **sesgo neutro** sería una IA que muestra una preferencia por candidatos que han incluido la palabra "organigrama" en su currículum. Es un sesgo porque el sistema está dando un valor predictivo a una palabra específica que no necesariamente se correlaciona con el éxito en el puesto. La IA, al analizar los currículums de empleados actuales que tienen buen rendimiento, podría haber "aprendido" que muchos de ellos usaron esa palabra. Por lo tanto, asocia su presencia con un buen perfil.

Este sesgo es neutro porque la probabilidad de usar la palabra "organigrama" no está sistemáticamente ligada a ningún grupo demográfico protegido (como género, etnia, edad, etc.). Simplemente refleja una cierta jerga o estilo de redacción de currículums que es aleatorio entre la población de candidatos.

### 1.3 Exclusión

Un concepto relacionado con la discriminación, pero diferente es el de exclusión.

Un ejemplo de **sesgo discriminatorio y excluyente en una IA** es un sistema de selección de personal entrenado con datos históricos que penaliza los currículums que incluyen un vacío laboral por "permiso de maternidad".

Este sesgo es discriminatorio porque se dirige y perjudica injustamente a un grupo específico: las mujeres. Aunque un hombre puede tomar un permiso de paternidad, históricamente está más ligado a las mujeres. Al aprender de datos pasados donde las pausas en la carrera (especialmente por motivos familiares) eran vistas negativamente o eran menos comunes en los perfiles contratados (que históricamente eran hombres), la IA asocia el "permiso de maternidad" con un menor rendimiento o compromiso, penalizando a las candidatas por una razón directamente ligada a su género.

A la vez, es excluyente porque el resultado práctico de esta discriminación es que a un grupo de candidatas perfectamente cualificadas se les niega sistemáticamente la oportunidad de avanzar en el proceso de selección.

Por otro lado, un ejemplo de **sesgo discriminatorio pero no excluyente** sería un algoritmo de IA de publicidad de préstamos que muestra anuncios con tasas de interés más altas a usuarios que viven en códigos postales de bajos ingresos.

El sesgo es discriminatorio porque se dirige y perjudica a un grupo de personas basándose en un factor socioeconómico indirecto: su lugar de residencia. El algoritmo ha aprendido de los datos que ciertos códigos postales se correlacionan con un mayor riesgo crediticio o con una mayor probabilidad de aceptar condiciones menos favorables. Al mostrar sistemáticamente peores ofertas a este grupo, la IA perpetúa y amplifica una desventaja económica basada en la geografía, lo cual es una forma de discriminación.

Este sesgo no es excluyente porque no niega por completo el acceso al producto o servicio. Los residentes de estas áreas todavía ven los anuncios y tienen la oportunidad de solicitar el préstamo. No se les bloquea ni se les impide participar. Sin embargo, se les ofrece la oportunidad en condiciones peores que a otros grupos, lo que constituye una discriminación en la calidad del acceso, pero no en el acceso en sí mismo.

Por tanto, todos los errores no son sesgos y todos los sesgos no son negativos ni todos los sesgos negativos son discriminatorios, ni toda discriminación produce exclusión.