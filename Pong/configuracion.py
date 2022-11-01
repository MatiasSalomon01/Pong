import pygame

class Configuracion:
    def __init__(self, ventana, fondo_final):
        self.ventana = ventana
        self.fondo_final = fondo_final

        self.blanco = "#FFFFFF"
        self.negro = "#000000"

        pygame.display.set_caption("Configuración")

        self.font = pygame.font.SysFont('unispacebold', 32)
        self.font_options = pygame.font.SysFont('unispacebold', 25)

        self.dificultad = ""
        self.puntaje_total = 5

    def loop(self, run_configuracion):
        self.seleccionado = pygame.Rect(0, 0, 0, 0)
        while run_configuracion:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_configuracion = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run_configuracion = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mas.collidepoint(mouse_pos):
                        self.seleccionado.width = mas.width+2
                        self.seleccionado.height = mas.height+1
                        self.seleccionado.center = mas.center
                        self.puntaje_total += 1
                    if menos.collidepoint(mouse_pos):
                        self.seleccionado.width = menos.width+2
                        self.seleccionado.height = menos.height+1
                        self.seleccionado.center = menos.center
                        if self.puntaje_total > 1:
                            self.puntaje_total -= 1
                        else:
                            self.puntaje_total = 1
                    if facil.collidepoint(mouse_pos):
                        self.dificultad = "facil"
                        self.seleccionado.width = facil.width+15
                        self.seleccionado.height = facil.height+10
                        self.seleccionado.center = facil.center
                    if normal.collidepoint(mouse_pos):
                        self.dificultad = "normal"
                        self.seleccionado.width = normal.width+15
                        self.seleccionado.height = normal.height+10
                        self.seleccionado.center = normal.center
                    if dificil.collidepoint(mouse_pos):
                        self.dificultad = "dificil"
                        self.seleccionado.width = dificil.width+15
                        self.seleccionado.height = dificil.height+10
                        self.seleccionado.center = dificil.center
                    if aplicar.collidepoint(mouse_pos):
                        self.seleccionado.width = aplicar.width+15
                        self.seleccionado.height = aplicar.height+10
                        self.seleccionado.center = aplicar.center
                        self.aplicar(self.dificultad)

            self.ventana.blit(self.fondo_final, (0, 0))
            self.draw()

            pygame.draw.line(self.ventana, self.blanco, (0, 250), (self.ventana.get_width(), 250), 3)
            
            pygame.display.update()

    def draw(self):
        self.draw_options()

    def draw_options(self):
        global facil, normal, dificil, aplicar, total, mas, menos

        self.draw_text("Dificultad de la Pelota:", self.blanco, self.ventana.get_width()//2, 60)
        total = self.draw_text(f"Puntaje Total: {self.puntaje_total}", self.blanco, self.ventana.get_width()//2.8, 300)
        facil = self.draw_text("Facil", self.blanco, self.ventana.get_width()//2, 110)
        normal = self.draw_text("Normal", self.blanco, self.ventana.get_width()//2, 160)
        dificil = self.draw_text("Dificil", self.blanco, self.ventana.get_width()//2, 210)

        mas = self.draw_text("+", self.blanco, 315, 290)
        menos = self.draw_text("-", self.blanco, 315, 315)

        aplicar = self.draw_text("Aplicar", self.blanco, self.ventana.get_width()-70, 370)

        pygame.draw.rect(self.ventana, "#C0392B", self.seleccionado, 3)

    def draw_text(self, text, color, x, y):
        text_surface = self.font_options.render(text, True, color, None)
        posicion = text_surface.get_rect()
        posicion.center = (x, y)
        self.ventana.blit(text_surface, posicion)
        return posicion

    def aplicar(self, difficulty):
        url = f"Settings/dificultad.txt"
        archivo = open(url, "w")

        if difficulty == "facil":
            archivo.write(f"{5}\n")
            archivo.write(f"{4.5}\n")
            archivo.write(f"{3}\n")
            archivo.write(f"{self.puntaje_total}")
            archivo.close()
        elif difficulty == "normal":
            archivo.write(f"{7}\n")
            archivo.write(f"{6.5}\n")
            archivo.write(f"{4}\n")
            archivo.write(f"{self.puntaje_total}")
            archivo.close()
        elif difficulty == "dificil":
            archivo.write(f"{9}\n")
            archivo.write(f"{8.5}\n")
            archivo.write(f"{5}\n")
            archivo.write(f"{self.puntaje_total}")
            archivo.close()
        elif difficulty == "":
            archivo.write(f"{5}\n")
            archivo.write(f"{4.5}\n")
            archivo.write(f"{3}\n")
            archivo.write(f"{self.puntaje_total}")
            archivo.close()

        return url