import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

def plot_function():
    func_input = function_entry.get()
    try:
        x = np.linspace(-10, 10, 1000)

        local_namespace = {
            'x': x,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'ctg': lambda x: 1 / np.tan(x),
            'exp': np.exp,
            'log': np.log,
            'sqrt': np.sqrt,
        }

        y = eval(func_input, {"__builtins__": {}}, local_namespace)

        plt.figure(figsize=(8, 5))
        plt.plot(x, y, label=f"y = {func_input}")
        plt.title(f"График функции: y = {func_input}")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.show()
    except Exception as e:
        messagebox.showerror("Ошибка", "oshibka")

def exit_application():
    root.destroy()

root = Tk()
root.title("Визуализация функций")

Label(root, text="Введите функцию от x:", font=("Arial", 12)).pack(pady=10)

function_entry = StringVar()
Entry(root, textvariable=function_entry, font=("Arial", 14), width=30).pack(pady=5)

Button(root, text="Построить график", command=plot_function, font=("Arial", 12), bg="lightblue").pack(pady=10)
Button(root, text="Выход", command=exit_application, font=("Arial", 12), bg="lightcoral").pack(pady=5)

root.mainloop()