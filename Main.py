import os
from tkinter import *
from tkinter import messagebox
window=Tk()
icon = PhotoImage(file = 'icon.png')
window.iconphoto(False, icon)
window.title('Project Manager')

directory = os.getcwd()

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()

v7 = str()
v8 = str()

bigboi = str()

def update():
    lbl=Label(window,
     text=
     str(v1.get()) + 
     str(v2.get()) + 
     str(v3.get()) + 
     str(v4.get()) + 
     str(v5.get()) + 
     str(v6.get()),
    fg='black', font=("Helvetica", 16))
    lbl.place(x=60, y=270)

    global bigboi
    bigboi = v1.get() + v2.get() + v3.get() + v4.get() + v5.get() + v6.get()

    print (bigboi)

def create():
    customer = C8.get()
    project = C9.get()
    if bigboi != 0:
        if project != '':
            if customer == '':
                os.mkdir(project)
                os.chdir(project)
                catalogcreator()
                os.chdir(directory)
                ready()

            elif customer != '':
                os.mkdir(customer + ' - ' + project)
                os.chdir(customer + ' - ' + project)
                catalogcreator()
                os.chdir(directory)
                ready()
        elif project == '':
            messagebox.showerror('ERROR','You need to input something!')
    elif bigboi == 0:
        messagebox.showerror('ERROR',"You can't just create a empty folder!")

def catalogcreator():
        if v1.get() == 1:
            os.mkdir ('Textures')
        if v2.get() == 1:
            os.mkdir ('Exports')
        if v3.get() == 1:
            os.mkdir ('Images')
        if v4.get() == 1:
            os.mkdir ('Documents')
        if v5.get() == 1:
            os.mkdir ('Alphas')
        if v6.get() == 1:
            os.mkdir ('Renders')


def ready():
    messagebox.showinfo('Project Manager','Your folders are ready!', command = window.destroy())
    


C1 = Checkbutton(window, text = "Textures", variable = v1, command = update)
C2 = Checkbutton(window, text = "Exports", variable = v2, command = update)
C3 = Checkbutton(window, text = "Images", variable = v3, command = update)
C4 = Checkbutton(window, text = "Documents", variable = v4, command = update)
C5 = Checkbutton(window, text = "Alphas", variable = v5, command = update)
C6 = Checkbutton(window, text = "Renders", variable = v6, command = update)

C7 = Button(window, text = "Create", command = create, cursor = "spider",)

C8 = Entry(window, textvariable = v7)
C9 = Entry(window, textvariable = v8)

C10 = Label(window,text = "Customer")
C11 = Label(window,text = "Project")

C1.place(x=300, y=10)
C2.place(x=300, y=40)
C3.place(x=300, y=70)
C4.place(x=300, y=100)
C5.place(x=300, y=130)
C6.place(x=300, y=160)
C7.place(x=350, y=270)
C8.place(x=100, y=10)
C9.place(x=100, y=40)
C10.place(x=30, y=10)
C11.place(x=30, y=40)

update()

window.resizable(False, False)
window.geometry("400x300+10+10")
window.mainloop()