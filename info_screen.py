import os
import sys
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


def info(file_name):
    do_again = False
    def again():
        nonlocal do_again
        do_again = True
        root.destroy()
        return True

    def zakoncz():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width // 2
    window_height = screen_height // 2

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.title("Kroki algorytmu A*")

    x, y, unblocked, visited = [], [], [], []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip().split()
            x.append(float(line[0]))
            y.append(float(line[1]))
            unblocked.append(line[2])
            visited.append(line[3])

    fig, ax = plt.subplots()

    colors = []
    for i in range(len(unblocked)):
        if visited[i] == "True":
            colors.append('b')
        elif unblocked[i] == "True":
            colors.append('g')
        elif unblocked[i] == "False":
            colors.append('r')

    ax.scatter(x, y, c=colors)

    # Dodanie legendy
    legend_labels = {
        'g': 'zielony - dostępne skrzyżowanie',
        'r': 'czerwony - zablokowane skrzyżowanie',
        'b': 'niebieski - obecne skrzyżowanie'
    }
    handles = [plt.Line2D([], [], marker='o', color=color, linestyle='None', markersize=10) for color in
               legend_labels.keys()]
    plt.legend(handles=handles, labels=legend_labels.values(), loc="upper center")

    plt.xticks(np.arange(min(x), max(x) + 1, 1))

    # Dodanie etykiet osi
    ax.set_xlabel("Jednostka czasu")
    ax.set_ylabel("Numery skrzyżowań")
    for i in range(len(x)):
        plt.annotate(f'({x[i]}, {y[i]})', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')


    # Dodanie wykresu do interfejsu Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    exit_button = tk.Button(root, text="Zakończ", command=zakoncz)
    exit_button.pack(side=tk.BOTTOM, pady=5)
    exit_button = tk.Button(root, text="Odtwórz ponownie symualcję", command=again)
    exit_button.pack(side=tk.BOTTOM, pady=5)


    # Uruchomienie pętli głównej Tkinter
    root.mainloop()
    return do_again