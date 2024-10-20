from tkinter import *

window = Tk()
window.title('My First GUI Program')
window.minsize(width = 500 , height= 500)

#Label

my_label = Label(text='I Am a Label', font=('Arial' , 24 , 'bold'))
my_label.pack()

# my_label['text'] = 'New Label Text'
my_label.config(text='New Text' , font =('Arial' , 25 , 'bold'))


# Button

def button_clicked():
    print('I got clicked')
    if my_label
    my_label['text'] = 'I Got Clicked !'

button = Button(text= 'Click Me' , command = button_clicked)
button.pack()




window.mainloop()