import pygame, sys
from opciones import Opciones
from creditos import Creditos 
from game import Pong
from como_jugar import ComoJugar

class Menu:
    def __init__(self, width, height):
        pygame.init()
        self.blanco = "#FFFFFF"
        self.negro = "#000000"

        self.fps = 60
        self.fps_clock = pygame.time.Clock()

        self.width = width
        self.height = height

        self.ventana = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong")

        self.font = pygame.font.SysFont('unispacebold', 32)
        self.font_options = pygame.font.SysFont('unispacebold', 25)

        self.fondo = pygame.image.load("Images\\fondo.jpg").convert_alpha()
        self.fondo_final = pygame.transform.scale(self.fondo, (self.width, self.height))

        self.icono = pygame.image.load("Images\\paddle.png").convert_alpha()
        pygame.display.set_icon(self.icono)

        self.save_colors("Settings/colores.txt")
        self.default_dificultad("Settings/dificultad.txt")
        
    def save_colors(self, url):
        archivo = open(f"{url}", "w")
        archivo.write(f"{self.blanco}\n")
        archivo.write(f"{self.blanco}\n")
        archivo.write(f"{self.blanco}\n")
        archivo.write(f"{self.negro}")
        archivo.close()

    def default_dificultad(self, url):
        archivo = open(f"{url}", "w")
        archivo.write(f"{5}\n")
        archivo.write(f"{4.5}\n")
        archivo.write(f"{3}\n")
        archivo.write(f"{5}\n")
        archivo.close()

    def loop(self, run):
        global posicion_x_cursor, posicion_y_cursor
        posicion_x_cursor = 200
        posicion_y_cursor = 150

        while run:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save_colors("Settings/colores.txt")
                    self.default_dificultad("Settings/dificultad.txt")
                    self.run = False
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if jugar.collidepoint(mouse_pos):
                        posicion_x_cursor = jugar.x-15
                        posicion_y_cursor = jugar.centery 
                        empezar = Pong(self.ventana, self.width, self.height, self.fondo_final)
                        empezar.loop(True)
                        pygame.display.set_caption("Pong")

                    if como_jugar.collidepoint(mouse_pos):
                        posicion_x_cursor = como_jugar.x-15
                        posicion_y_cursor = como_jugar.centery
                        reglas = ComoJugar(self.ventana, self.fondo_final)
                        reglas.loop(True)
                        pygame.display.set_caption("Pong")

                    if opciones.collidepoint(mouse_pos):
                        posicion_x_cursor = opciones.x-15
                        posicion_y_cursor = opciones.centery 
                        menu_opciones = Opciones(self.ventana, self.fondo_final)
                        menu_opciones.loop(True)
                        pygame.display.set_caption("Pong")

                    if creditos.collidepoint(mouse_pos):
                        posicion_x_cursor = creditos.x-15
                        posicion_y_cursor = creditos.centery 
                        menu_creditos = Creditos(self.ventana, self.fondo_final)
                        menu_creditos.loop(True)
                        pygame.display.set_caption("Pong")

                    if salir.collidepoint(mouse_pos):
                        posicion_x_cursor = salir.x-15
                        posicion_y_cursor = salir.centery 
                        self.save_colors("Settings/colores.txt")
                        self.default_dificultad("Settings/dificultad.txt")
                        self.run = False
                        pygame.quit()
                        sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if cursor.y == jugar.y:
                            empezar = Pong(self.ventana, self.width, self.height, self.fondo_final)
                            empezar.loop(True)
                            pygame.display.set_caption("Pong")

                        if cursor.y == como_jugar.y:
                            reglas = ComoJugar(self.ventana, self.fondo_final)
                            reglas.loop(True)
                            pygame.display.set_caption("Pong")

                        if cursor.y == opciones.y:
                            menu_opciones = Opciones(self.ventana, self.fondo_final)
                            menu_opciones.loop(True)
                            pygame.display.set_caption("Pong")

                        if cursor.y == creditos.y:
                            menu_creditos = Creditos(self.ventana, self.fondo_final)
                            menu_creditos.loop(True)
                            pygame.display.set_caption("Pong")
                            
                        if cursor.y == salir.y:
                            self.save_colors("Settings/colores.txt")
                            self.default_dificultad("Settings/dificultad.txt")
                            self.run = False
                            pygame.quit()
                            sys.exit()
                    
                    if event.key == pygame.K_ESCAPE:
                        self.save_colors("Settings/colores.txt")
                        self.default_dificultad("Settings/dificultad.txt")
                        self.run = False
                        pygame.quit()
                        sys.exit()

                    if event.key == pygame.K_DOWN:
                        if posicion_y_cursor == jugar.centery:
                            posicion_x_cursor = como_jugar.x-15
                            posicion_y_cursor = como_jugar.centery
                        elif posicion_y_cursor == como_jugar.centery:
                            posicion_x_cursor = opciones.x-15
                            posicion_y_cursor = opciones.centery                             
                        elif posicion_y_cursor == opciones.centery:
                            posicion_x_cursor = creditos.x-15
                            posicion_y_cursor = creditos.centery
                        elif posicion_y_cursor == creditos.centery:
                            posicion_x_cursor = salir.x-15
                            posicion_y_cursor = salir.centery
                        elif posicion_y_cursor == salir.centery:
                            posicion_x_cursor = jugar.x-15
                            posicion_y_cursor = jugar.centery
                    if event.key == pygame.K_UP:
                        if posicion_y_cursor == jugar.centery:
                            posicion_x_cursor = salir.x-15
                            posicion_y_cursor = salir.centery 
                        elif posicion_y_cursor == como_jugar.centery:
                            posicion_x_cursor = jugar.x-15
                            posicion_y_cursor = jugar.centery
                        elif posicion_y_cursor == opciones.centery:
                            posicion_x_cursor = como_jugar.x-15
                            posicion_y_cursor = como_jugar.centery
                        elif posicion_y_cursor == creditos.centery:
                            posicion_x_cursor = opciones.x-15
                            posicion_y_cursor = opciones.centery
                        elif posicion_y_cursor == salir.centery:
                            posicion_x_cursor = creditos.x-15
                            posicion_y_cursor = creditos.centery

            self.ventana.blit(self.fondo_final, (0, 0))

            self.draw()
            pygame.draw.line(self.ventana, self.blanco, (0, 100), (self.width, 100), 3)
            pygame.display.update()
            self.fps_clock.tick(self.fps)
            
    def draw(self):
        self.draw_header()
        self.draw_options()

    def draw_header(self):
        opciones = self.font.render('Menú del Juego', True, self.blanco, None)
        posicion = opciones.get_rect()
        posicion.center = (self.ventana.get_width()//2, 50)
        self.ventana.blit(opciones, posicion)

    def draw_options(self):
        global opciones, salir, creditos, jugar, cursor, como_jugar
        jugar = self.draw_text('Jugar', self.blanco, self.ventana.get_width()//2, 150)
        como_jugar = self.draw_text('Cómo Jugar', self.blanco, self.ventana.get_width()//2, 200)
        opciones = self.draw_text('Opciones', self.blanco, self.ventana.get_width()//2, 250)
        creditos = self.draw_text('Créditos', self.blanco, self.ventana.get_width()//2, 300)
        salir = self.draw_text('Salir', self.blanco, self.ventana.get_width()//2, 350)
        cursor = self.draw_text('>', self.blanco, posicion_x_cursor, posicion_y_cursor)

    def draw_text(self, text, color, x, y):
        text_surface = self.font_options.render(text, True, color, None)
        posicion = text_surface.get_rect()
        posicion.center = (x, y)
        self.ventana.blit(text_surface, posicion)
        return posicion
