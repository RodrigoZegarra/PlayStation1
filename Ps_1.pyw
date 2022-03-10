import pygame, sys

#Inicializamos Pygame
pygame.init()

#Atributos de la pantalla ancho y alto
WIDTH = 1280
HEIGHT = 720

#Aqui declaramos la pantalla con su ancho alto y titulo
Window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Proyecto PS1')

#Aqui cargamos la imagen
logo_ps1=pygame.transform.scale(pygame.image.load(r'Proyecto_PS\logo_ps1.png'),(150,150))

#Creamos la funcion juego
def playing():
    cord_x=400
    cord_y=200
    speed_x=3
    speed_y=3
    #FPS
    clock = pygame.time.Clock()
    while True:
        #Este for lee los eventos de la pantalla 
        for event in pygame.event.get():
            print(event)
            #Si el evento es cerrar la ventana se cierra
            if event.type == pygame.QUIT:
                sys.exit()
        #Aqui definimos los limites de la pantalla para que la imagen no se salga de esta
        if cord_x > WIDTH-150 or cord_x < 0:
            speed_x *=-1
        if cord_y > HEIGHT-150 or cord_y<0:
            speed_y *=-1
        #Le sumamos la velocidad a la coordenada para que parezca una animacion
        cord_x+=speed_x
        cord_y+=speed_y
        #Color de fondo
        Window.fill("BLACK")
        #Aqui Mostramos el logo en pantalla
        Window.blit(logo_ps1,[cord_x,cord_y])
        #Actualizamos la ventana
        pygame.display.flip()
        #Definimos cuantos fps queremos para la velocidad del juego
        clock.tick(60)

playing()