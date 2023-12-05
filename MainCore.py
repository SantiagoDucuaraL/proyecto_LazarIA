import RPi.GPIO as pin
import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import libcamera
import pygame
import subprocess
import colores

picam2 = Picamera2()#Inicializar camara

confi = picam2.create_preview_configuration() #Creacion de configuracion
confi["transform"] = libcamera.Transform(hflip=1, vflip=1)#Rotacion de 180 grados en imagen
picam2.configure(confi)#Aplicar configuracion
    

def playwav(wav):
    pygame.init()
    pygame.mixer.init()#Inicializar salida audio
    sound = pygame.mixer.Sound(wav)
    playing = sound.play()
    while playing.get_busy():
        pygame.time.delay(100)

def deteccion(comando):
    #Crear/borrar contenido del txt
    with open('/home/lazaria/Desktop/proyecto/repoyolov5/yolov5/runs/detect/exp/labels/Foto1.txt', 'w') as txtblank:
        pass
        
    #Comenzar operación de reconocimiento
    subprocess.run(comando, shell=True)
    
    #Obtener resultados que fueron escritos
    with open('/home/lazaria/Desktop/proyecto/repoyolov5/yolov5/runs/detect/exp/labels/Foto1.txt', 'r') as txtclases:
        lineas = txtclases.readlines()
        if lineas:
            for i in lineas:
                match i[0]:
                    case '1':
                        playwav('/home/lazaria/Descargas/Audio/100k.wav')
                    case '2':
                        playwav('/home/lazaria/Descargas/Audio/10k.wav')
                    case '3':
                        playwav('/home/lazaria/Descargas/Audio/20k.wav')
                    case '4':
                        playwav('/home/lazaria/Descargas/Audio/2k.wav')
                    case '5':
                        playwav('/home/lazaria/Descargas/Audio/50k.wav')
                    case '6':
                        playwav('/home/lazaria/Descargas/Audio/5k.wav')
                    case '7':
                        playwav('/home/lazaria/Descargas/Audio/poste.wav')
                    case '8':
                        playwav('/home/lazaria/Descargas/Audio/puerta.wav')
                    case '9':
                        playwav('/home/lazaria/Descargas/Audio/silla.wav')
                    
        else:
            print('txt vacío')

foldercap = '/home/lazaria/Desktop/proyecto/captures/'
foldervid = '/home/lazaria/Desktop/Reto3/videos/'
foldertex = '/home/lazaria/Desktop/Reto3/read/'


#Para trabajar con la numeración fisica de la tarjeta
pin.setmode(pin.BOARD)

def enbutton(board_number):
    pin.setup(board_number, pin.IN, pull_up_down = pin.PUD_DOWN)
    
enbutton(11)
enbutton(13)
enbutton(15)
enbutton(37) #boton para modo Cloud
modoCloud = False
pushArray = [False, False, False, False]
playwav('/home/lazaria/Desktop/Reto3/audiosr3/starting.wav')
playwav('/home/lazaria/Desktop/Reto3/audiosr3/liasaludo.wav')

while True:
    if pin.input(11) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        playwav('/home/lazaria/Descargas/Audio/modobilletes.wav')
        picam2.start(show_preview=False)
        time.sleep(3) #Timer de 3 segundos
        picam2.autofocus_cycle()
        picam2.capture_file(foldercap+"Foto1.jpg")
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacapture.wav')
        deteccion('python3 repoyolov5/yolov5/detect.py --source /home/lazaria/Desktop/proyecto/captures/Foto1.jpg --weights repoyolov5/yolov5/best1.pt --conf 0.35 --save-txt --exist-ok --class 1 2 3 4 5 6')
        print('guardado')
        pushArray[0] = True
    else:
        pushArray[0] = False
        
    if pin.input(13) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        playwav('/home/lazaria/Descargas/Audio/modoobstaculos.wav')
        picam2.start(show_preview=False)
        time.sleep(3) #Timer de 3 segundos
        picam2.autofocus_cycle()
        picam2.capture_file(foldercap+"Foto1.jpg")
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacapture.wav')
        deteccion('python3 repoyolov5/yolov5/detect.py --source /home/lazaria/Desktop/proyecto/captures/Foto1.jpg --weights repoyolov5/yolov5/best1.pt --conf 0.35 --save-txt --exist-ok --class 7 8 9')
        print('guardado')
        pushArray[1] = True
    else:
        pushArray[1] = False
        
    if pin.input(15) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        playwav('/home/lazaria/Descargas/Audio/modocolores.wav')
        picam2.start(show_preview=False)
        time.sleep(3) #Timer de 3 segundos
        picam2.autofocus_cycle()
        picam2.capture_file(foldercap+"Foto1.jpg")
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacapture.wav')
        for i in colores.decircolor():
            match i:
                case 'azul':
                    playwav('/home/lazaria/Descargas/Audio/azul.wav')
                case 'rojo':
                    playwav('/home/lazaria/Descargas/Audio/rojo.wav')
                case 'amarillo':
                    playwav('/home/lazaria/Descargas/Audio/amarillo.wav')
                case 'morado':
                    playwav('/home/lazaria/Descargas/Audio/morado.wav')
                case 'verde':
                    playwav('/home/lazaria/Descargas/Audio/verde.wav')
                case 'naranja':
                    playwav('/home/lazaria/Descargas/Audio/naranja.wav')
        print(colores.decircolor())
        pushArray[2] = True
    else:
        pushArray[2] = False
        
    if pin.input(37) == pin.HIGH:
        playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
        into = True
        pushArray[3] = True
        modoCloud = not modoCloud
        if modoCloud:
            playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacloudon.wav')
            print("Entraste en modo Cloud")
        while modoCloud:
            if pin.input(11) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                picam2.start(show_preview=False)
                time.sleep(3) #Timer de 3 segundos
                picam2.autofocus_cycle()
                picam2.capture_file(foldercap+"Foto1.jpg")
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacapture.wav')
                print('foto tomada')
                picam2.stop()
                pushArray[0] = True
            else:
                pushArray[0] = False
                
            if pin.input(13) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                print("inicio video")
                #picam2.start_and_record_video("test.mp4", duration=5)
                encoder = H264Encoder(10000000)
                output = FfmpegOutput(foldervid+'test.mp4')
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/liarecstart.wav')
                picam2.start_recording(encoder, output)
                time.sleep(5)#clip de 5 segundos
                picam2.stop_recording()
                picam2.stop_recording()
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/liarecstop.wav')
                print("fin de video")
                pushArray[1] = True
            else:
                pushArray[1] = False
                
            if pin.input(15) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                with open('/home/lazaria/Desktop/Reto3/gps/enableGPS.txt', 'w') as archivo:
                    archivo.write('1')
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/gps.wav') #TODO
                print('Coordenadas enviadas')
                picam2.stop()
                pushArray[2] = True
            else:
                pushArray[2] = False
            if pin.input(37) == pin.HIGH:
                playwav('/home/lazaria/Desktop/Reto3/audiosr3/press.wav')
                if into:
                    into = not into #para evitar que el click de acceso se cuente
                    
                else:
                    modoCloud = not modoCloud #Para salir de modo Cloud oprimir el boton Cloud 2 veces
                    print('Saliste de modo Cloud')
                    playwav('/home/lazaria/Desktop/Reto3/audiosr3/liacloudoff.wav')
                pushArray[3] = True
            else:
                pushArray[3] = False
                
            hubotrue = False
            for i in range(len(pushArray)):
                if pushArray[i]:
                    hubotrue = True
                    print('Cloud Push button'+str(i+1), end=' ')
            if hubotrue:
                print('')
            time.sleep(0.2)
                
    else:
        pushArray[3] = False
        
    hubotrue = False
    for i in range(len(pushArray)):
        if pushArray[i]:
            hubotrue = True
            print('Push button'+str(i+1), end=' ')
    if hubotrue:
        print('')
    time.sleep(0.15)
