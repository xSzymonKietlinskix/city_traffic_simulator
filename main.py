import random
from algorithm import a_star
import numpy as np
import menu
import simulation
from threading import Thread
import noPathInfo

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def generate_map(L, p):
    city = np.random.choice([0, 1], size=(L, L), p=[1.0-p, p])
    return city

def collect_data():
    L_, p_, t_ = menu.menu()
    while True:
        if L_ < 2 or p_ < 0.1 or p_ > 0.9 or t_ < 0 or t_ > 10 or L_ > 40:
            noPathInfo.npi("Podano błędne dane. L = (0,40), p = (0.1, 0.9), t = (0, inf)")
            L_, p_, t_ = menu.menu()
        else:
            break

    start_ = (random.randint(0, L_ - 1), random.randint(0, L_ - 1))
    end_ = (random.randint(0, L_ - 1), random.randint(0, L_ - 1))

    city_ = generate_map(L_, p_)

    while city_[start_] == 1:
        start_ = (random.randint(0, L_ - 1), random.randint(0, L_ - 1))
    while city_[start_] == city_[end_]:
        end_ = (random.randint(0, L_ - 1), random.randint(0, L_ - 1))
    while city_[end_] == 1:
        end_ = (random.randint(0, L_ - 1), random.randint(0, L_ - 1))

    path_, file_name_ = a_star(city_, start_, end_, L_)
    
    return path_, L_, city_, start_, end_, t_, file_name_

if __name__ == '__main__':
    path, L, city, start, end, t, file_name = collect_data()
    while not path:
        print("Nie znaleziono ścieżki.")
        noPathInfo.npi("Nie znaleziono ścieżki od startu do mety.")
        path, L, city, start, end, t, file_name = collect_data()

    print("Znaleziona ścieżka:", path)


    simulation_thread = Thread(target=lambda: simulation.simulate(path, L, city, start, end, t, file_name))
    simulation_thread.start()


