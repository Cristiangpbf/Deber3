from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width=960, height=609)
canvas.pack()

campo=PhotoImage(file='campo.png')
pelota = PhotoImage(file='pelota.png')
gol = PhotoImage(file='gol.png')

canvas.create_image(0, 0 , anchor=NW , image=campo)
canvas.create_image(480-20, 308.5-25, anchor=NW, image=pelota)

def moverPelota(event):

    if event.keysym == 'Up':
        canvas.move(2, 0, -5)
        print(canvas.coords(2))

    elif event.keysym == 'Down':
        canvas.move(2, 0, 5)
        print(canvas.coords(2))
    elif event.keysym == 'Left':
        canvas.move(2, -5, 0)
        print(canvas.coords(2))
    else:
        canvas.move(2, 5, 0)
        print(canvas.coords(2))

    if canvas.coords(2)[0] <= 26 and canvas.coords(2)[1] >= 273.5 and canvas.coords(2)[1] <=293.5:
        canvas.create_image(0, 0, anchor=NW, image=gol)

    if canvas.coords(2)[0] >= 896 and canvas.coords(2)[1] >= 273.5 and canvas.coords(2)[1] <=293.5:
        canvas.create_image(0, 0, anchor=NW, image=gol)


canvas.bind_all('<KeyPress-Up>', moverPelota)
canvas.bind_all('<KeyPress-Down>', moverPelota)
canvas.bind_all('<KeyPress-Left>', moverPelota)
canvas.bind_all('<KeyPress-Right>', moverPelota)

tk.mainloop()