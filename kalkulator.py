import Tkinter as tk

window = tk.Tk()
window.title("Kalkulator")

def set_text(text):
    input_field.insert(tk.END, text)
    input_field.xview_moveto(1)

def clear():
    input_field.delete(0, "end")


def equals():
    value = eval(input_field.get())
    clear()
    input_field.insert(0, value)


input_field = tk.Entry(window, justify=tk.RIGHT)
input_field.grid(row=1, columnspan=5, sticky='nwse')


button_0 = tk.Button(window, text="0", command=lambda: set_text("0"), width=10)
button_0.grid(row=5, column=1, columnspan=2, sticky='nwse')
button_1 = tk.Button(window, text="1", command=lambda: set_text("1"), width=4)
button_1.grid(row=4, column=1, sticky='nwse')
button_2 = tk.Button(window, text="2", command=lambda: set_text("2"), width=4)
button_2.grid(row=4, column=2, sticky='nwse')
button_3 = tk.Button(window, text="3", command=lambda: set_text("3"), width=4)
button_3.grid(row=4, column=3, sticky='nwse')
button_4 = tk.Button(window, text="4", command=lambda: set_text("4"), width=4)
button_4.grid(row=3, column=1, sticky='nwse')
button_5 = tk.Button(window, text="5", command=lambda: set_text("5"), width=4)
button_5.grid(row=3, column=2, sticky='nwse')
button_6 = tk.Button(window, text="6", command=lambda: set_text("6"), width=4)
button_6.grid(row=3, column=3, sticky='nwse')
button_7 = tk.Button(window, text="7", command=lambda: set_text("7"), width=4)
button_7.grid(row=2, column=1, sticky='nwse')
button_8 = tk.Button(window, text="8", command=lambda: set_text("8"), width=4)
button_8.grid(row=2, column=2, sticky='nwse')
button_9 = tk.Button(window, text="9", command=lambda: set_text("9"), width=4)
button_9.grid(row=2, column=3, sticky='nwse')

button_plus = tk.Button(window, text="+", command=lambda: set_text("+"), width=4)
button_plus.grid(row=2, column=4, sticky='nwse')
button_minus = tk.Button(window, text="-", command=lambda: set_text("-"), width=4)
button_minus.grid(row=3, column=4, sticky='nwse')
button_equals = tk.Button(window, text="=", command=equals, width=4)
button_equals.grid(rowspan=2, row=4, column=4, sticky='nwse')
button_clear = tk.Button(window, text="C", command=clear, width=4, background="#E0FFFF")
button_clear.grid(row=5, column=3, sticky='nwse')

window.mainloop()

