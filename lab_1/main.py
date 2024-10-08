import tkinter as tk
from modules.dialog1 import open_first_dialog
from modules.dialog2 import open_second_dialog
from modules.slider_input import open_slider

def open_slider_menu():
    selected_number = open_slider()
    if selected_number:
        info_output.config(text=f"Обране число: {selected_number}")

def open_first_dialog_with_next():
    def open_second_dialog_with_back():
        open_second_dialog(open_first_dialog_with_next, on_yes_button_click)  
    open_first_dialog(open_second_dialog_with_back)  

def open_dialogs_menu():
    open_first_dialog_with_next() 

def on_yes_button_click():
    info_output.config(text="Ви натиснули 'Так'")  
root = tk.Tk()
root.title("Головне вікно")
root.geometry("500x400")
root.resizable(width=False, height=False)

menu = tk.Menu(root)
root.config(menu=menu)

info_output = tk.Label(root, width=30, font="Arial", anchor="w")
info_output.pack(pady=20, padx=20)

slider_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Меню", menu=slider_menu)
slider_menu.add_command(label="Повзунок", command=open_slider_menu)
slider_menu.add_command(label="Вікна діалогу", command=open_dialogs_menu)

root.mainloop()
