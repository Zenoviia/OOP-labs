import tkinter as tk

def open_slider():
    chosen_value = None

    def close_window(value=None):
        nonlocal chosen_value
        chosen_value = value
        root.destroy()

    root = tk.Tk()
    root.title("Повзунок")
    root.geometry("400x200")
    root.resizable(width=False, height=False)

    tk.Label(root, width=20, font="Arial", text="Оберіть число").pack(pady=20)

    slider = tk.Scale(
        root,
        from_=1,
        to=100,
        orient=tk.HORIZONTAL,
        length=300
    )
    slider.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    tk.Button(
        button_frame,
        text="Так",
        font="Arial",
        width=10,
        command=lambda: close_window(slider.get())
    ).pack(side=tk.LEFT, padx=10)

    tk.Button(
        button_frame,
        text="Відміна",
        font="Arial",
        width=10,
        command=lambda: close_window()
    ).pack(side=tk.LEFT, padx=10)

    root.protocol("WM_DELETE_WINDOW", lambda: close_window())
    root.wait_window()

    return chosen_value
