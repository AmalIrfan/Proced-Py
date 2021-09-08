import pygame

# -- CONSTANTS --------------------------------------------

WIDTH = 600
HEIGHT = 600

FPS = 60

# -- CONTROLS ---------------------------------------------

win: pygame.Surface
clk: pygame.time.Clock

# -- COMPONENTS -------------------------------------------



def main():

    # -- INIT ---------------------------------------------

    pygame.init()

    global win, clk

    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clk = pygame.time.Clock()

    while True:

        # -- EVENT ----------------------------------------

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

        # -- UPDATE ---------------------------------------

        dt = clk.tick(FPS) * 0.001

        # -- DRAW -----------------------------------------

        win.fill("#080c00")

        pygame.display.flip()


if __name__ == "__main__":
    main()