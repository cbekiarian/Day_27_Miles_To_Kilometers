from tkinter import *

def button_clicked():

    val = input.get()
    val = float(val)* 1.60934
    txt5.config(text = val)

window = Tk()
window.config(padx = 20,pady = 20)
window.title("Mile to Km  Converter")
window.minsize(width= 0, height=00)
txt1 = Label()
txt1.grid(row= 0 , column = 0)

input = Entry(width= 10)
input.insert(END,string = "0")
input.grid(row = 0,column = 1)
txt4 = Label(text= "is equal to ")
txt4.grid(row= 1  , column = 0)
txt2 = Label(text= "Miles")
txt2.grid(row= 0 , column = 2)
txt3 = Label(text = "Km")
txt3.grid(row= 1 , column = 2)
txt5 = Label(text = "0")
txt5.grid(row= 1 , column = 1)


button = Button(text= "Calculate", command= button_clicked)
button.grid(row = 2, column = 1)
# my_label = tkinter.Label(text= "i am a label")
# my_label.grid(row = 0 , column =0)
#

#
#
# button =tkinter.Button(text= "Click me", command= button_clicked)
# button.grid(row = 2, column = 0)
#
#

#
#
#
#
#
#
window.mainloop()