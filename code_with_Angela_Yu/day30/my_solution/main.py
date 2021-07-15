# Acknowledgement = DR. Angela (udemy.com), Dr Bro code (youtube)
import string
from tkinter import *
from time import *
from PIL import Image
from string import *
import os
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


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
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    def report(_):
        website = website_entry1.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            elif website =="":
                messagebox.showinfo(title="Error", message="Please! fill in the entry")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    window2 = Toplevel()
    window2.title("Search Engines")
    window2.config(padx=20, pady=20)
    window2.resizable(0,0)
    search_website = Label(window2, text="Website:")
    search_website.grid(row=0, column=0)
    website_entry1 = Entry(window2, width=30)
    website_entry1.bind("<Return>", report) # this line of code will allow us to press the "return" key and run the-
    # report function; however, by default, it will pass 1 unknown argument to the report function. Therefore, we-
    # have to put a parameter in the report function, or it won't work. I decided to use "_" as the parameter.
    website_entry1.grid(row=0, column=1)
    exit_button = Button(window2, text="Exit", command=window2.destroy)   # destroy is use to close the window2 only
    exit_button.grid(row=1, column=0, sticky=W + E)
    search_button1 = Button(window2, text="Search", command=report)
    search_button1.grid(row=1, column=1, sticky=W + E)


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
password_entry = Entry(frame3, width=18)
password_entry.grid(row=3, column=1, sticky=W+E)

# Todo: setup buttons and put it into frame3
generate_password_button = Button(frame3, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky=W+E)
add_button = Button(frame3, text="Add", width=18, command=save)
add_button.grid(row=4, column=1, sticky=W+E)
search_button = Button(frame3, text= "Search", width=16, command=find_password)
search_button.grid(row=4, column=2, sticky=W+E)

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
Button(frame2, text="M", fg="#FFAEBC", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[0].show()).pack(side=LEFT)
Button(frame2, text="E", fg="#FFAEBC", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[1].show()).pack(side=LEFT)
Button(frame2, text="O", fg="#FFAEBC", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[2].show()).pack(side=LEFT)
Button(frame2, text="W", fg="#FFAEBC", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[3].show()).pack(side=LEFT)
# Button(frame2, text="L", fg="" ,font=("Party LET", 25), width=5, height=3, command=lambda: img_list[4].show()).pack(side=LEFT)
# Button(frame2, text="A", fg="" ,font=("Party LET", 25), width=5, height=3, command=lambda: img_list[5].show()).pack(side=LEFT)
Button(frame2, text="♥️", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[6].show()).pack(side=LEFT)
Button(frame2, text="!", fg="#FFAEBC", font=("Party LET", 25), width=5, height=3, command=lambda: img_list[7].show()).pack(side=LEFT)

window.resizable(0,0)
window.mainloop()
