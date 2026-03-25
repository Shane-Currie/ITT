import tkinter as tk

def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_container.get())
    temp_convert = (fahrenheit-32) * 5/9
    result_var.set(temp_convert)

root = tk.Tk() 
root.title('Temp Convert')  
root.geometry("360x160")    

tk.Label(root, text="Fahrenhight:").grid(row=0, column=0, padx=8, pady=8, sticky="e")
fahrenheit_container = tk.StringVar()
entry_f = tk.Entry(root, width=12, textvariable = fahrenheit_container)
entry_f.grid(row=0, column=1, padx=8, pady=8, sticky="w")

tk.Button(root, text="Convert", command=fahrenheit_to_celsius).grid(row=0, column=2, padx=8, pady=8)

tk.Label(root, text="Celsius:").grid(row=1, column=0, padx=8, pady=8, sticky="e")
result_var = tk.StringVar(value="")
tk.Label(root, textvariable=result_var).grid(row=1, column=1, padx=8, pady=8, sticky="w")

status_var = tk.StringVar(value="")
tk.Label(root, textvariable=status_var, fg="green").grid(row=2, column=0, columnspan=3, pady=6)

root.columnconfigure(1, weight=1)
root.mainloop()


