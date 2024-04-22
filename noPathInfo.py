import tkinter as tk
import os
import sys

def npi(info):
    def again():
        root.destroy()

    def quit_action():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    root = tk.Tk()
    root.title("Symulator przejazdu")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = screen_width // 4
    window_height = screen_height // 4

    # Obliczanie pozycji okna na środku ekranu
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Ustawianie pozycji okna
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.tk.call('tk', 'scaling', 2.0)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    label1 = tk.Label(root, text=info)
    label1.grid(row=0, column=0, padx=5, pady=5)

    start_button = tk.Button(root, text="Spróbuj jeszcze raz!", command=again)
    start_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    quit_button = tk.Button(root, text="Zakończ", command=quit_action)
    quit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()