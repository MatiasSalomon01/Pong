import pygame

class ComoJugar:
    def __init__(self, ventana, fondo_final):
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)

        self.ventana = ventana

        pygame.display.set_caption("Cómo Jugar")

        self.font = pygame.font.SysFont('unispacebold', 32)
        self.font_options = pygame.font.SysFont('unispacebold', 17)

        self.foto1 = pygame.image.load("Images/flecha arriba.png").convert_alpha()
        self.foto2 = pygame.image.load("Images/flecha abajo.png").convert_alpha()

        self.flecha_arriba = pygame.transform.scale(self.foto1, (0, 0))
        self.flecha_abajo = pygame.transform.scale(self.foto2, (0, 0))

        self.fondo_final = fondo_final

    def loop(self, run_como_jugar):
        while run_como_jugar:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_como_jugar = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_como_jugar = False

            self.ventana.fill(self.negro)
            self.ventana.blit(self.fondo_final, (0, 0))
            self.draw()
            self.ventana.blit(self.foto1, (rec1.x-4.05, rec1.y-4.05))
            self.ventana.blit(self.foto2, (rec2.x-4.05, rec2.y-4.05))

            pygame.display.update()
    
    def draw(self):
        self.draw_options()

    def draw_options(self):
        global regla3, regla4, rec1, rec2
        self.draw_text('Reglas de Juego', self.blanco, self.ventana.get_width()//2, 50, self.font)
        self.draw_text('w: subir jugador 1 (paleta izquierda)', self.blanco, self.ventana.get_width()//2, 100, self.font_options)
        self.draw_text('s: bajar jugador 1 (paleta izquierda)', self.blanco, self.ventana.get_width()//2, 150, self.font_options)
        regla3 = self.draw_text(' : subir jugador 2 (paleta derecha)', self.blanco, self.ventana.get_width()//2, 200, self.font_options)
        regla4 = self.draw_text(' : bajar jugador 2 (paleta derecha)', self.blanco, self.ventana.get_width()//2, 250, self.font_options)

        rec1 = pygame.Rect(0, 0, self.foto1.get_width()-9.05, self.foto1.get_height()-9.05)
        rec1.x = regla3.x-15
        rec1.y = regla3.y
        pygame.draw.rect(self.ventana, self.blanco, rec1)

        rec2 = pygame.Rect(0, 0, self.foto2.get_width()-9.05, self.foto2.get_height()-9.05)
        rec2.x = regla4.x-15
        rec2.y = regla4.y
        pygame.draw.rect(self.ventana, self.blanco, rec2)

        self.draw_text('ESC: para ir atrás', self.blanco, self.ventana.get_width()//2, 300, self.font_options)

    def draw_text(self, text, color, x, y, font):
        text_surface = font.render(text, True, color, None)
        posicion = text_surface.get_rect()
        posicion.center = (x, y)
        self.ventana.blit(text_surface, posicion)
        return posicion