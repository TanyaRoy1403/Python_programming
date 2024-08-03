from tkinter import *
import math
BLUE="#f7f5dd"
GREEN="#72c368"
BLACK="#000000"
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
         window.after(1000, count_down, count-1)

window = Tk()
window.title("Time manager.")
window.config(padx=100, pady=50 , bg=BLUE)
title_label = Label(text="Timer", fg=GREEN, font="courier,60")
title_label.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, highlightthickness=0,bg=BLUE)
tomato_img=PhotoImage(file="C:\\Users\\Asus\\Desktop\\tomato.png")
canvas.create_image(103,112, image=tomato_img)
timer_text=canvas.create_text(100,130, text="", fill="blue", font="courier,35,bold ")
# canvas.create_text(100,130, text="00:00", fill="blue", font="courier,35,bold ")
canvas.grid(column=1, row=1)
canvas.config(bg=BLUE, highlightthickness=0)
count_down(5)
start_button = Button(text="start")
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark = Label(text="✔", fg=GREEN, bg=BLUE)
check_mark.grid(column=1, row=3)

























window.mainloop()