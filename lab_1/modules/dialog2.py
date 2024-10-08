import tkinter as tk

def open_second_dialog(on_back_callback, on_yes_callback):
    def on_back_button_click():
        root.destroy()
        on_back_callback()

    def on_yes_button_click():
        root.destroy()
        on_yes_callback()

    def on_cancel_button_click():
        root.destroy()

    root = tk.Toplevel()
    root.title("Друге діалогове вікно")
    root.geometry("300x100")

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)

    tk.Button(button_frame, text="< Назад", command=on_back_button_click).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Так", command=on_yes_button_click).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Відміна", command=on_cancel_button_click).pack(side=tk.LEFT, padx=10)

    root.protocol("WM_DELETE_WINDOW", on_cancel_button_click)
    root.wait_window()
