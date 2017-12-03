from tkinter import *

window=Tk()

def km_to_weights():
    #print(e1_value.get())
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t_grams.insert(END,grams)
    t_pounds.insert(END,pounds)
    t_ounces.insert(END,ounces)

l1=Label(window,text="Kg")
l1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=km_to_weights)
b1.grid(row=0,column=2)

l1=Label(window,text="Grams")
l1.grid(row=1,column=0)

l1=Label(window,text="Pounds")
l1.grid(row=1,column=1)

l1=Label(window,text="Ounces")
l1.grid(row=1,column=2)

t_grams=Text(window,height=1,width=20)
t_grams.grid(row=2,column=0)

t_pounds=Text(window,height=1,width=20)
t_pounds.grid(row=2,column=1)

t_ounces=Text(window,height=1,width=20)
t_ounces.grid(row=2,column=2)

window.mainloop()
