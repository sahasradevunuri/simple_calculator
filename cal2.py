import tkinter as tk

def click(event):
    button_text = event.widget["text"]
    if button_text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("GUI Calculator")

entry = tk.Entry(root, width=40, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        b = tk.Button(root, text=btn, font=('Arial', 18), padx=20, pady=10)
        b.grid(row=i+1, column=j, sticky="nsew")
        b.bind("<Button-1>", click)

root.mainloop()
