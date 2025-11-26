from tkinter import *
window = Tk()
window.title("Miles Calculator")
window.geometry("300x300")
def button_clicked():
    miles = float(input_entry.get()) * 1.609
    label_three.config(text=str(miles))

window.config(padx=50, pady=50)
input_entry = Entry()
input_entry.grid(row=2, column=2)

label = Label(window, text="Miles")
label.grid(row=2, column=3)

label_two = Label(window, text="is equal to")
label_two.grid(row=3, column=1)

label_three = Label(window, text="0")
label_three.grid(row=3, column=2)

label_four = Label(window, text="KM")
label_four.grid(row=3, column=3)
#
button = Button(text="Calculate", command=button_clicked)
button.grid(row=4, column=2)





window.mainloop()
