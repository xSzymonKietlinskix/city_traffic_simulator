import os
import sys
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import threading
import time


def info(t, list):


    def zakoncz():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    # Funkcja aktualizująca wykres co czas t
    def update_plot():
        i = 0
        while True:
            if i == len(list):
                break
            y = list[i]
            x = i
            i += 1
            ax.plot(x, y, 'o', label=f'Skrzyżowanie {y}')
            # Odświeżenie legendy wykresu
            ax.legend()
            # Odświeżenie wykresu w interfejsie Tkinter
            canvas.draw()
            # Pauza na czas t
            time.sleep(t)

    # Tworzenie interfejsu Tkinter
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Wykres odwiedzonych skrzyżowań")

    # Tworzenie wykresu Matplotlib
    fig, ax = plt.subplots()
    ax.set_ylabel('Numer Skrzyżowania')
    ax.set_xlabel('Jednostka czasu')
    ax.set_title('Odwiedzone skrzyżowania w danym czasie')
    ax.grid(True)

    # Dodanie wykresu do interfejsu Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    exit_button = tk.Button(root, text="Zakończ", command=zakoncz)
    exit_button.pack(side=tk.BOTTOM, pady=5)

    # Uruchomienie funkcji aktualizującej wykres w osobnym wątku
    update_thread = threading.Thread(target=update_plot)
    update_thread.daemon = True
    update_thread.start()


    # Uruchomienie pętli głównej Tkinter
    root.mainloop()