# Dataproject

README – Proyecto de Análisis del Consumo de Alcohol en EE. UU. (1977–2023)
Este proyecto analiza la evolución del consumo de alcohol en Estados Unidos entre 1977 y 2023. Incluye un pipeline completo de limpieza de datos, un análisis estadístico en Python y un dashboard interactivo en Power BI para comparar el consumo de cerveza, vino y spirits a lo largo del tiempo.

📁 Estructura del proyecto
A continuación se describe la función de cada archivo incluido en el repositorio:
1. niaaa_apparent_per_capita_consumption_1977_2023.csv
Dataset original con los datos brutos de consumo per cápita de:
  -Cerveza
  -Vino
  -Spirits
  -Total estandarizado en “bebidas equivalentes”
Es el archivo de entrada del proyecto.

2. main.py
Script principal que implementa el pipeline de limpieza y validación del dataset.
Incluye:
  -Carga del archivo original
  -Inspección inicial (primeras filas, tipos, nulos)
  -Eliminación de duplicados
  -Estandarización de nombres de columnas
  -Validaciones de coherencia
  -Exportación del dataset limpio
Genera como salida el archivo clean_data.csv.

3. clean_data.csv
Dataset limpio y estandarizado generado automáticamente por main.py.
Es el archivo utilizado tanto para el análisis estadístico como para el dashboard de Power BI.

4. Analisis.py
Script que contiene todo el análisis estadístico del proyecto:

  -Regresión lineal temporal
  -ANOVA por décadas
  -Matriz de correlaciones
  -Intervalo de confianza
  -Gráficos generados con Matplotlib y Seaborn

Los resultados obtenidos se incluyen en el informe final.

5. Análisis.pbix
Archivo del dashboard de Power BI, donde se comparan las categorías:

  -Cerveza
  -Vino
  -Spirits

Se centra en estas tres categorías porque están en la misma unidad física y permiten comparaciones visuales coherentes.

6. Análisis del proyecto.pdf
Documento final del proyecto que explica con profundidad los datos del proyecto. 

🧩 Aclaración sobre el uso del “total” en el análisis
En el análisis estadístico se utiliza la columna total porque representa el consumo global convertido a bebidas estándar, una unidad común que permite estudiar tendencias generales y realizar modelos como regresiones o ANOVA.

Sin embargo, esta columna no es la suma directa de cerveza, vino y spirits. Cada tipo de bebida se convierte a “bebidas estándar” según su contenido de alcohol, por lo que el total está calculado de forma distinta y puede resultar confuso si se mezcla con las categorías individuales.

🧩 Por qué en Power BI no se incluye el total
En Power BI se comparan únicamente cerveza, vino y spirits porque están en unidades físicas equivalentes (número de cervezas, copas y chupitos).
El total está calculado con otra metodología (bebidas estándar), por lo que mezclarlo con las bebidas individuales generaría visualizaciones confusas.

Por eso:

En estadística sí se usa el total (para ver la tendencia global)

En Power BI no se usa (porque no es comparable con las bebidas individuales)

🔄 Flujo de trabajo del proyecto
Dataset original → niaaa_apparent_per_capita_consumption_1977_2023.csv

Limpieza y validación → main.py

Dataset limpio → clean_data.csv

Análisis estadístico → Analisis.py

Dashboard interactivo → Análisis.pbix

Informe final → Análisis del proyecto.pdf


