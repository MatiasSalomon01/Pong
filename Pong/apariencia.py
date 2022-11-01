import pygame

class Apariencia:
    def __init__(self, ventana, width, height, fondo_final):        
        self.ventana = ventana
        self.width = width
        self.height = height
        self.fondo_final = pygame.transform.scale(fondo_final, (self.width, self.height))

        self.archivo = open("Settings/colores.txt", "r")
        self.lista_colores = self.return_colors(self.archivo)

    def return_colors(self, archivo):
        lista_colores = []
        for linea in archivo:
            lista_colores.append(linea)
        return lista_colores

    def loop(self, run_apariencia):
        self.blanco = "#FFFFFF"
        self.negro = "#000000"

        self.color_seleccionado = None

        self.ventana = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Apariencia del Juego")

        self.font = pygame.font.SysFont('unispacebold', 32)
        self.font_options = pygame.font.SysFont('unispacebold', 20)

        self.color1 = "#D52E2E" 
        self.color2 = "#68D52E" 
        self.color3 = "#E7EF3B" 
        self.color4 = "#47D6CC"
        self.color5 = "#A847D6"

        self.color_jugador1 = self.lista_colores[0][:-1]
        self.color_jugador2 = self.lista_colores[1][:-1]
        self.color_pelota = self.lista_colores[2][:-1]
        self.color_cancha = self.lista_colores[3]

        while run_apariencia:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_apariencia = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.save_colors("Settings/colores.txt")
                        run_apariencia = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.jugador1_opcion1.collidepoint(mouse_pos):
                        self.color_jugador1 = self.color1
                    if self.jugador1_opcion2.collidepoint(mouse_pos):
                        self.color_jugador1 = self.color2
                    if self.jugador1_opcion3.collidepoint(mouse_pos):
                        self.color_jugador1 = self.color3
                    if self.jugador1_opcion4.collidepoint(mouse_pos):
                        self.color_jugador1 = self.color4
                    if self.jugador1_opcion5.collidepoint(mouse_pos):
                        self.color_jugador1 = self.color5
                    if self.jugador1_opcion6.collidepoint(mouse_pos):
                        self.color_jugador1 = self.blanco
                    if self.jugador1_opcion7.collidepoint(mouse_pos):
                        self.color_jugador1 = self.negro

                    if self.jugador2_opcion1.collidepoint(mouse_pos):
                        self.color_jugador2 = self.color1
                    if self.jugador2_opcion2.collidepoint(mouse_pos):
                        self.color_jugador2 = self.color2
                    if self.jugador2_opcion3.collidepoint(mouse_pos):
                        self.color_jugador2 = self.color3
                    if self.jugador2_opcion4.collidepoint(mouse_pos):
                        self.color_jugador2 = self.color4
                    if self.jugador2_opcion5.collidepoint(mouse_pos):
                        self.color_jugador2 = self.color5
                    if self.jugador2_opcion6.collidepoint(mouse_pos):
                        self.color_jugador2 = self.blanco
                    if self.jugador2_opcion7.collidepoint(mouse_pos):
                        self.color_jugador2 = self.negro

                    if self.pelota_opcion1.collidepoint(mouse_pos):
                        self.color_pelota = self.color1
                    if self.pelota_opcion2.collidepoint(mouse_pos):
                        self.color_pelota = self.color2
                    if self.pelota_opcion3.collidepoint(mouse_pos):
                        self.color_pelota = self.color3
                    if self.pelota_opcion4.collidepoint(mouse_pos):
                        self.color_pelota = self.color4
                    if self.pelota_opcion5.collidepoint(mouse_pos):
                        self.color_pelota = self.color5
                    if self.pelota_opcion6.collidepoint(mouse_pos):
                        self.color_pelota = self.blanco
                    if self.pelota_opcion7.collidepoint(mouse_pos):
                        self.color_pelota = self.negro

                    if self.cancha_opcion1.collidepoint(mouse_pos):
                        self.color_cancha = self.color1
                    if self.cancha_opcion2.collidepoint(mouse_pos):
                        self.color_cancha = self.color2
                    if self.cancha_opcion3.collidepoint(mouse_pos):
                        self.color_cancha = self.color3
                    if self.cancha_opcion4.collidepoint(mouse_pos):
                        self.color_cancha = self.color4
                    if self.cancha_opcion5.collidepoint(mouse_pos):
                        self.color_cancha = self.color5
                    if self.cancha_opcion6.collidepoint(mouse_pos):
                        self.color_cancha = self.blanco
                    if self.cancha_opcion7.collidepoint(mouse_pos):
                        self.color_cancha = self.negro

            self.ventana.blit(self.fondo_final, (0, 0))
            self.draw()
            pygame.display.update()

    def draw(self):
        self.draw_options()

    def draw_options(self):

        self.draw_text('Personalización', self.blanco, self.ventana.get_width()//2, 50, self.font)
        self.jugador1 = self.draw_text('Color del Jugador 1: ', self.blanco, self.ventana.get_width()//3, 100, self.font_options)
        self.jugador2 = self.draw_text('Color del Jugador 2: ', self.blanco, self.ventana.get_width()//3, 220, self.font_options)
        self.pelota = self.draw_text('Color de la Pelota:  ', self.blanco, self.ventana.get_width()//3, 340, self.font_options)
        self.cancha = self.draw_text('Color de la Cancha:', self.blanco, self.ventana.get_width()//3.2, 460, self.font_options)
        self.cancha_texto = self.draw_text(self.color_cancha, self.blanco, self.cancha.centerx+160, 460, self.font_options)

        rec_jugador1 = self.draw_player(0, 0, self.color_jugador1, self.jugador1)

        self.jugador1_opcion1 = self.draw_colors_options(150, 150, self.color1)
        self.jugador1_opcion2 = self.draw_colors_options(180, 150, self.color2)
        self.jugador1_opcion3 = self.draw_colors_options(210, 150, self.color3)
        self.jugador1_opcion4 = self.draw_colors_options(240, 150, self.color4)
        self.jugador1_opcion5 = self.draw_colors_options(270, 150, self.color5)
        self.jugador1_opcion6 = self.draw_colors_options(300, 150, self.blanco)
        self.jugador1_opcion7 = self.draw_colors_options(330, 150, self.negro)

        rec_jugador2 = self.draw_player(0, 0, self.color_jugador2, self.jugador2)

        self.jugador2_opcion1 = self.draw_colors_options(150, 270, self.color1)
        self.jugador2_opcion2 = self.draw_colors_options(180, 270, self.color2)
        self.jugador2_opcion3 = self.draw_colors_options(210, 270, self.color3)
        self.jugador2_opcion4 = self.draw_colors_options(240, 270, self.color4)
        self.jugador2_opcion5 = self.draw_colors_options(270, 270, self.color5)
        self.jugador2_opcion6 = self.draw_colors_options(300, 270, self.blanco)
        self.jugador2_opcion7 = self.draw_colors_options(330, 270, self.negro)

        pelota = pygame.Rect(0, 0, 20, 20)
        pelota.center = (self.pelota.midright)
        pygame.draw.ellipse(self.ventana, self.color_pelota, pelota)        

        self.pelota_opcion1 = self.draw_colors_options(150, 390, self.color1)
        self.pelota_opcion2 = self.draw_colors_options(180, 390, self.color2)
        self.pelota_opcion3 = self.draw_colors_options(210, 390, self.color3)
        self.pelota_opcion4 = self.draw_colors_options(240, 390, self.color4)
        self.pelota_opcion5 = self.draw_colors_options(270, 390, self.color5)
        self.pelota_opcion6 = self.draw_colors_options(300, 390, self.blanco)
        self.pelota_opcion7 = self.draw_colors_options(330, 390, self.negro)

        self.cancha_opcion1 = self.draw_colors_options(150, 500, self.color1)
        self.cancha_opcion2 = self.draw_colors_options(180, 500, self.color2)
        self.cancha_opcion3 = self.draw_colors_options(210, 500, self.color3)
        self.cancha_opcion4 = self.draw_colors_options(240, 500, self.color4)
        self.cancha_opcion5 = self.draw_colors_options(270, 500, self.color5)
        self.cancha_opcion6 = self.draw_colors_options(300, 500, self.blanco)
        self.cancha_opcion7 = self.draw_colors_options(330, 500, self.negro)

    def draw_text(self, text, color, x, y, font):
        text_surface = font.render(text, True, color, None)
        posicion = text_surface.get_rect()
        posicion.center = (x, y)
        self.ventana.blit(text_surface, posicion)
        return posicion

    def draw_colors_options(self, x, y, color):
        rec = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(self.ventana, color, rec)
        return rec

    def draw_player(self, x, y, color, pos):
        rec = pygame.Rect(x, y, 10, 50)
        rec.midleft = pos.midright
        pygame.draw.rect(self.ventana, color, rec)
        return rec

    def save_colors(self, url):
        archivo = open(f"{url}", "w")
        archivo.write(f"{self.color_jugador1}\n")
        archivo.write(f"{self.color_jugador2}\n")
        archivo.write(f"{self.color_pelota}\n")
        archivo.write(f"{self.color_cancha}")
        archivo.close()