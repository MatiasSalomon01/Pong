import pygame
from apariencia import Apariencia
from configuracion import Configuracion

class Opciones:
    def __init__(self, ventana, fondo_final):        
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)

        self.ventana = ventana

        pygame.display.set_caption("Opciones")

        self.font = pygame.font.SysFont('unispacebold', 32)
        self.font_options = pygame.font.SysFont('unispacebold', 25)

        self.fondo_final = fondo_final
        
    def loop(self, run_graficos):
        global posicion_x_cursor, posicion_y_cursor
        posicion_x_cursor = 85
        posicion_y_cursor = 100

        while run_graficos:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_graficos = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if apariencia.collidepoint(mouse_pos):
                        menu_apariencia = Apariencia(self.ventana, 500, 550, self.fondo_final)
                        menu_apariencia.loop(True)
                        self.ventana = pygame.display.set_mode((500, 400))
                        pygame.display.set_caption("Opciones")
                    if configuracion.collidepoint(mouse_pos):
                        menu_configuracion = Configuracion(self.ventana, self.fondo_final)
                        menu_configuracion.loop(True)
                        pygame.display.set_caption("Opciones")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_graficos = False
                    if event.key == pygame.K_RETURN:
                        if cursor.y == apariencia.y:
                            posicion_x_cursor = apariencia.x-15
                            posicion_y_cursor = apariencia.centery
                            menu_apariencia = Apariencia(self.ventana, 500, 550, self.fondo_final)
                            menu_apariencia.loop(True)
                            self.ventana = pygame.display.set_mode((500, 400))
                            pygame.display.set_caption("Opciones")

                        if cursor.y == configuracion.y:
                            posicion_x_cursor = configuracion.x-15
                            posicion_y_cursor = configuracion.centery
                            menu_configuracion = Configuracion(self.ventana, self.fondo_final)
                            menu_configuracion.loop(True)
                            pygame.display.set_caption("Opciones")

                    if event.key == pygame.K_DOWN:
                        posicion_x_cursor = configuracion.x-15
                        posicion_y_cursor = configuracion.centery
                    if event.key == pygame.K_UP:
                        posicion_x_cursor = apariencia.x-15
                        posicion_y_cursor = apariencia.centery

            self.ventana.blit(self.fondo_final, (0, 0))          

            self.draw()

            pygame.display.update()

    def draw(self):
        self.draw_options()

    def draw_options(self):
        global apariencia, configuracion, cursor
        apariencia = self.draw_text('Apariencia del Juego', self.blanco, self.ventana.get_width()//2, 100)
        configuracion = self.draw_text('Configuración del Juego', self.blanco, self.ventana.get_width()//2, 150)
        cursor = self.draw_text('>', self.blanco, posicion_x_cursor, posicion_y_cursor)

    def draw_text(self, text, color, x, y):
        text_surface = self.font_options.render(text, True, color, None)
        posicion = text_surface.get_rect()
        posicion.center = (x, y)
        self.ventana.blit(text_surface, posicion)
        return posicion