from tkinter import *
tags = ['google', 'github', 'twitch', 'asfja']
passwords = ['ajsjf', 'rkrss', 'opsde', 'ajdjd']

window = Tk()
window.geometry('750x600')
window.title("PASSWORD GENERATOR")
window.minsize(550, 550)
window.configure(bg='white')

title = Label(window, text="SAVED PASSWORDS",
              font="helvetica 20 bold")
title.pack(pady=20)

frame = LabelFrame(window, padx=20, pady=20, bg='#ADD8E6',
                   relief=RAISED, borderwidth=7)
frame.pack(pady=50, anchor='nw', padx=50)


# before execution check if len(passwords) == len(tags) else call Invalid_UI
for i in range(len(passwords)):
    disp = Label(frame, text=tags[i] + ": " +
                 passwords[i], bg='#ADD8E6', font='helvatica 12')
    disp.pack(anchor="nw")

window.mainloop()
