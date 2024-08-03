from tkinter import*
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip  # it copy and paste anything from clipboard
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    # nr_letters =random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # password_list = []
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    #
    # random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)  # now you can paste this password by ctrl+v at anywhere


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="alert", message="Please don't leave boxes empty")

    # messagebox.showinfo(title="Title", message="Message")
    # messagebox.askokcancel(title=website, message=
    # f"These are the details you have entered:\n Email:{email}\n Password:{password}\n"
    #                                               f"is this ok ?")

    with open("Data1.txt", "a") as data_file:
        data_file.write(f"{website}| {email} |{password}\n\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


window = Tk()
WHITE = "#FFFFFF"
window.geometry("600x600")
window.title("PASSWORD")
canvas = Canvas(height=200, width=200, bg=WHITE)
window.config(padx=50, pady=50)
logo_img=PhotoImage(file="C:\\Users\\Asus\\Desktop\\imageslogo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:", font="10")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:", font="10")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:",font="10")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry=Entry(width=32)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"roytanya1403@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1,)


# Buttons
generate_password = Button(text="Generate Password", font="5", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add",font="5", command=save)
add_button.grid(row=4, column=1,columnspan=2)


window.mainloop()