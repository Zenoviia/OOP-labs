import tkinter as tk

def open_first_dialog(on_next_callback):
    def on_next_button_click():
        root.destroy()
        on_next_callback()

    def on_cancel_button_click():
        root.destroy()

    root = tk.Toplevel()
    root.title("Перше діалогове вікно")
    root.geometry("300x100")

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=20)

    tk.Button(
        button_frame, 
        text="Далі >", 
        command=on_next_button_click).pack(side=tk.LEFT, padx=10)
    
    tk.Button(button_frame, 
              text="Відміна", 
              command=on_cancel_button_click).pack(side=tk.LEFT, padx=10)

    root.protocol("WM_DELETE_WINDOW", on_cancel_button_click)
    root.wait_window()
