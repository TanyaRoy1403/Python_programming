from tkinter import*
window=Tk()
WHITE="#FFFFFF"
window.geometry("600x600")
window.title("PASSWORD")
canvas = Canvas(height=200, width=200, bg=WHITE)
window.config(padx=50, pady=50)
logo_img=PhotoImage(file="C:\\Users\\Asus\\Desktop\\imageslogo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)


#Labels
website_label = Label(text="Website:", font="20")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:", font="20")
email_label.grid(row=2, column=0)
password_labl = Label(text="Password:", font="20")
password_labl.grid(row=3, column=0)


#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry=Entry(width=32)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


#Buttons
generate_password = Button(text="Generate Password")
generate_password.grid(row=3, column=2)
add_button =Button(text="Add")
add_button.grid(row=4, column=1,columnspan=2)






window.mainloop()