from tkinter import *

window = Tk()
window.title('Mile to Km converter')
window.minsize(width=500,height=500)
window.config(padx=200 , pady=200)


# miles input
miles_input = Entry()
miles_input.grid(column=1 , row=0)

# miles label
miles_label = Label(text= 'Miles')
miles_label.grid(column=2 , row=0)

# equal label
equal_label = Label(text= 'is equal to ')
equal_label.grid(column=0 , row=1)

# km result
km_result = Label(text= '0')
km_result.grid(column=1 , row=1)

# km label
km_label = Label(text= 'Km')
km_label.grid(column=2 , row=1)

def calculate() :
 if miles_input.get() :
    miles = float(miles_input.get())
    km = round(miles * 1.609 , 4)
    km_result['text'] = km

# calculate button
calculate_button = Button(text= 'Calculate' , command = calculate)
calculate_button.grid(column=1 , row=2)



window.mainloop()