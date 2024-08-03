from tkinter import *

window=Tk()
window.title("hello GUI")


window.minsize(width=500, height=300)
my_label = Label(text=" hii tanya", font=("Arial", 20, "italic"))
my_label.pack(side="top")

my_label["text"]="New text"
my_label.config(text="new text")

#Button

def button_clicked():
    # print("i got it")
    new_text=input.get()
    my_label.config(text= new_text)


button = Button(text="click Me", command=button_clicked)
button.pack()

#Entry 

input = Entry()
input.pack()
print(input.get())





















window.mainloop()
