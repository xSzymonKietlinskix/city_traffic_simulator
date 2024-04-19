import pygame
import time
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH = 1920

def show_city(city, start, end, current, screen, cell_size, droga_img, blokada_img, car_img, meta_img, start_img, L):
    screen.fill(BLACK)


    for i in range(L):
        for j in range(L):
            if start[0] == i and start[1] == j:
                screen.blit(start_img, (i * cell_size, j * cell_size))
            elif current[0] == i and current[1] == j:
                screen.blit(car_img, (i * cell_size, j * cell_size))
            elif end[0] == i and end[1] == j:
                screen.blit(meta_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 0:
                screen.blit(droga_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 1:
                screen.blit(blokada_img, (i * cell_size, j * cell_size))

    for i in range(L):
        for j in range(L):
            font = pygame.font.Font(None, int(WIDTH / (12 * L)))
            text_surface = font.render(f"({j*L + i})", True, WHITE)
            screen.blit(text_surface,
                        (i * cell_size + cell_size/20, j * cell_size + cell_size/20))

    pygame.display.flip()

def simulate(path, L, city, start, end, t):
    pygame.init()

    cell_size = WIDTH / (3 * L)
    window_size = (L * cell_size, L * cell_size)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Symulator Przejazdu Pojazdu")

    droga_img = pygame.image.load("droga.png").convert_alpha()
    blokada_img = pygame.image.load("blokada.png").convert_alpha()
    car_img = pygame.image.load("car.png").convert_alpha()
    meta_img = pygame.image.load("meta.png").convert_alpha()
    start_img = pygame.image.load("start.png").convert_alpha()
    droga_img = pygame.transform.scale(droga_img, (cell_size, cell_size))
    blokada_img = pygame.transform.scale(blokada_img, (cell_size, cell_size))
    car_img = pygame.transform.scale(car_img, (cell_size, cell_size))
    meta_img = pygame.transform.scale(meta_img, (cell_size, cell_size))
    start_img = pygame.transform.scale(start_img, (cell_size, cell_size))


    show_city(city, start, end, start, screen, cell_size, droga_img, blokada_img, car_img, meta_img, start_img, L)
    # time.sleep(1)

    counter = len(path)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if counter > 0:
            for p in path:
                counter -= 1
                show_city(city, start, end, p, screen, cell_size, droga_img, blokada_img, car_img, meta_img, start_img, L)
                time.sleep(t)

        pygame.display.update()

    # pygame.quit()