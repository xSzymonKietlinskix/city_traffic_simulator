import tkinter as tk


def menu():
    L = -1
    p = 0.0
    t = 0
    def start_action():
        nonlocal L, p, t
        L = entry1.get()
        p = entry2.get()
        t = entry3.get()
        if not(L == '' or p == '' or t == ''):
            print("Rozmiar siatki L: ", L)
            print("Prawdopodobieństwo wystapienia blokady drogowej. (np. 0.5): ", p)
            root.destroy()

    def quit_action():
        root.destroy()

    root = tk.Tk()
    root.title("Symulator przejazdu MENU")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width // 4
    window_height = screen_height // 4

    # Obliczanie pozycji okna na środku ekranu
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Ustawianie pozycji okna
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.tk.call('tk', 'scaling', 1.2)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)


    label1 = tk.Label(root, text="Rozmiar siatki L:")
    label1.grid(row=0, column=0, padx=5, pady=5)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    label2 = tk.Label(root, text="Prawdopodobieństwo wystąpienia blokady drogowej. (np. 0.5): ")
    label2.grid(row=1, column=0, padx=5, pady=5)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=5, pady=5)

    label3 = tk.Label(root, text="Czas pomiędzy kolejnymi krokami w sekundach: ")
    label3.grid(row=2, column=0, padx=5, pady=5)
    entry3 = tk.Entry(root)
    entry3.grid(row=2, column=1, padx=5, pady=5)

    start_button = tk.Button(root, text="Start", command=start_action)
    start_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    quit_button = tk.Button(root, text="Zakończ", command=quit_action)
    quit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # domyślne parametry
    entry1.insert(0, 6)
    entry2.insert(0, 0.3)
    entry3.insert(0, 1)

    root.mainloop()
    return int(L), float(p), float(t)