# Acknowledgement = DR. Angela (udemy.com), Dr Bro code (youtube)
import string
from tkinter import *
from time import *
from PIL import Image
from string import *
import os
# from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# TODO: all function will be put here

# ---------------------------- DATE_TIME GENERATOR ------------------------------- #
def date_time():
    """Real-time clock"""
    # global time_label, day_label, date_label
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    frame1.after(1000, date_time)  # use recursive technique; this function allows the frame1 to update in every 1000ms

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    # letters = ascii_letters     # it return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # numbers = digits            # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # symbols = punctuation       # ['!', '#', '$', '%', '&', '(', ')', '*', '+', etc]

    password_letters = [choice(ascii_letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(punctuation) for _ in range(randint(2, 4))]
    password_numbers = [choice(digits) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    # mode = 'a' if os.path.exists(".") else 'w'
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

    # if len(website) == 0 or len(password) == 0:
    #     messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    #     # note: message box does work well on mac bigsur
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
    #                                                   f"\nPassword: {password} \nIs it ok to save?")
    #     if is_ok:
    #         mode = 'a' if os.path.exists(".") else 'w'
    #         with open("data.txt", "a") as data_file:
    #             data_file.write(f"{website} | {email} | {password}\n")
    #             website_entry.delete(0, END)
    #             password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# TODO: setup a window to work on
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.config(bg="light yellow")

# TODO: setup all the frames and put it into a window

frame3 = Frame(window, bg="light yellow")
frame3.pack(side=TOP)

frame1 = Frame(window, bg="light yellow")
frame1.pack(side=LEFT)       # note: we can't put the pack() in one line with Frame() because it won't work. I don't know why.

frame2 = Frame(window, bg="light yellow", relief=SUNKEN, padx=5, pady=5)
frame2.pack(side=BOTTOM)




# Todo: create a canvas to put a logo image
# canvas = Canvas(frame3, height=200, width=200, bg="light yellow", relief=SUNKEN)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
logo = PhotoImage(file="logo.png")
logo_label = Label(frame3, image=logo, bg="light yellow")
logo_label.grid(row=0, column=0, columnspan=3)

# Todo: setup labels and put it into frame3
website_label = Label(frame3, text="Website:", bg="light yellow")
website_label.grid(row=1, column=0)
email_label = Label(frame3, text="Email/Username:", bg="light yellow")
email_label.grid(row=2, column=0)
password_label = Label(frame3, text="Password:", bg="light yellow")
password_label.grid(row=3, column=0)

# Todo: setup entries and put it into frame3
website_entry = Entry(frame3, width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(frame3, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@gmail.com")
password_entry = Entry(frame3, width=21)
password_entry.grid(row=3, column=1)

# Todo: setup buttons and put it into frame3
generate_password_button = Button(frame3, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(frame3, text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# TODO: set up labels for real-time clock
time_label = Label(frame1, font=("Arial", 16), bg="light yellow")
time_label.pack() # don't use it on the same line with Label(); you wont be able to use .config function; and i may cause some errors.
day_label = Label(frame1, font=("PT Mono", 16), bg="light yellow")
day_label.pack()
date_label = Label(frame1, font=("PT Mono", 16), bg="light yellow")
date_label.pack()

date_time()     # call the clock

# Todo: make a list of images and embed it to buttons
img_list = []
for img in os.listdir("./png wallpapers"):
    i = Image.open(f"./png wallpapers/{img}")
    img_list.append(i)

# Todo: create buttons and allows users to view different image when clicking on each letter
Button(frame2, text="M", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[0].show()).pack(side=LEFT)
Button(frame2, text="E", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[1].show()).pack(side=LEFT)
Button(frame2, text="O", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[2].show()).pack(side=LEFT)
Button(frame2, text="W", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[3].show()).pack(side=LEFT)
# Button(frame2, text="L", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[4].show()).pack(side=LEFT)
# Button(frame2, text="A", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[5].show()).pack(side=LEFT)
Button(frame2, text="♥️", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[6].show()).pack(side=LEFT)
Button(frame2, text="!", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[7].show()).pack(side=LEFT)

window.resizable(0,0)
window.mainloop()
