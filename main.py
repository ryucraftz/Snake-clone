from settings import *

class Main:
    def __init__(self):
        # GENERAL
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.update()

main = Main()
main.run()
