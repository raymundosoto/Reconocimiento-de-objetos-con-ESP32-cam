import cv2 #Importar OpenCv
import urllib.request #Librería para para abrir y leer la URL del servidor web del ESP32 CAM
import numpy as np

#PROGRAMA DE CLASIFICACION DE OBJETOS PARA VIDEO EN DIRECCION IP 

url = 'http://192.168.100.142/capture'    #Aquí se debe insertar la IP que arroja el monitor serial del IDE de Arduino

winName = 'Cámara ESP32'
cv2.namedWindow(winName,cv2.WINDOW_AUTOSIZE)

# Configuración de la red neuronal 

classNames = []
classFile = 'coco.names'  #Archivo con los nombres de los objetos a reconocer
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'  #Archivos con los pesos de la red neuronal
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while(1):
    imgResponse = urllib.request.urlopen (url) #abrimos el URL con las imágenes tomadas del ESP32
    imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    img = cv2.imdecode (imgNp,-1) #decodificción de la imágenes

    #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # Descomentar esta línea si se quiere la imagen vertical
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Descomentar si se quieren lasm imáganes en escala de grises

    

    classIds, confs, bbox = net.detect(img,confThreshold=0.5)   #Clasificación de los objetos
    print(classIds,bbox)

    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness = 3) #mostramos en rectangulo lo que se encuentra
            cv2.putText(img, classNames[classId-1], (box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0),2)
            
            
    #Reescalamiento de la imagen
    scale_percent = 200 # porcentaje de la dimensiones de la imegn img
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

# Redimensionamiento de imagen para mostrarlas
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


    cv2.imshow(winName,img) # mostramos la imagen

    #esperamos a que se presione ESC para terminar el programa
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
cv2.destroyAllWindows()
