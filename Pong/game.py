import pygame, random

class Pong:
    def __init__(self, ventana, width, height, fondo_final):
        self.ventana = ventana
        self.width = width
        self.height = height
        self.fondo_final = fondo_final

        self.archivo_colores = open("Settings/colores.txt", "r")
        self.lista_colores = self.return_colors(self.archivo_colores)
        self.archivo_colores.close()

        self.archivo_dificultad = open("Settings/dificultad.txt", "r")
        self.lista_dificultad = self.return_dificultad(self.archivo_dificultad)
        self.archivo_dificultad.close()

        self.negro = "#000000"
        self.blanco = "#FFFFFF"
        self.verde = (17, 191, 26)

        self.color_jugador1 = self.lista_colores[0][:-1]
        self.color_jugador2 = self.lista_colores[1][:-1]
        self.color_pelota = self.lista_colores[2][:-1]
        self.color_cancha = self.lista_colores[3]
        self.color_linea = self.blanco
        self.color_puntaje = self.blanco

        if self.color_cancha == self.blanco:
            self.color_linea = self.negro
            self.color_puntaje = self.negro

        self.fps_game = 60
        self.fps_clock_game = pygame.time.Clock()

        self.contador = 3
    
    def return_colors(self, archivo):
        lista_colores = []
        for linea in archivo:
            lista_colores.append(linea)
        return lista_colores

    def return_dificultad(self, archivo):
        lista_data = []
        for linea in archivo:
            lista_data.append(linea)
        return lista_data

    def loop(self, run_pong):
        self.jugador_width = 10
        self.jugador_height = 50

        #Jugadores
        self.x = 5
        self.x_jugador2 = self.width - self.jugador_width - self.x

        self.y_jugador1 = self.height//2 - self.jugador_height//2
        self.y_jugador2 = self.height//2 - self.jugador_height//2

        #self.velocidad_jugador = float(self.lista_dificultad[0][:-1]) 
        self.velocidad_jugador = int(self.lista_dificultad[0][:-1])

        #Pelota
        self.x_pelota = self.width//2
        self.y_pelota =  self.height//2
        self.pelota_width = 14
        self.pelota_height = 14
        
        for i in range(1):
            self.aleatorio = random.randrange(-1, 2, 2)
        
        self.speed_x = float(self.lista_dificultad[1][:-1]) 
        self.speed_y = int(self.lista_dificultad[2][:-1])

        self.velocidad_pelota_x = self.speed_x
        self.velocidad_pelota_y = self.speed_y
        
        global puntaje1
        global puntaje2
        self.puntaje1 = 0
        self.puntaje2 = 0

        self.puntaje_limite = int(self.lista_dificultad[3])

        while run_pong:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_pong = False

            self.tecla = pygame.key.get_pressed()
            if self.tecla[pygame.K_ESCAPE]:
                run_pong = False
            
            if self.tecla[pygame.K_RETURN]:
                self.x = 5
                self.x_jugador2 = self.width - self.jugador_width - self.x

                self.y_jugador1 = self.height//2 - self.jugador_height//2
                self.y_jugador2 = self.height//2 - self.jugador_height//2
                self.x_pelota = self.width//2
                self.y_pelota = self.height//2
                self.velocidad_pelota_x = random.choice((-self.speed_x,self.speed_x))
                self.velocidad_pelota_y = random.choice((-self.speed_y,self.speed_y))
                self.puntaje1 = 0
                self.puntaje2 = 0

                self.contador = 3
                
            if self.tecla[pygame.K_w] and self.y_jugador1 >= 0:
                self.y_jugador1 -=self.velocidad_jugador

            if self.tecla[pygame.K_s] and self.y_jugador1 + self.jugador_height <= self.height:
                self.y_jugador1 +=self.velocidad_jugador

            if self.tecla[pygame.K_UP] and self.y_jugador2 >= 0:
                self.y_jugador2 -=self.velocidad_jugador

            if self.tecla[pygame.K_DOWN] and self.y_jugador2 + self.jugador_height <= self.height:
                self.y_jugador2 +=self.velocidad_jugador

            if self.y_pelota <= 0:
                self.velocidad_pelota_y *= -1

            if self.y_pelota >= self.height:
                self.velocidad_pelota_y *= -1

            if self.x_pelota <= 0:
                self.x_pelota = self.width//2
                self.y_pelota = self.height//2
                self.velocidad_pelota_x *= -1
                self.velocidad_pelota_y = random.choice((-self.speed_y,self.speed_y))
                self.puntaje2 += 1

            if self.x_pelota >= self.width:
                self.x_pelota = self.width//2
                self.y_pelota = self.height//2
                self.velocidad_pelota_x *= -1
                self.velocidad_pelota_y = random.choice((-self.speed_y,self.speed_y))
                self.puntaje1 += 1

            self.jugador1 = pygame.Rect(self.x, self.y_jugador1, self.jugador_width, self.jugador_height)
            self.jugador2 = pygame.Rect(self.x_jugador2, self.y_jugador2, self.jugador_width, self.jugador_height)
            global pelota
            self.pelota = pygame.Rect(self.x_pelota - self.pelota_width//2, self.y_pelota - self.pelota_height//2, self.pelota_width, self.pelota_height)
            global text_obj
            self.text_obj = pygame.font.SysFont('unispacebold', 32)
            self.puntaje_jugador1 = self.text_obj.render(f"{self.puntaje1}", True, self.color_puntaje, None)
            self.puntaje_jugador2 = self.text_obj.render(f"{self.puntaje2}", True, self.color_puntaje, None)

            #Colision con jugadores
            if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self.jugador2):
                self.velocidad_pelota_x *= -1

            self.x_pelota += self.velocidad_pelota_x * self.aleatorio
            self.y_pelota -= self.velocidad_pelota_y

            self.ventana.fill(self.color_cancha)

            pygame.draw.rect(self.ventana, self.color_jugador1, self.jugador1)
            pygame.draw.rect(self.ventana, self.color_jugador2, self.jugador2)
            pygame.draw.ellipse(self.ventana, self.color_pelota, self.pelota)

            pygame.draw.line(self.ventana, self.color_linea, (self.width//2, 0), (self.width//2, self.height))

            self.ventana.blit(self.puntaje_jugador1, (self.width//4-self.puntaje_jugador1.get_width()//2, self.height-50))
            self.ventana.blit(self.puntaje_jugador2, (self.width//1.3-self.puntaje_jugador2.get_width()//2, self.height-50))
            
            if self.puntaje1 == self.puntaje_limite:
                self.ganador = self.text_obj.render(f"Jugador 1 ha ganado!", True, self.color_puntaje, self.color_cancha)
                self.reiniciar_obj = pygame.font.SysFont("unispacebold", 20)
                self.reiniciar = self.reiniciar_obj.render(f"Enter - para reiniciar", True, self.color_puntaje, self.color_cancha)
                self.salir = self.reiniciar_obj.render(f"Esc - para salir", True, self.color_puntaje, self.color_cancha)
                self.x_pelota = self.width//2
                self.y_pelota = self.height//2
                self.velocidad_pelota_x = 0
                self.velocidad_pelota_y = 0
                self.ventana.blit(self.ganador, (self.width//7.7, 20))
                self.ventana.blit(self.reiniciar, (self.width//4, 100))
                self.ventana.blit(self.salir, (self.width//3, 150))

            if self.puntaje2 == self.puntaje_limite:
                self.ganador = self.text_obj.render(f"Jugador 2 ha ganado!", True, self.color_puntaje, self.color_cancha)
                self.reiniciar_obj = pygame.font.SysFont("unispacebold", 20)
                self.reiniciar = self.reiniciar_obj.render(f"Enter - para reiniciar", True, self.color_puntaje, self.color_cancha)
                self.salir = self.reiniciar_obj.render(f"Esc - para salir", True, self.color_puntaje, self.color_cancha)
                self.x_pelota = self.width//2
                self.y_pelota = self.height//2
                self.velocidad_pelota_x = 0
                self.velocidad_pelota_y = 0
                self.ventana.blit(self.ganador, (self.width//7.7, 20))
                self.ventana.blit(self.reiniciar, (self.width//4, 100))
                self.ventana.blit(self.salir, (self.width//3, 150))

            if self.contador >= 0:
                pygame.time.wait(850)
                self.conteo_obj = pygame.font.SysFont('unispacebold', 50)
                self.conteo = self.conteo_obj.render(f"{self.contador}", True, self.color_puntaje, self.color_cancha)
                self.conteo_posicion = self.conteo.get_rect()
                self.conteo_posicion.center = (self.width//2, self.height//2-50)
                self.ventana.blit(self.conteo, self.conteo_posicion)
                self.x_pelota = self.width//2
                self.y_pelota = self.height//2

                self.contador-=1

            pygame.display.update()
            self.fps_clock_game.tick(self.fps_game)