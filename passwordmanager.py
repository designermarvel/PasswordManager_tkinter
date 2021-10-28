import tkinter
from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip


window = Tk()

window.title("Password Manager")
window.configure(bg="white")

window.config(padx=50,pady=50)
canva = Canvas(width=200,height=200,bg="white",highlightthickness=0)
# ---- PASSWORD MANAGER ---- #
#Password Generator Project
import random

def randomnumber():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



	password_list = []


	password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

	password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
	password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]


	password_list = password_letters + password_symbols + password_numbers	
	random.shuffle(password_list)

	password = "".join(password_list)


	password_entry.insert(0,f"{password}")
	pyperclip.copy(password)

#---- USER INTERFACE AND FUNCTIONALITY -- #

logo_img = PhotoImage(file="logo.png")
canva.create_image(100,100,image=logo_img)
canva.grid(column=1,row=0)
WEBSITE_label = Label(text="Website:",bg="white")
WEBSITE_label.grid(column=0,row=1)

EMAIL_label = Label(text="Email/Username:",bg="white")
EMAIL_label.grid(column=0,row=2)
Password_label = Label(text="Password:",bg="white")
Password_label.grid(column=0,row=3)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=1)
email_entry.insert(0,"example@example.com")
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=1)

def save():
	data1 = website_entry.get()
	data2 = email_entry.get()
	data3 = password_entry.get()

	if len(data1) == 0 or len(data2)  == 0 or len(data3) == 0:
		messagebox.askokcancel(title="alert",message="Don't leave any fields empty")
	else:


		is_ok = messagebox.askokcancel(title=f'{data1}'
		,message=f'These are the details entered \n Email:{data2}\nPassword:{data3}')

		if is_ok:

				with open('data.txt','a')as file_object:
					file_object.write(data1)
					file_object.write(' | ')
					file_object.write(data2)
					file_object.write(' | ')
					file_object.write(data3)
					file_object.write(' | ')
					file_object.write('\n')
					website_entry.delete(0,END)
					password_entry.delete(0,END)




add_button = Button(text="Add",width=20,command=save)
add_button.grid(row=4,column=1)

Generator_button = Button(text="Generate Password",width=15,command=randomnumber)

Generator_button.grid(row=3,column=2)


window.mainloop()
#we can use columnspan to span an item to more than one column!
