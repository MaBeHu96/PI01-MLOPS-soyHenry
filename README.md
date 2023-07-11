# PI01-MLOPS-soyHenry
INTRODUCCIÓN
Quiero contarles como fue mi experiencia como Data Scientist en una startup de servicios de agregación de plataformas de streaming. El proyecto principal se centró en mejorar la comprensión y el uso de los datos relacionados con las películas transmitidas en la plataforma.

comencé el proyecto recibiendo dos archivos CSV que contenían información detallada sobre las películas. El objetivo era utilizar técnicas avanzadas de análisis de datos y aprendizaje automático para extraer patrones, tendencias y conocimientos relevantes y así, generar recomendaciones personalizadas para los usuarios.

El primer paso fue explorar exhaustivamente el conjunto de datos utilizando tecnicas de ETL, identificar las variables clave y realizar una limpieza y organización de los datos para garantizar su calidad y coherencia. También se llevó a cabo una transformación y codificación adecuada de las características relevantes para preparar los datos para un análisis posterior.

A continuación, se realizó un análisis descriptivo para obtener una visión general de las características de las películas en la plataforma. Esto implicó el uso de visualizaciones y correlaciones relevantes para obtener información detallada sobre los géneros más populares, las palabras que más se ven reflejadas en los títulos y otras características importantes para el negocio.

Para proporcionar recomendaciones personalizadas a los usuarios, implemente un modelo de recomendación basado en contenido proporcionado. Este modelo utilizó técnicas avanzadas de aprendizaje automático, buscando procesar  información clave sobre las películas, como el título, con el fin de encontrar películas similares y ofrecer recomendaciones personalizadas a cada usuario en función de sus preferencias individuales.

FLUJO DE TRABAJO
El trabajo se realizó bajo los siguientes pasos:
-	El preprocesamiento de datos es una etapa crítica en la que se realiza una limpieza y transformación de los datos para garantizar su calidad y adecuación al modelo. Esto implica eliminar valores faltantes, normalizar datos y codificar variables categóricas.

-	El análisis exploratorio de datos (EDA) es otra etapa importante en la que se investiga y comprende la información en bruto mediante técnicas estadísticas y visuales. Se describe y visualiza la distribución de variables, se exploran relaciones por medio de matrices de correlacion.

-	Después del EDA, se crea una matriz de características que representa cada película con vectores numéricos que capturan información clave como título, género y directores.

-	Luego, se calcula la similitud entre las películas utilizando la medida de similitud del coseno en los vectores de características. Esto permite identificar las películas similares más a una película dada.

-	Finalmente, se seleccionarán las 5 películas más similares basadas en su similitud y se presentarán como recomendaciones al usuario.

En resumen, el proceso implica preprocesamiento de datos, análisis exploratorio, creación de matrices de características, cálculo de similitudes y recomendación de películas similares.

OBJETIVOS DEL TRABAJO
El proyecto tiene como objetivo principal realizar consultas específicas a los datos para obtener información relevante sobre las películas transmitidas en la plataforma de agregación de streaming. Se busca identificar patrones, tendencias y características clave mediante consultas específicas que proporcionen una comprensión profunda del contenido disponible.

Además, se busca desarrollar un modelo de descripción de películas basado en contenido que pueda ofrecer una lista de 5 películas similares al ingresar un título. Este modelo utilizará técnicas de aprendizaje automático para procesar la información clave, como el título de las películas, y generará recomendaciones personalizadas basadas en las características compartidas entre las películas.

Para asegurar la accesibilidad y la integración de estas funcionalidades, se desarrollará una API que expondrá las consultas específicas a los datos y el modelo de recomendaciones de películas. Esta API estará diseñada para ser intuitiva, documentada adecuadamente logrando así cumplir con las mejores prácticas de seguridad, permitiendo a otros a ser uso de ella. 

CONSULTAS QUE BASE EL PROYECTO 
El proyecto se enfocá en las siguientes 6 funciones, que para el usuario ésta relacionadas como consultas que puede realizar y obtendrá un resultado coherente con su pregunta; estas son:

-	Películas_idioma: a lo cual el usuario pregunta un idioma y la respuesta que obtendrá son la cantidad de películas que se pueden encontrar en ese idioma.

-	Películas_duración: si el usuario pregunta el título de una película, encontrara como respuesta el tiempo de duración en minutos y el año en el que fue estrenado.

-	Franquicias: aquí al usuario introducir el nombre de una franquicia, la respuesta que recibirá será la cantidad de películas que esta ha producido, además de un número que define la cantidad de ganancias y otro que identifica el promedio de ganancias de esta franquicia. 

-	Películas_país: al poner el nombre de un país en la respuesta encontrará la cantidad de películas producidas por dicho país.

-	Productoras_exitosas: al poner el nombre de una productora, recibirá el número de películas producidas y los ingresos generados. 

-	Get_director: al poner el nombre de un director, la respuesta que obtendrá es un listado de las películas realizadas por él.

MODELO DE RECOMENDACIONES
En este espacio realizamos La recomendación basada en el contenido proporcionado y realizando un símil de las películas, para luego de a ver obtenido la información proporcionada por el usuario, generar una lista de las 5 películas más similares al título de la película ingresada por el usuario. Estas recomendaciones se basan en las características compartidas entre las películas y ayudan a los usuarios a descubrir y explorar películas que se ajustan a sus preferencias individuales.

CONCLUSIONES

-	El análisis de datos proporcionó información detallada sobre las películas disponibles en la plataforma de streaming, revelando patrones y tendencias clave, lo que permitió una comprensión profunda del contenido.

-	El modelo de recomendación de películas basado en técnicas de aprendizaje automático cumplió con éxito el objetivo de ofrecer recomendaciones personalizadas, mejorando la experiencia del usuario al adaptarse a sus gustos y preferencias.

-	Se desarrolló una API intuitiva, bien documentada y segura que facilita la integración de las funcionalidades del proyecto en otros sistemas y aplicaciones.

-	En general, se logró una personalización efectiva en la experiencia del usuario, brindando recomendaciones acordes a sus preferencias y necesidades.

-	El proyecto aportó valor y mejoró la experiencia del usuario, y se destaca la importancia de continuar trabajando para ofrecer un servicio aún mejor en el futuro.
![image](https://github.com/MaBeHu96/PI01-MLOPS-soyHenry/assets/114516506/3141595a-2ec4-4d51-89ef-01ca978f9328)

