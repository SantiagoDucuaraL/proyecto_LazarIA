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



 
