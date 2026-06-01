from tkinter import*

window = Tk()
window.title("GUI Program")
window.minsize(width = 500,height = 500)
window.config(padx=20,pady=20)

#Label
my_label = Label(text = "I am a Label",font = ("Arial",24,"bold"))
my_label.config(text='new text')
my_label.grid(column=0,row=0)

#Buttons
def click():
    new_text = input.get()
    my_label.config(text= new_text)
    print(input.get())

button = Button(text = "Click Me", command= click)
button.grid(column=1,row=1)

new_button = Button(text="Click Here!",command=click)
new_button.grid(column=2,row=0)

#Entry
input= Entry(width=30)
input.insert(END, string="Enter your text here.")
print(input.get())
input.grid(column=3,row=1)

window.mainloop()