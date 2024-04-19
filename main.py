import random
import sys
import time
from algorithm import a_star

import numpy as np
import menu
import info_screen
import simulation
from threading import Thread

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def generate_map(L, p):
    city = np.random.choice([0, 1], size=(L, L), p=[1.0-p, p])
    return city

if __name__ == '__main__':
    L, p, t = menu.menu()
    if L == -1:
        exit()

    start = (random.randint(0, L - 1), random.randint(0, L - 1))
    end = (random.randint(0, L - 1), random.randint(0, L - 1))

    city = generate_map(L, p)

    while city[start] == 1:
        start = (random.randint(0, L - 1), random.randint(0, L - 1))
    while city[start] == city[end]:
        end = (random.randint(0, L - 1), random.randint(0, L - 1))
    while city[end] == 1:
        end = (random.randint(0, L - 1), random.randint(0, L - 1))

    path = a_star(city, start, end, L)

    if path:
        print("Znaleziona ścieżka:", path)
    else:
        print("Nie znaleziono ścieżki.")
        exit()

    intersection_list = []
    for p in path:
        intersection_list.append(p[1] * L + p[0])

    print(intersection_list)
    simulation_thread = Thread(target=lambda: simulation.simulate(path, L, city, start, end, t))
    simulation_thread.start()

    info_thread = Thread(target=lambda: info_screen.info(t,intersection_list))
    info_thread.start()


