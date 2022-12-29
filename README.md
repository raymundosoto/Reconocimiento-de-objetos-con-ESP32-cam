# Reconocimiento de objetos con ESP32CAM
 Este repositorio contiene la descripción del proyecto y archivos necesarios para reconocer objetos usando redes neuronales con el ESP32 CAM.


# Material necesario

- Un microcontrolador ESP32CAM con cámara OV2640
- Un cable USB a microUSB (se conectará el controlador a un puerto USB de la computadora)

# Software necesario 

Este proyecto se corrió en Linux en una máquina virtual con Ubuntu 22.04 pero se pueden seguir los mismos pasos en windows con las consideraciones necesarias para tener un ambiente de desarrollo adecuado.

- IDE de Arduino 1.8.19 para programar el ESP32CAM
- Anaconda para linux 
- Python 3.7.13
- Editor de código para Python de su preferencia (Visual estudio code, Sublime text, etc.)
- Todos los programas del repositorio 

# Instalación del proyecto

- Instalar IDE de Arduino [Guía de instalación](https://ubunlog.com/arduino-ide-entorno-desarrollo-para-trabajar-con-arduino/?utm_source=dlvr.it&utm_medium=twitter)

- Confugurar el IDE de Arduino para programar el ESP32CAM [Guía de configuración](https://randomnerdtutorials.com/program-upload-code-esp32-cam/)

- Instalar Anaconda en linux [Guía de instalación de Anaconda](https://noviello.it/es/como-instalar-anaconda-en-ubuntu-22-04/)

En todas las instrucciones a continuación se considera que se conoce el manejo de la terminal de Linux por lo que las instrucciones se escribe directamente en la terminal. 

- Crear un carpeta con el nombre que se quiera para el proyecto
- Abrir una terminal en la carpeta y clonar el repositorio con todos los archivos

`git clone https://github.com/raymundosoto/Reconocimiento-de-objetos-con-ESP32-cam`

Con esta instrucción, todos los archivos se guardarán en la carpeta creada anteriormente.

- Se recomienda crear un ambiente virtual en Anaconda para trabajar el script de Python, esto evitará que nuestra instalación afecte otras instalaciones de Python, sin salir de la carpeta donde está abierta nuestra terminal de linux, se crea el ambiente virtual en la terminal con el siguiente comando

`conda create -n ESP32obj python==3.7.13`

Se creará un ambiente virtual con el nombre *ESP32obj* con la versión 3.7.13 de Python

- Activamos el ambiente virtual para configurarlo con las bibliotecas que necesitamos

`conda activate ESP32obj`

- Instalamos las bibliotecas listadas en el archivo **requeriments.txt**

`pip install requeriments.txt`

Con esto ya podemos correr el script de python pero antes de correrlo debemos programar el ESP32 CAM para capturar las imágenes


# Instrucciones de programación del ESP32 CAM como servidor web

- Abrir el archivo _CameraWebServer.ino_ de la carpeta CameraWebServer con el IDE de Arduino
- Conectar el ESP32CAM a la computadora con el cable USB
- Subir al ESP32CAM el archivo _CameraWebServer.ino_
- Una vez subido el programa al ESP32 CAM revisar el monitor serial para leer la dirección IP que nos ayudará a obtener las imágenes, el monitor serie se verá algo así una vez conectado al WiFi

~~~
WiFi connected
Camera Ready! Use 'http://192.168.100.xxx' to connect
~~~

Copiar la dirección IP y pegarla en el script de Python en la siguiente línea

~~~
url = 'http://192.168.100.xxx/capture'    #Aquí se debe insertar la IP que arroja el monitor serial del IDE de Arduino
~~~

- Guardar el archivo .py y correrlo desde la terminal que está abierta en la carpeta de nuestro proyecto y donde se ejecuta nuestro ambiente virtual

`python reconocimientoESP32.py`

Si todo se realizó correctamente debería observar una ventana donde se transmiten las imágenes y los objetos reconocidos dentro de ellas

## Notas del uso del script

Si requiere que la ventana de salida con las imágenes sea más grande modifica la siguiente línea del script de python

~~~
#Reescalamiento de la imagen
    scale_percent = 200 # porcentaje de la dimensiones de la imagen img
~~~

scale_percent puede tener valores arriba de 100, incluso menores de 100 pero esto provocaría que la imagen de salida sea más pequeña.


# Resultados
 