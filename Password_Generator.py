import random
import string
import tkinter as tk

def generate_password():
    try:
        length = int(length_entry.get())
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text="Password: " + password, fg="green")
        message_label.config(text="")
    except ValueError:
        message_label.config(text="Invalid input. Please enter a valid number.", fg="red", font=("Helvetica", 12))
        password_label.config(text="Password: ", fg="black")

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")


length_label = tk.Label(window, text="Enter the number of characters:", bg="#f2f2f2", fg="#333333", font=("Helvetica", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(window, font=("Helvetica", 12))
length_entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="#4CAF50", fg="#ffffff", font=("Helvetica", 12))
generate_button.pack(pady=10)

password_label = tk.Label(window, text="Password: ", fg="black", font=("Helvetica", 12))
password_label.pack()

message_label = tk.Label(window, text="", fg="red")
message_label.pack()

window.mainloop()
