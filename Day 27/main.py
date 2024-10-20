import tkinter

window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width = 500 , height= 500)

#Label

my_label = tkinter.Label(text='I Am a Label', font=('Arial' , 24 , 'bold'))
my_label.pack(side='left')

# my_label['text'] = 'New Label Text'
my_label.config(text='New Text' , font =('Arial' , 25 , 'bold'))









window.mainloop()