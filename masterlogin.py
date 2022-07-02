from tkinter import *

#widget is created
window = Tk()
window.geometry('980x600')
window.title("PASSWORD GENERATOR")
window.minsize(550, 550)
window.configure(bg='#748ed7')

# title
title = Label(window, text='''Welcome User
Enter your credentials
''', font='Times 25 bold', bg='#748ed7', pady=20, fg='orange')
title.pack()

frame = LabelFrame(window, padx=20, pady=20, bg='#63e53e',
                   relief=RAISED, borderwidth=7)
frame.pack(padx=30, pady=10)

# username
details = LabelFrame(frame, text='Enter Username: ', bg='#63e53e')
username = Entry(details, font='helvetica 20')
usr = username.get()
details.pack(pady=15, padx=10)
username.pack(pady=20, padx=10)

# master password
details = LabelFrame(frame, text='Enter Master Password: ', bg='#63e53e')
password = Entry(details, font='helvetica 20')
pwd = password.get()
details.pack(pady=15, padx=10)
password.pack(pady=20, padx=10)


window.mainloop()
