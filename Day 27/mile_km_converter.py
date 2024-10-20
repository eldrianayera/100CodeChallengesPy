from tkinter import *

window = Tk()
window.title('Mile to Km converter')
window.minsize(width=500,height=500)

miles_input = Entry()
miles_input.grid(column=1 , row=0)

miles_label = Label(text= 'Miles')
miles_label.grid(column=2 , row=0)

window.mainloop()