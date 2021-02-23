from tkinter import *
from tkinter.colorchooser import askcolor


default_color = 'black'
default_size = '2.0'
b1 = 'up'
x_old = None
y_old = None

def b1down(event):
    global b1
    b1 = 'down'

def b1up(event):
    global b1, x_old, y_old
    b1 = 'up'
    x_old = None
    y_old = None

def motion(event):
    global x_old, y_old, b1
    if b1 == 'down':
        if x_old is not None and y_old is not None:
            event.widget.create_line(x_old, y_old, event.x, event.y, smooth=True, fill=default_color, width=default_size)
        x_old = event.x
        y_old = event.y

def choose_color():
    global default_color
    color = askcolor()[1]
    if color != None:
        default_color = color
    else:
        return None


def main():
    window = Tk()
    window.title('Alex Paint')

    color_button = Button(window, text='color', command=choose_color)
    color_button.grid(row=0, column=2)

    canvas = Canvas(window, bg='white', width=500, height=400)
    canvas.grid(row=1, columnspan=5)

    def clear_canvas():
        canvas.delete("all")

    clear_button = Button(window, text='clear', command=clear_canvas)
    clear_button.grid(row=0, column=3)

    canvas.bind('<Motion>', motion) 
    canvas.bind('<ButtonPress-1>', b1down) 
    canvas.bind('<ButtonRelease-1>', b1up)

    window.mainloop()



main()