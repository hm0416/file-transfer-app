import tkinter as tk
window = tk.Tk()
window.title("File-Transfer Application")

send_btn = tk.Button( text="Send file to client!", width = 5, height = 1, bg = "#bb0000", fg = "white")
input_box = tk.Entry(bg="white", fg = "#bb0000", width = 48)

send_btn.pack()
input_box.pack()

input_box.insert(0, "Enter the name of the file you would like to transfer")

text = input_box.get()
print(text)

window.mainloop()