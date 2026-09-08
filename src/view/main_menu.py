from tkinter import Tk, ttk, N, W, E, S
import tkinter

class Main:
    def __init__(self, root: Tk) -> None:
        name: str = "Sistema de Adoção Patinhas Felizes"
        root.title(name)

        # we use a frame themed to the system to hold all of our widgets
        frame: ttk.Frame = ttk.Frame(root)
        frame.grid(column=0, row=0, sticky=( N, W, E, S ))

        label: ttk.Label = ttk.Label(frame, text=name)
        label.grid(column=0, row=0)

        self.buttons(frame, 2)

        root.mainloop()

    def buttons(self, frame: ttk.Frame, row_offset: int):
        # TODO we need to specify the commands for every button
        cad_dog = tkinter.Button(frame)
        cad_cat = tkinter.Button(frame)
        list_animals = tkinter.Button(frame)
        cad_adot = tkinter.Button(frame)
        solic_adoc = tkinter.Button(frame) 

        # we could join pending adoptions in one menu, providing buttons for approval/decline
        aprov_adoc = tkinter.Button(frame)
        rejeitar_adoc = tkinter.Button(frame)
        list_adoc = tkinter.Button(frame)

        buttons: list[tkinter.Button] = []
        buttons.append(cad_dog)
        buttons.append(cad_cat)
        buttons.append(list_animals)
        buttons.append(cad_adot)
        buttons.append(solic_adoc)
        buttons.append(aprov_adoc)
        buttons.append(rejeitar_adoc)
        buttons.append(list_adoc)

        for i, button in enumerate(buttons):
            button.grid(row=(i + row_offset))
