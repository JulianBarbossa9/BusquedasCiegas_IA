import pygame
from pygame.locals import QUIT
import time
import random
import sys


num_list = []
# 1 2 3
# 4 5 6
# 7 8 0 <--0;empty
# 3 * y + x + 1  
# (x= 1, y = 2) ==> 3 * 2 + 1 + 1 = 8
# (x = 2, y = 1) ==> 3 * 1 + 2 + 1 = 6
#Creo el arreglo de 3x3 con 0 que es el espacio que esta vacio
for x in range(3):
    l = []
    for y in range(3):
        l.append(3 * x + y + 1)
    num_list.append(l)
num_list[2][2] = 0

print(num_list)

#Tamaño de la ventana
pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()

def main():

    pieza_1 = pygame.image.load("./img/1.png")
    pieza_1 = pygame.transform.scale(pieza_1, (100, 100))
    pieza_2 = pygame.image.load("./img/2.png")
    pieza_2 = pygame.transform.scale(pieza_2, (100, 100))
    pieza_3 = pygame.image.load("./img/3.png")
    pieza_3 = pygame.transform.scale(pieza_3, (100, 100))
    pieza_4 = pygame.image.load("./img/4.png")
    pieza_4 = pygame.transform.scale(pieza_4, (100, 100))
    pieza_5 = pygame.image.load("./img/5.png")
    pieza_5 = pygame.transform.scale(pieza_5, (100, 100))
    pieza_6 = pygame.image.load("./img/6.png")
    pieza_6 = pygame.transform.scale(pieza_6, (100, 100))
    pieza_7 = pygame.image.load("./img/7.png")
    pieza_7 = pygame.transform.scale(pieza_7, (100, 100))
    pieza_8 = pygame.image.load("./img/8.png")
    pieza_8 = pygame.transform.scale(pieza_8, (100, 100))
    pieza_0 = pygame.image.load("./img/0.png")
    pieza_0 = pygame.transform.scale(pieza_0, (100, 100))

    piezas = [[pieza_1, pieza_2, pieza_3], 
              [pieza_4, pieza_5,pieza_6], 
              [pieza_7, pieza_8, pieza_0]]


    #Guardo la posicion de la ficha vacia 0
    ix = 0
    iy = 0 
    # Cambiar las piezas en un orden aleatorio
    # Estados posibles arriba, abajo, izquierda, derecha para la dirección
    tipo_mov = ['u', 'd', 'l', 'r']
    for _ in range(100):
        num = random.randint(0,3)
    
        # Moverse hacia arriba
        if tipo_mov[num] == 'u':
            for i in range(3):
                for j in range (3):
                    #Estoy encontrando la poscicion de 0 el espacio vacio
                    if num_list[i][j] == 0:
                        ix = i
                        iy = j
        
            if ix != 2:
                num_list[ix][iy] = num_list[ix + 1][iy]
                num_list[ix + 1][iy] = 0
                piezas[ix][iy] = piezas[ix + 1][iy]
                piezas[ix + 1][iy] = pieza_0

        # Moverse hacia abajo
        elif tipo_mov[num] == 'd':
            for i in range(3):
                for j in range (3):
                    #Estoy encontrando la poscicion de 0 el espacio vacio
                    if num_list[i][j] == 0:
                        ix = i
                        iy = j
        
            if ix != 0:
                num_list[ix][iy] = num_list[ix - 1][iy]
                num_list[ix - 1][iy] = 0
                piezas[ix][iy] = piezas[ix - 1][iy]
                piezas[ix - 1][iy] = pieza_0

        # Moverse hacia la izquierda
        elif tipo_mov[num] == 'l':
            for i in range(3):
                for j in range (3):
                    #Estoy encontrando la poscicion de 0 el espacio vacio
                    if num_list[i][j] == 0:
                        ix = i
                        iy = j
        
            if iy != 2:
                num_list[ix][iy] = num_list[ix][iy + 1]
                num_list[ix][iy + 1] = 0
                piezas[ix][iy] = piezas[ix][iy + 1]
                piezas[ix][iy + 1] = pieza_0

        # Moverse hacia la derecha
        elif tipo_mov[num] == 'r':
            for i in range(3):
                for j in range (3):
                    #Estoy encontrando la poscicion de 0 el espacio vacio
                    if num_list[i][j] == 0:
                        ix = i
                        iy = j
        
            if iy != 0:
                num_list[ix][iy] = num_list[ix][iy - 1]
                num_list[ix][iy - 1] = 0
                piezas[ix][iy] = piezas[ix][iy - 1]
                piezas[ix][iy - 1] = pieza_0


    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # elif event.type == pygame.KEYDOWN:

            #     if event.key == pygame.K_RIGHT:
            #         for i in range(3):
            #             for j in range (3):
            #                 if num_list[i][j] == 0:
            #                     ix = i
            #                     iy = j
            #         if iy != 0:
            #             num_list[ix][iy] = num_list[ix][iy - 1]
            #             num_list[ix][iy - 1] = 0
            #             piezas[ix][iy] = piezas[ix][iy - 1]
            #             piezas[ix][iy - 1] = pieza_0

            #     elif event.key == pygame.K_LEFT:
            #         for i in range(3):
            #             for j in range (3):
            #                 if num_list[i][j] == 0:
            #                     ix = i
            #                     iy = j
            #         if iy != 2:
            #             num_list[ix][iy] = num_list[ix][iy + 1]
            #             num_list[ix][iy + 1] = 0
            #             piezas[ix][iy] = piezas[ix][iy + 1]
            #             piezas[ix][iy + 1] = pieza_0
                    
            #     elif event.key == pygame.K_UP:
            #         for i in range(3):
            #             for j in range (3):
            #                 if num_list[i][j] == 0:
            #                     ix = i
            #                     iy = j
            #         if ix != 2:
            #             num_list[ix][iy] = num_list[ix + 1][iy]
            #             num_list[ix + 1][iy] = 0
            #             piezas[ix][iy] = piezas[ix + 1][iy]
            #             piezas[ix + 1][iy] = pieza_0

            #     elif event.key == pygame.K_DOWN:
            #         for i in range(3):
            #             for j in range (3):
            #                 if num_list[i][j] == 0:
            #                     ix = i
            #                     iy = j
            #         if ix != 0:
            #             num_list[ix][iy] = num_list[ix - 1][iy]
            #             num_list[ix - 1][iy] = 0
            #             piezas[ix][iy] = piezas[ix - 1][iy]
            #             piezas[ix - 1][iy] = pieza_0

        SURFACE.fill((255, 255, 255))
        for i in range(3):
            for j in range(3):
                SURFACE.blit(piezas[i][j], (j *100, i * 100))

        pygame.display.update()


if __name__ == "__main__":
    main()



