from tkinter import *
from PIL import Image, ImageTk


def parameters_UI():
    ###main window
    root = Tk()
    root.geometry('750x1000')
    root.title("PASSWORD GENERATOR")
    root.minsize(550, 550)
    root.configure(bg = 'white')


    ###Bg Image
    '''photo = Image.open('Password generator/4.jpg')
    picture = ImageTk.PhotoImage(photo)
    pict = Label(image = picture)
    pict.place(x = 0, y = 0, relwidth=1, relheight=1)'''


    ###Frame for criterias
    frame = LabelFrame(root, padx = 20, pady = 20, bg = '#ADD8E6', relief = RAISED, borderwidth=7)
    frame.pack(pady=150)

    ###Heading for criterias
    criteria = Label(frame, text = '\n\nSelect the criterias for your password', font = 'helvetica 15 bold', fg = 'black', bg = '#ADD8E6')
    criteria.pack()

    ###Checkbox Command
    def checkbox():
        response_special.config(text = var.get())
        response_digits.config(text = var1.get())
        global inp 
        inp = len_entry.get(1.0, "end-1c")
        root.destroy()
        

    ###Checkbox variable
    var = StringVar(value = 'No Characters')
    var1 = StringVar(value = 'No digits')

    ###Creating Checkboxes
    special_char = Checkbutton(frame, text = 'Special Characters', variable=var, onvalue="Include Char",offvalue='No Characters', font = 'helvetica 10 bold', bg = '#ADD8E6')
    special_char.pack(anchor = 'nw', pady = 10)

    digits = Checkbutton(frame, text = 'Numbers in password', onvalue="Include digits", offvalue="No digits", variable=var1, font = 'helvetica 10 bold', bg = '#ADD8E6')
    digits.pack(anchor = 'nw')

    response_special = Label(root)
    #response_special.place(x = 30, y = 450)

    response_digits = Label(root)
    #response_digits.place(x = 30, y = 480)

    #Creating Length Criteria
    length = LabelFrame(frame, text = 'Enter the length of password you want to generate', bg = '#ADD8E6', font = 'helvetica 12 bold')
    length.pack(anchor = 'nw', pady = 15, padx = 10)
    len_entry = Text(length, height = 1, width = 20)
    len_entry.pack(pady = 20, padx = 10)


    ###Creating Generate Button
    generate = Button(frame, text = 'Generate Password', font = 'comicsansms 13', command = checkbox)
    generate.pack()
    root.mainloop()
    
    if var.get() == 'No Characters':
        spchar = False
    else:
        spchar = True
    if var1.get() == 'No digits':
        num = False
    else:
        num = True
    return spchar, num, inp


def invalid_UI():
    root = Tk()
    root.geometry('200x100')
    root.title("Error")
    root.configure(bg = "white")

    def ok_button():
        root.destroy()

    invalid = Label(text='\nInvalid Input!', bg = 'white', font = 'helvetica 16')
    invalid.pack()

    ok_button = Button(text = 'OK', font = 'helvetica 10', command = ok_button)
    ok_button.pack(pady = 10, padx=20)

    root.mainloop()


def master_UI():
    #widget is created
    window = Tk()
    window.geometry('750x1000')
    window.title("PASSWORD GENERATOR")
    window.minsize(550, 550)
    window.configure(bg='white')

    # title
    title = Label(window, text='''Welcome User
    Enter your credentials
    ''', font='Times 25 bold',bg='white', pady=20, fg='black')
    title.pack()

    frame = LabelFrame(window, padx=20, pady=20, bg='#ADD8E6',
                    relief=RAISED, borderwidth=7)
    frame.pack(padx=30, pady=10)

    def close():
        global usr
        global pwd
        usr = username.get()
        pwd = password.get()
        window.destroy()
    # username
    details = LabelFrame(frame, text='Enter Username: ', bg='#ADD8E6')
    username = Entry(details, font='helvetica 20')
    details.pack(pady=15, padx=10)
    username.pack(pady=20, padx=10)

    # master password
    details = LabelFrame(frame, text='Enter Master Password: ', bg='#ADD8E6')
    password = Entry(details, font='helvetica 20')
    details.pack(pady=15, padx=10)
    password.pack(pady=20, padx=10)

    enter = Button(frame, text = 'Enter', font = 'helvetica 15', command = close)
    enter.pack(pady = 20)

    window.mainloop()
    return usr, pwd


def display_UI():
    root = Tk()
    root.geometry('750x1000')
    root.title("Menu Options")
    root.configure(bg = 'white')

    frame = LabelFrame(root, bg = '#ADD8E6', relief=RAISED, borderwidth=7)
    frame.pack(pady=150)


    def create():
        global a
        a = 1
        root.destroy()    

    def show():
        global a
        a = 2
        root.destroy()

    def save_exit():
        global a
        a = 3
        root.destroy()

    option = Label(frame, text = 'Select the Menu Option', font = 'helvetica 25', fg = 'black', bg = '#ADD8E6')
    option.pack(padx = 50, pady = 30)

    create = Button(frame, text = 'Create New Password', font = 'helvetica 15', command=create)
    create.pack(pady = 10)

    show = Button(frame, text='Show saved Passwords', font='helvetica 15', command=show)
    show.pack(pady = 10)

    save_exit = Button(frame, text = 'Save & Exit', font = 'helvetica 15', command = save_exit)
    save_exit.pack(pady = 10)

    root.mainloop()
    return a


def pwd_display_UI(caption, password):
    tags = caption
    passwords = password

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


def pwd_maker_UI(password):
    root = Tk()
    root.geometry('750x1000')
    root.title('Generated Password')
    root.configure(bg = 'white')

    def keep_pw():
        def save_button():
            global input_tag
            input_tag = entrybox.get()
            root.destroy()
                
        sitename = LabelFrame(frame, text = 'Enter the name in which you want to store the password', bg = '#ADD8E6', font = 'helvetica 12 bold')
        sitename.pack(pady = 15, padx = 10)
        entrybox = Entry(sitename, font = 'helvetica 15')
        entrybox.pack(pady = 20, padx = 10)
        ok_button = Button(frame, text = 'SAVE & EXIT', font = 'helvetica 10', command = save_button)
        ok_button.pack(pady = 10, padx=20)

    def regenerate():
        global regen
        regen = 1
        root.destroy()

    frame = LabelFrame(root, bg = '#ADD8E6', relief=RAISED, borderwidth=7)
    frame.pack(pady = 150)

    pw_display = Label(frame, text = password, font = 'helvetica 20', bg = '#ADD8E6', fg = 'red')
    pw_display.pack(pady = 15, padx = 50)

    keep = Button(frame, text = 'Keep the password', font = 'helvetica 10', command = keep_pw)
    keep.pack(pady = 10)

    regenerate = Button(frame, text = 'Regenerate Password', font = 'helvetica 10', command = regenerate)
    regenerate.pack(pady = 10)

    root.mainloop()
    try:
        if regen == 1:
            return False
    except NameError:
        return input_tag
