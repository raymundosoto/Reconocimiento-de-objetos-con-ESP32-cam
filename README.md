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

- Instalar Anaconda en linux [Guía de instalación de Anaconda](https://noviello.it/es/como-instalar-anaconda-en-ubuntu-22-04/)

En todas las instrucciones a continuación se considera que se conoce el manejo de la terminal de Linux por lo que las instrucciones se escribe directamente en la terminal. 

- Crear un carpeta con el nombre que se quiera para el proyecto
- Abrir una terminal en la carpeta y clonar el repositorio con todos los archivos

`git clone https://github.com/raymundosoto/Reconocimiento-de-objetos-con-ESP32-cam`

Con esta instrucción, todos los archivos se guardarán en la carpeta creada anteriormente.

- Se recomienda crear un ambiente virtual en Anaconda para trabajar el script de Python, esto evitará que nuestra instalación afecte otras instalaciones de Python, sin salir de la carpeta donde está abierta nuestra terminal de linux, se crea el ambiente virtual en la terminal con el siguiente comando

`conda create -n ESP32obj python==3.7.13`

Se creará un ambiente virtual con el nombre *ESP32obj* con la versión 3.7.13 de Python



# Instrucciones del programa _reconocimientoESP32.py_ para detectar los objetos

# Instrucciones de uso

# Resultados
 