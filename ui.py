from tkinter import *
widget = Label(None, text='Hello GUI world!') #  Makes an instance of the imported Label class
widget.place(relx=.5, rely=.5) #  Packs (arranges) the new Label in its parent widget
widget.mainloop() # Calls mainloop to bring up the window and start the tkinter event loop