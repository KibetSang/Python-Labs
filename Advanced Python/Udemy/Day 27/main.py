from tkinter import *
def button_clicked():
    # label.config(text = "Button Clicked")
    input_string.get()
    label.config(text = input_string.get())


window = Tk()
window.title("Student Details" )
window.minsize(400, 400)
label = Label(window, text="This Label", font = ("Arial", 16,))
label.grid(row=0, column=0)

# Buttons

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(row=0, column=3)
new_button.config(bg="red")
new_button.config(padx=5, pady=5)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=2)
# Entry
input_string = Entry(width=20, justify ="left")
input_string.grid(row=3, column=3)













window.mainloop()