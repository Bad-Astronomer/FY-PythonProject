from tkinter import *

tags = ['google', 'github', 'twitch', 'asfja']
passwords = ['ajsjf', 'rkrss', 'opsde', 'ajdjd']

window = Tk()
window.geometry('750x600')
window.title("PASSWORD GENERATOR")
window.minsize(550, 550)
window.configure(bg='white')

def ok_button():
    window.destroy()

title = Label(window, text="SAVED PASSWORDS", bg = "white",
              font="helvetica 20 bold")
title.pack(pady=20)

frame = LabelFrame(window, padx=20, pady=20, bg='#ADD8E6',
                   relief=RAISED, borderwidth=7)
frame.pack(pady=50, padx=50)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

disp = Listbox(frame, bg='#ADD8E6', font='helvetica 17',
               yscrollcommand=scrollbar.set)

# before execution check if len(passwords) == len(tags) else call Invalid_UI
for i in range(len(passwords)):
    disp.insert(END, tags[i] + ':')
    disp.itemconfig(END, bg='#3aeb34')
    disp.insert(END, passwords[i])
    disp.itemconfig(END, bg='#eb9334')
    disp.insert(END, "")
    disp.pack()

ok_button = Button(frame, text = 'OK', font = 'helvetica 10', command = ok_button)
ok_button.pack(pady = 10, padx=20)

window.mainloop()
