import random
import time
from a_star import a_star_

import pygame
import numpy as np



def generate_map(L):
    city = np.random.choice([0, 1], size=(L, L), p=[0.6, 0.4])
    return city

def show_city(city, start, end, current):
    screen.fill(BLACK)
    for i in range(L):
        for j in range(L):
            if start[0] == i and start[1] == j:
                screen.blit(car_img, (i * cell_size, j * cell_size))
            elif current[0] == i and current[1] == j:
                screen.blit(car_img, (i * cell_size, j * cell_size))
            elif end[0] == i and end[1] == j:
                screen.blit(meta_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 0:
                screen.blit(droga_img, (i * cell_size, j * cell_size))
            elif city[i][j] == 1:
                screen.blit(blokada_img, (i * cell_size, j * cell_size))

    pygame.display.flip()

if __name__ == '__main__':
    L = int(input("Podaj rozmiar siatki: "))

    start = (random.randint(0, L - 1), random.randint(0, L - 1))
    end = (random.randint(0, L - 1), random.randint(0, L - 1))

    city = generate_map(L)

    while city[start] == 1:
        start = (random.randint(0, L - 1), random.randint(0, L - 1))
    while city[end] == 1:
        end = (random.randint(0, L - 1), random.randint(0, L - 1))

    pygame.init()
    BLACK = (0, 0, 0)
    cell_size = 50
    window_size = (L * cell_size, L * cell_size)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Symulator Przejazdu Pojazdu")

    droga_img = pygame.image.load("droga.png").convert_alpha()
    blokada_img = pygame.image.load("blokada.png").convert_alpha()
    car_img = pygame.image.load("car.png").convert_alpha()
    meta_img = pygame.image.load("meta.png").convert_alpha()

    droga_img = pygame.transform.scale(droga_img, (cell_size, cell_size))
    blokada_img = pygame.transform.scale(blokada_img, (cell_size, cell_size))
    car_img = pygame.transform.scale(car_img, (cell_size, cell_size))
    meta_img = pygame.transform.scale(meta_img, (cell_size, cell_size))
    path = a_star_(city, start, end, L)

    if path:
        print("Znaleziona ścieżka:", path)
    else:
        print("Nie znaleziono ścieżki.")

    show_city(city, start, end, start)
    time.sleep(1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for p in path:
            show_city(city, start, end, p)
            time.sleep(1)

        pygame.display.update()

    pygame.quit()



