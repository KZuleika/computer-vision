Crea tarjetas con operaciones matemáticas usando los operadores aritméticos de Pyton (Suma +, Resta -, Multiplicación *, división /, Modulo % y Potencia)


Haz al menos 10 tarjetas. El formato de las operaciones puede ser simple (4 + 7.5) o complejo (3+(4/5)**2).


Haz un programa que lea una tarjetas, usando una webcam y despliegue el resultado de la operación mostrada en ella. Se debe de segmentar la imagen, aplicar una transformación de perspectiva y extraer únicamente el pedazo de la imagen que contiene la operación a evaluar, para pasar solo esa parte de la imagen al algoritmo de OCR. El programa deberá analizar continuamente la imagen, para determinar si hay alguna tarjeta, y en caso de ser así, procesarla.

Puedes usar la instrucción eval() para evaluar la expresión.


Mide el tiempo que toma realizar el análisis OCR de la imagen en el programa, usando Tesseract y EasyOCR. (Puedes usar la función time.time())
En tu reporte, reporta cual fue el promedio de tiempo con cada biblioteca, así como cual de ellos cometió mas errores, en caso de haberlos cometido.


Prueba el algoritmo usando una tarjeta escrita a mano. Ve que el texto este alineado para no tener problemas (puedes imprimir una línea punteada degradada para escribir sobre ella). Reporta que tan bien puede reconocer Tesseract texto manuscrito. 