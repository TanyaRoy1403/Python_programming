from tkinter import*
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip  # it copies and paste anything from clipboard
import json
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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


#Todo find password
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details {website} exists.")
# TODO implementing exception in old and new data
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="alert", message="Please don't leave boxes empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
           # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving update data
                json.dump(data, data_file, indent=4)
        finally:
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
website_label = Label(text="Website:",)
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "roytanya1403@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1,)


# Buttons
generate_password = Button(text="Generate Password",bg="pink", command=generate_password)
generate_password.grid(row=3, column=2)
add_button = Button(text="Add",command=save, bg="pink")
add_button.grid(row=4, column=1,columnspan=2)
search_button = Button(text="search", width=13, bg="blue", command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()