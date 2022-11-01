import pygame

class Creditos:
    def __init__(self, ventana, fondo_final):        
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)

        self.ventana = ventana

        pygame.display.set_caption("Créditos")

        self.font = pygame.font.SysFont('unispacebold', 32)
        self.font_options = pygame.font.SysFont('unispacebold', 25)

        self.fondo_final = fondo_final

    def loop(self, run_creditos):
        while run_creditos:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_creditos = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_creditos = False

            self.ventana.fill(self.negro) 
            self.ventana.blit(self.fondo_final, (0, 0))
            self.draw()
            pygame.display.update()

    def draw(self):
        self.draw_options()

    def draw_options(self):
        by = self.draw_text('Made By', self.blanco, self.ventana.get_width()//2, 100)
        name = self.draw_text('Matías Salomón', self.blanco, self.ventana.get_width()//2, 150)
        
    def draw_text(self, text, color, x, y):
        text_surface = self.font_options.render(text, True, color, None)
        posicion = text_surface.get_rect()
        posicion.center = (x, y)
        self.ventana.blit(text_surface, posicion)
        return posicion