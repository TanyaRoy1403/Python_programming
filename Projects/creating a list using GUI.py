from tkinter import *

#Creating new window and configurations
window=Tk()
window.title("List")
# window.minsize(width=500, height=500)
window.geometry("600x600")



#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()


#Buttons
def action():
    print("Do somthing")

#calls action() when passed


button = Button(text="Click on me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text= Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Add some text to begin with
text.insert(END, "example of multiline text entry")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()
#Spin box
def spin_box():
 #get current value in spinbox
      print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spin_box)
spinbox.pack()

#Scale
#Called with current scale  value.
def scale_value(value):
    print(value)
scale= Scale(from_=0, to=100, command=scale_value)
scale.pack()

#Check button
def check_button():
#prints 1 if on button checked, otherwise 0
      print(check_state.get())
#variable to hold on to checked state, 0 is off, 1 is on
check_state = IntVar()
checkbutton= Checkbutton(text="Is on?", variable=check_state, command=check_button)
check_state.get()
checkbutton.pack()

#Radiobutton
def radio_button():
    print(radio_state.get())

#variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="option1", value=1, variable=radio_state, command=radio_button)
radiobutton2 = Radiobutton(text="option2", value=2, variable=radio_state, command=radio_button)
radiobutton3 = Radiobutton(text="option3", value=3, variable=radio_state, command=radio_button)
radiobutton4 = Radiobutton(text="option4", value=4, variable=radio_state, command=radio_button)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

#Listbox
def list_box():
    #get current selection from listbox
    print(listbox.get(listbox.curselection()))
listbox= Listbox(height=4)
fruits = ["Applee", "Pear", "orange", "cherry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<Listboxselection>>",list_box)
listbox.pack()



















window.mainloop()
