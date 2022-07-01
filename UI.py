from cProfile import label
import imp
from lib2to3.pgen2.pgen import generate_grammar
from msilib.schema import CheckBox
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('1200x750')
root.title("PASSWORD GENERATOR")
root.minsize(550, 550)


photo = Image.open('Password generator/4.jpg')
picture = ImageTk.PhotoImage(photo)
pict = Label(image = picture)
pict.place(x = 0, y = 0, relwidth=1, relheight=1)


heading = Label(text = 'Welcome to Password Generator', font = 'comicsansms 25 bold', bg = 'black', fg = 'red')
heading.pack()

frame = LabelFrame(root, padx = 20, pady = 20, bg = '#ADD8E6', relief = RAISED, borderwidth=7)
frame.pack(anchor = 'nw', padx = 30, pady = 100)

criteria = Label(frame, text = '\n\nSelect the criterias for your password', font = 'helvetica 15 bold', fg = 'red', bg = '#ADD8E6')
criteria.pack(anchor= 'nw')

# Special characters in password(Y/N): y
# Numbers in password(Y/N): y
# Enter length of password: 25

check1 = Checkbutton(frame, text = 'Special Characters', font = 'helvetica 10 bold', bg = '#ADD8E6')
check1.pack(anchor = 'nw', pady = 10)

check2 = Checkbutton(frame, text = 'Numbers in password', font = 'helvetica 10 bold', bg = '#ADD8E6')
check2.pack(anchor = 'nw')

length = LabelFrame(frame, text = 'Enter the length of password you want to generate', bg = '#ADD8E6', font = 'helvetica 10 bold')
length.pack(anchor = 'nw', pady = 15, padx = 10)

len_entry = Entry(length, font = 'helvetica 20')
len_entry.pack(pady = 20, padx = 10)

generate = Button(frame, text = 'Generate Password', font = 'comicsansms 13')
generate.pack()

pw_gen = Entry(frame, text = '', font = 'helvetica 25')
pw_gen.pack(pady = 20, anchor = 'nw', padx = 10)

root.mainloop()
