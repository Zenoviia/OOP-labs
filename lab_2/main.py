from tkinter import *

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('OOP_lab2')
        self.root.geometry('400x400')
        self.root.resizable(width=False, height=False)

        self.create_menu()

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Файл", menu=file_menu)

        objects_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Об'єкти", menu=objects_menu)

        information_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Довідка", menu=information_menu)



root = Tk()
main_window = MainWindow(root)
root.mainloop()