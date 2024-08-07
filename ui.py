from tkinter import *
from tkinter.messagebox import *


def quit_app():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')


def show_spam():
    showerror('Spam', 'Sorry, no Spam allowed!')


root = Tk()

# Add Checkbuttons
for i in range(3): Checkbutton(root, text=f'Item {i + 1}').pack()

# Add Radiobuttons
for i in range(2): Radiobutton(root, text=f'Subject {i + 1}', value=i + 1).pack()

# Add Buttons
Button(root, text='Quit', command=quit_app).pack(fill=X)
Button(root, text='Spam', command=show_spam).pack(fill=X)

root.mainloop()
