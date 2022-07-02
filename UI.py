from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def parameters_UI():
    ###main window
    root = Tk()
    root.geometry('250x250')
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
    frame.place(x = 30, y = 100)

    ###Heading for criterias
    criteria = Label(frame, text = '\n\nSelect the criterias for your password', font = 'helvetica 15 bold', fg = 'black', bg = '#ADD8E6')
    criteria.pack(anchor= 'nw')

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
    messagebox.showerror("showerror", "Invalid Input!")
