from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project


def clear_text():
    password_entry.delete(0, END)


def generate_password():
    clear_text()

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Empty", message='You left some fields empty')
    else:
        is_ok = messagebox.askokcancel(title=f"{website_text}", message=f"These are the detailed entered:\nEmail:"
                                                                        f" {email_text} \nPassword: {password_text}\n \
                                                                        Is it ok to save?")
        if is_ok:
            with open("Data.txt", "a") as data_file:
                data_file.write(f"{website_text} | {email_text} | {password_text}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
# window.minsize(300, 300)
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website: ")
website.grid(row=1, column=0)

email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

password = Label(text="Password: ")
password.grid(row=3, column=0)


# Entries
website_entry = Entry(width=41)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

website_entry.get()


email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string="gregorykowalczyk25@gmail.com")
email_entry.get()


password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)
password_entry.get()

# Buttons

add_button = Button(text="Add", width=41, command=save)
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

window.mainloop()
