<h1 align="center">Manual de usuario  </h1>

En esta sección se explicará cómo se usa el prototipo de LazarIA y con cuales funcionalidades cuenta el prototipo hasta el momento. 

<h3>Contenido </h3>

Aspectos físicos 
Instrucciones de uso 
Ejemplo de funcionamiento del prototipo
Aspectos técnicos de funcionamiento

<h3>Aspecto físico</h3> 

El prototipo consta de una tarjeta Raspi 4, una cámara pi 4, un módulo de de 4 botones con funcionalidades asignadas y  una batería de 2.2A para alimentar la Raspi 4.  La tarjeta Raspi 4 se encuentra protegida del exterior por una caja transparente de acrílico, la cámara pi 4 se encuentra conectada a la raspi por medio de un flex y el módulo de botones se encuentran conectados por medio de jumpers a los pines gpio de la Raspi 4.

<h3>Instrucciones de uso</h3>

Para iniciar el funcionamiento del prototipo el script maincore debe ser ejecutado manualmente si este se ejecuta correctamente el sistema reproducirá un audio de bienvenida, luego de ello mientras el sistema se encuentre energizado podrá usarse sin inconvenientes. El prototipo lazarIA cuenta con dos modos de funcionamiento: Modo cloud y el modo sin conexión.

![Gráfica de funcionamiento de los botones](https://raw.githubusercontent.com/SantiagoDucuaraL/proyecto_LazarIA/main/Captura.PNG)

<h5>Algunas aclaraciones TODAS las IMÁGENES y VIDEOS se sobreescriben cada vez que se toma una nueva imagen o video en cualquiera de los modos, esto para ahorrar memoria y por la seguridad de la información.</h5>

<h4>A. Modo cloud </h4>
Para activar el modo cloud se debe presionar una vez el boton amarillo del modulo de botenes. 

1. El botón que se encuentra justo debajo botón de activación del modo cloud al presionar realizará la adquisiciones de datos proporcionados por el módulo gps y por medio se calculará la posición y se enviará por medio de un bot en telegram como un google maps 
2. El siguiente botón permite tomar un video clip de 5 segundos que puede ser solicitado por medio del  bot de telegram al escribir la palabra video (cada nuevo video reescribe el anterior). 
3. El siguiente botón al presionarlo toma una una foto que será enviada a los servicios de azure para que retorne una descripción en audio de lo que se observe en la foto.
4. Para salir del modo cloud presione dos veces el boton amarillo del paso 1 de este modo se desactiva el modo cloud y entra en el modo sin conexion.

<h4>B. Modo Sin conexión </h4>
  
1. Asegúrese que se encuentra el modo cloud desactivado (revisar el paso 5 del modo cloud)
2. Al presionar el botón que se encuentra justo después del botón de activación del modo cloud activará el modo de detección de colores y después de un tiempo de 3 segundos la cámara tomará una foto, una vez el sistema procese la imagen se reproducirá un audio que dirá qué colores se encuentran en la imagen. El sistema está configurado para detectar alrededor de 30 por ciento de las tonalidades de los colores rojo, naranja, amarillo, verde, azul  y morado haciendo uso de la escala de color hsv.
3. El siguiente botón al presionarlo activará el modo de detección de obstáculos, después de tres segundos se tomará una foto para su posterior procesamiento. Los obstáculos que puede detectar el sistema son postes, puertas y sillas de parques. Cabe hacer la aclaración de que el sistema no avisa sobre la cercanía de estos objetos solo genera una salida de audio diciendo que obstáculos entre los ya mencionados se encuentran en la imagen tomada por la cámara. 
4. El siguiente botón al ser presionado activa el modo de detección de billetes, después de tres segundos tomará una foto la cámara para el posterior procesamiento de la imagen. Este modo detecta billetes colombianos de todas las denominaciones nuevas hasta la fecha de 2023 y genera una salida de audio donde avisa que denominación tiene cada billete que se detecte en la foto tomada. Para mayor seguridad del resultado se recomienda repetir el proceso por ambas caras del o de los billetes.

<h3>Ejemplo de funcionamiento</h3>

![Gráfica de funcionamiento de los botones](https://raw.githubusercontent.com/SantiagoDucuaraL/proyecto_LazarIA/main/Captura2.PNG)

![Gráfica de funcionamiento de los botones](https://raw.githubusercontent.com/SantiagoDucuaraL/proyecto_LazarIA/main/Captura3.PNG)

<h3>Aspectos Técnicos de funcionamiento</h3>

Para el funcionamiento de la detección de obstáculos y billetes se entrenó un modelo de predicción usando un dataset que contenia las imágenes de billetes de todas la denominaciones colombianas recientes e imágenes de postes, sillas de parques y puertas todas con sus respectivos labels y YoloV5 para entrenar el modelo. La matriz de confusión obtenida fue la siguiente:

 ![Gráfica de funcionamiento de los botones](https://raw.githubusercontent.com/SantiagoDucuaraL/proyecto_LazarIA/main/Captura4.PNG)

Para el modo de detección de colores se usó opencv y la escala de colores hsv.  El espacio de color HSV (Hue, Saturation, Value / Matiz, Saturación, Brillo), posee 3 componentes, similar al espacio de color RGB. Para determinar el color se usa H que va de 0 a 180 para determinar la saturación y brillo se usan valores de 0 a 255. Para el prototipo se escogio saturación y brillo constante de 100 para los colores rojo, naranja, amarillo, verde, azul y morado

 ![Gráfica de funcionamiento de los botones](https://raw.githubusercontent.com/SantiagoDucuaraL/proyecto_LazarIA/main/Captura5.PNG)

 Por defecto opencv lee las imágenes en BGR por ello se usa previamente la función cv2.cvtcolor con el argumento de cv2.COLOR_BGR2HSV para indicar que transformaremos de BGR a HSV. Una vez fijados los rangos de los colores en HVS se hace uso de la función cv2.inRANGE que se encargará de buscar los rangos en caso de que se detecte algún color. La detección de los colores puede variar dependiendo de la luz del entorno y de la calidad o fabricación de la cámara.

En maincore tenemos la asignación física de los pines de la raspi que serán usados y la configuración  de la cámara pi 4, además de cada uno de los modos tanto de cloud como de sin conexión descritos. Para el modo sin conexión en la identificación de billetes y colores se usa detect.py que viene con la instalacion de Yolov5 y se le agregan los parámetros de filtrado dependiendo el caso, si es para billetes se usan el filtrado de -class 1 2 3 4 6 para solo mostrar dichos resultados o -class 7 8 9 para la deteccion de obstaculos. Los resultados de la predicción del modelo se almacenan en un txt cuyo contenido se borra y se reescribe con cada nueva predicción, dependiendo de lo escrito en el txt por el modelo se activa un audio para dar la información de lo detectado. Solo se detecta aquello que tenga un grado de confianza de 35% o más si el modelo detecta algo por debajo de ese valor lo toma como que no detecto nada.


