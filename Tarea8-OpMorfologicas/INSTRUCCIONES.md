# Operaciones Morfológicas

Investiga las funciones morfologicas incluidas en OpenCV (como se llaman, que parametros requieren, etc)

Haz un ejemplo de cada una de ellas.

## Investigación

Las transformaciones morfolóficas son operaciones simples que normalmente se aplican a imágenes binarias. Los operadores morfológicos más básicos son la erosión y la dilación. Para aplicar estas operaciones es necesario contar con dos elementos:
1.	Imagen original. La matriz que contiene a la imagen binarizada
2.	Elemento estructurante. La matriz que decide la naturaleza de la operación.
A partir de estas dos operaciones pueden derivarse la apertura, cierre, gradiente, top-hat, black-hat.
Para obtener el elemento estructurante podemos utilizar la función de OpenCV:
`cv.getStructuringElement(shape, ksize[, anchor])`

Que en sus parámetros recibe la forma del elemento estructural, puede ser una de las formas morfológicas descritas en la Ilustración 1, ksize es el tamaño del elemento estructurante y anchor es el ancho del elemento.


La función de OpenCV que realiza la operación de erosión es:
`cv2.erode(scr, kernel, iterations = 1)`

La función de OpenCV que realiza la operación de dilación es:
`cv2.dilate(scr, kernel, iterations = 1)`

Ambas funciones previas en sus parámetros reciben:
*	scr. La imagen original sobre la que se va a realizar la erosión. Parámetro obligatorio.
*	kernel. Es la matriz con la que se convoluciona la imagen.
*	iterations. Es el número de iteraciones a las que se somete a la erosión, es un parámetro opcional.
Para el caso de los operadores morfológicos restantes se utiliza la función genérica de OpenCV:
`cv2.morphologyEx (src, op, kernel)`
Que en sus parámetros recibe:
*	scr. La imagen original sobre la que se va a realizar la erosión. Parámetro obligatorio.
*	op. La operación por realizar.
*	kernel. Es la matriz con la que se convoluciona la imagen.

**Operación	Descripción	Código**
**Apertura**	Primero realiza la erosión y luego la dilación. Limpia los puntos blancos del exterior del objeto de interés.	`cv2.MORPH_OPEN`
**Cerradura**	Primero realiza la dilación y luego la erosión. Rellena los espacios negros en el interior del objeto de interés.	`cv2.MORPH_CLOSE`
**Gradiente morfológico**	Es la diferencia entre la aplicación de la dilación y la erosión en una imagen. El resultado es el contorno de un objeto.	`cv2.MORPH_ GRADIENT`
**Black-hat**	Es la diferencia ente la cerradura de la imagen y la imagen original.	`cv2.MORPH_BLACKHAT`
**Top-hat**	Es la diferencia ente la imagen original y la apertura de la imagen.	`cv2.MORPH_TOPHAT`

Primero cargamos las imágenes en escala de grises de la misma forma que se ha hecho en practicas anteriores. Se debe realizar la umbralización de cada una de las imágenes. Para eso se utiliza la función threshold de OpenCV:
`_, aux= cv2.threshold(imagenOriginal[i],130,255,cv2.THRESH_BINARY)`

La función require que en sus parámetros se indique la imagen a la que se le va a aplicar la umbralización, el punto corte, la escala, y el modo de umbralización binario con `cv2.THRESH_BINARY`.
