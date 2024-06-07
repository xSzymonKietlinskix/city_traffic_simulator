import pygame
import time
import info_screen


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def show_city(city, start, end, current, screen, cell_size, droga_img, blokada_img, car_img, meta_img, start_img, sciezka_img, L):
    screen.fill(BLACK)

    for i in range(L):
        for j in range(L):
            if start[0] == i and start[1] == j:
                screen.blit(start_img, (i * cell_size, j * cell_size))
            elif current[0] == i and current[1] == j:
                screen.blit(car_img, (i * cell_size, j * cell_size))
                city[i][j] = 3
            elif end[0] == i and end[1] == j:
                screen.blit(meta_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 0:
                screen.blit(droga_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 1:
                screen.blit(blokada_img, (i * cell_size, j * cell_size))
                screen.blit(droga_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 3:
                screen.blit(sciezka_img, (i * cell_size, j * cell_size))

    for i in range(L):
        for j in range(L):
            font = pygame.font.Font(None, int(WIDTH / (12 * L)))
            text_surface = font.render(f"({j*L + i})", True, WHITE)
            screen.blit(text_surface,
                        (i * cell_size + cell_size/20, j * cell_size + cell_size/20))

    pygame.display.flip()

def simulate(path, L, city, start, end, t, file_name):
    pygame.init()
    info = pygame.display.Info()
    screen_width = info.current_w
    screen_h = info.current_h

    global WIDTH
    WIDTH = screen_width

    cell_size = WIDTH / (3 * L)
    w = L * cell_size
    h = L * cell_size
    window_size = (w, h)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Symulator Przejazdu Pojazdu")

    droga_img = pygame.image.load("images/droga.png").convert_alpha()
    blokada_img = pygame.image.load("images/blokada.png").convert_alpha()
    car_img = pygame.image.load("images/car.png").convert_alpha()
    meta_img = pygame.image.load("images/meta.png").convert_alpha()
    start_img = pygame.image.load("images/start.png").convert_alpha()
    sciezka_img = pygame.image.load("images/sciezka.png").convert_alpha()
    droga_img = pygame.transform.scale(droga_img, (cell_size, cell_size))
    blokada_img = pygame.transform.scale(blokada_img, (cell_size, cell_size))
    car_img = pygame.transform.scale(car_img, (cell_size, cell_size))
    meta_img = pygame.transform.scale(meta_img, (cell_size, cell_size))
    start_img = pygame.transform.scale(start_img, (cell_size, cell_size))
    sciezka_img = pygame.transform.scale(sciezka_img, (cell_size, cell_size))


    show_city(city, start, end, start, screen, cell_size, droga_img, blokada_img, car_img, meta_img, start_img, sciezka_img, L)
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
                show_city(city, start, end, p, screen, cell_size, droga_img, blokada_img, car_img, meta_img, start_img, sciezka_img, L)
                time.sleep(t)
        else:
            again = info_screen.info(file_name)
            if again:
                counter = len(path)

        pygame.display.update()

    # pygame.quit()