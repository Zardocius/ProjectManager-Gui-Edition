from tkinter import *
from tkinter.ttk import Combobox
window=Tk()

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()

def update():
    lbl=Label(window,
     text=
     str(v1.get()) + 
     str(v2.get()) + 
     str(v3.get()) + 
     str(v4.get()) + 
     str(v5.get()) + 
     str(v6.get()),
    fg='red', font=("Helvetica", 16))
    lbl.place(x=60, y=50)

C1 = Checkbutton(window, text = "Textures", variable = v1, command= update)
C2 = Checkbutton(window, text = "Exports", variable = v2, command= update)
C3 = Checkbutton(window, text = "Images", variable = v3, command= update)
C4 = Checkbutton(window, text = "Documents", variable = v4, command= update)
C5 = Checkbutton(window, text = "Alphas", variable = v5, command= update)
C6 = Checkbutton(window, text = "Renders", variable = v6, command= update)

C1.place(x=300, y=10)
C2.place(x=300, y=40)
C3.place(x=300, y=70)
C4.place(x=300, y=100)
C5.place(x=300, y=130)
C6.place(x=300, y=160)

icon = PhotoImage(file = 'icon.png')
window.iconphoto(False, icon)
window.title('Project Manager')
window.resizable(False, False)
window.geometry("400x300+10+10")
window.mainloop()