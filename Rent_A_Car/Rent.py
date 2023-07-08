from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import ImageTk, Image


class RentACarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rent a Car")
        self.root.geometry("800x500")

        # Krijimi i frame për foto
        self.photo_frame = Frame(self.root)
        self.photo_frame.pack(side=LEFT, pady=1)

        # Vendosja e fotos
        self.car_image = ImageTk.PhotoImage(Image.open("car_image.png"))
        self.car_label = Label(self.photo_frame, image=self.car_image)
        self.car_label.pack()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345677",
            database="rent_a_car"
        )
        self.cursor = self.db.cursor()

        self.create_tables()

        # Krijimi i tabelave për automjetet dhe klientët
        self.car_frame = Frame(self.root)
        self.car_frame.pack(side=LEFT, padx=20)

        self.car_label = Label(self.car_frame, text="Automjetet", font=("Arial", 14, "bold"))
        self.car_label.pack(side=TOP, pady=10)

        self.car_tree = ttk.Treeview(self.car_frame, columns=("ID", "Marka", "Modeli", "Viti", "Targa", "Çmimi"), show="headings")
        self.car_tree.column("ID", width=30)
        self.car_tree.column("Marka", width=100)
        self.car_tree.column("Modeli", width=100)
        self.car_tree.column("Viti", width=50)
        self.car_tree.column("Targa", width=80)
        self.car_tree.column("Çmimi", width=70)
        self.car_tree.heading("ID", text="ID")
        self.car_tree.heading("Marka", text="Marka")
        self.car_tree.heading("Modeli", text="Modeli")
        self.car_tree.heading("Viti", text="Viti")
        self.car_tree.heading("Targa", text="Targa")
        self.car_tree.heading("Çmimi", text="Çmimi")
        self.car_tree.pack(side=TOP)

        self.customer_frame = Frame(self.root)
        self.customer_frame.pack(side=LEFT, padx=20)

        self.customer_label = Label(self.customer_frame, text="Klientet", font=("Arial", 14, "bold"))
        self.customer_label.pack(side=TOP, pady=10)

        self.customer_tree = ttk.Treeview(self.customer_frame, columns=("ID", "Emri", "Adresa", "Targa Automjetit", "Ditet", "Pagesa (EUR)"), show="headings")
        self.customer_tree.column("ID", width=30)
        self.customer_tree.column("Emri", width=100)
        self.customer_tree.column("Adresa", width=150)
        self.customer_tree.column("Targa Automjetit", width=100)
        self.customer_tree.column("Ditet", width=70)
        self.customer_tree.column("Pagesa (EUR)", width=100)
        self.customer_tree.heading("ID", text="ID")
        self.customer_tree.heading("Emri", text="Emri")
        self.customer_tree.heading("Adresa", text="Adresa")
        self.customer_tree.heading("Targa Automjetit", text="Targa Automjetit")
        self.customer_tree.heading("Ditet", text="Ditet")
        self.customer_tree.heading("Pagesa (EUR)", text="Pagesa (EUR)")
        self.customer_tree.pack(side=TOP)

        # Krijimi i etiketave dhe fushave të hyrjes për automjetet
        self.car_make_label = Label(self.car_frame, text="Marka e automjetit:")
        self.car_make_label.pack(side=TOP, pady=5)
        self.car_make_entry = Entry(self.car_frame)
        self.car_make_entry.pack(side=TOP, pady=5)

        self.car_model_label = Label(self.car_frame, text="Modeli i automjetit:")
        self.car_model_label.pack(side=TOP, pady=5)
        self.car_model_entry = Entry(self.car_frame)
        self.car_model_entry.pack(side=TOP, pady=5)

        self.car_year_label = Label(self.car_frame, text="Viti i automjetit:")
        self.car_year_label.pack(side=TOP, pady=5)
        self.car_year_entry = Entry(self.car_frame)
        self.car_year_entry.pack(side=TOP, pady=5)

        self.car_license_label = Label(self.car_frame, text="Targa e automjetit:")
        self.car_license_label.pack(side=TOP, pady=5)
        self.car_license_entry = Entry(self.car_frame)
        self.car_license_entry.pack(side=TOP, pady=5)

        self.car_price_label = Label(self.car_frame, text="Çmimi i automjetit:")
        self.car_price_label.pack(side=TOP, pady=5)
        self.car_price_entry = Entry(self.car_frame)
        self.car_price_entry.pack(side=TOP, pady=5)

        # Krijimi i etiketave dhe fushave të hyrjes për klientët
        self.customer_name_label = Label(self.customer_frame, text="Emri i klientit:")
        self.customer_name_label.pack(side=TOP, pady=5)
        self.customer_name_entry = Entry(self.customer_frame)
        self.customer_name_entry.pack(side=TOP, pady=5)

        self.customer_address_label = Label(self.customer_frame, text="Adresa e klientit:")
        self.customer_address_label.pack(side=TOP, pady=5)
        self.customer_address_entry = Entry(self.customer_frame)
        self.customer_address_entry.pack(side=TOP, pady=5)

        self.customer_car_license_label = Label(self.customer_frame, text="Targa e automjetit:")
        self.customer_car_license_label.pack(side=TOP, pady=5)
        self.customer_car_license_entry = Entry(self.customer_frame)
        self.customer_car_license_entry.pack(side=TOP, pady=5)

        self.customer_days_label = Label(self.customer_frame, text="Ditët:")
        self.customer_days_label.pack(side=TOP, pady=5)
        self.customer_days_entry = Entry(self.customer_frame)
        self.customer_days_entry.pack(side=TOP, pady=5)

        # Krijimi i frame për butonat e automjeteve
        self.car_buttons_frame = Frame(self.car_frame)
        self.car_buttons_frame.pack(side=TOP, pady=10)

        self.add_car_button = Button(self.car_buttons_frame, text="Shto", command=self.add_car, bg="green", fg="white")
        self.add_car_button.pack(side=LEFT, padx=5)

        self.delete_car_button = Button(self.car_buttons_frame, text="Fshi", command=self.delete_car, bg="red", fg="white")
        self.delete_car_button.pack(side=LEFT, padx=5)

        self.update_car_button = Button(self.car_buttons_frame, text="Përditëso", command=self.update_car, bg="blue", fg="white")
        self.update_car_button.pack(side=LEFT, padx=5)

        # Krijimi i frame për butonat e klientëve
        self.customer_buttons_frame = Frame(self.customer_frame)
        self.customer_buttons_frame.pack(side=TOP, pady=10)

        self.add_customer_button = Button(self.customer_buttons_frame, text="Shto", command=self.add_customer, bg="green", fg="white")
        self.add_customer_button.pack(side=LEFT, padx=5)

        self.delete_customer_button = Button(self.customer_buttons_frame, text="Fshi", command=self.delete_customer, bg="red", fg="white")
        self.delete_customer_button.pack(side=LEFT, padx=5)

        self.update_customer_button = Button(self.customer_buttons_frame, text="Përditëso", command=self.update_customer, bg="blue", fg="white")
        self.update_customer_button.pack(side=LEFT, padx=5)

        # Shfaqja e të dhënave fillestare në tabelat
        self.display_data("cars", self.car_tree)
        self.display_data("customers", self.customer_tree)

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cars (id INT AUTO_INCREMENT PRIMARY KEY, make VARCHAR(255), model VARCHAR(255), year INT, license_plate VARCHAR(255), price DECIMAL(10, 2))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), car_license_plate VARCHAR(255), days INT, payment DECIMAL(10, 2))")

    def display_data(self, table, tree):
        tree.delete(*tree.get_children())
        if table == "cars":
            self.cursor.execute("SELECT * FROM cars")
        elif table == "customers":
            self.cursor.execute("SELECT * FROM customers")
        data = self.cursor.fetchall()
        for row in data:
            tree.insert("", END, values=row)

    def add_car(self):
        make = self.car_make_entry.get()
        model = self.car_model_entry.get()
        year = self.car_year_entry.get()
        license_plate = self.car_license_entry.get()
        price = self.car_price_entry.get()

        if make and model and year and license_plate and price:
            query = "INSERT INTO cars (make, model, year, license_plate, price) VALUES (%s, %s, %s, %s, %s)"
            values = (make, model, year, license_plate, price)
            self.cursor.execute(query, values)
            self.db.commit()
            messagebox.showinfo("Sukses", "Automjeti u shtua me sukses!")
            self.car_make_entry.delete(0, END)
            self.car_model_entry.delete(0, END)
            self.car_year_entry.delete(0, END)
            self.car_license_entry.delete(0, END)
            self.car_price_entry.delete(0, END)
            self.display_data("cars", self.car_tree)
        else:
            messagebox.showwarning("Gabim", "Ju lutem plotësoni të gjitha fushat.")

    def delete_car(self):
        selected_item = self.car_tree.selection()
        if selected_item:
            car_id = self.car_tree.item(selected_item)["values"][0]
            query = "DELETE FROM cars WHERE id = %s"
            self.cursor.execute(query, (car_id,))
            self.db.commit()
            messagebox.showinfo("Sukses", "Automjeti u fshi me sukses!")
            self.display_data("cars", self.car_tree)
        else:
            messagebox.showwarning("Gabim", "Ju lutem zgjidhni një automjet nga tabela.")

    def update_car(self):
        selected_item = self.car_tree.selection()
        if selected_item:
            car_id = self.car_tree.item(selected_item)["values"][0]
            make = self.car_make_entry.get()
            model = self.car_model_entry.get()
            year = self.car_year_entry.get()
            license_plate = self.car_license_entry.get()
            price = self.car_price_entry.get()

            if make and model and year and license_plate and price:
                query = "UPDATE cars SET make = %s, model = %s, year = %s, license_plate = %s, price = %s WHERE id = %s"
                values = (make, model, year, license_plate, price, car_id)
                self.cursor.execute(query, values)
                self.db.commit()
                messagebox.showinfo("Sukses", "Automjeti u përditësua me sukses!")
                self.car_make_entry.delete(0, END)
                self.car_model_entry.delete(0, END)
                self.car_year_entry.delete(0, END)
                self.car_license_entry.delete(0, END)
                self.car_price_entry.delete(0, END)
                self.display_data("cars", self.car_tree)
            else:
                messagebox.showwarning("Gabim", "Ju lutem plotësoni të gjitha fushat.")
        else:
            messagebox.showwarning("Gabim", "Ju lutem zgjidhni një automjet nga tabela.")

    def add_customer(self):
        name = self.customer_name_entry.get()
        address = self.customer_address_entry.get()
        car_license_plate = self.customer_car_license_entry.get()
        days = self.customer_days_entry.get()

        if name and address and car_license_plate and days:
            query = "SELECT price FROM cars WHERE license_plate = %s"
            self.cursor.execute(query, (car_license_plate,))
            price_data = self.cursor.fetchone()
            if price_data:
                price = price_data[0]
                payment = float(days) * float(price)
                query = "INSERT INTO customers (name, address, car_license_plate, days, payment) VALUES (%s, %s, %s, %s, %s)"
                values = (name, address, car_license_plate, days, payment)
                self.cursor.execute(query, values)
                self.db.commit()
                messagebox.showinfo("Sukses", "Klienti u shtua me sukses!")
                self.customer_name_entry.delete(0, END)
                self.customer_address_entry.delete(0, END)
                self.customer_car_license_entry.delete(0, END)
                self.customer_days_entry.delete(0, END)
                self.display_data("customers", self.customer_tree)
            else:
                messagebox.showwarning("Gabim", "Automjeti nuk ekziston.")
        else:
            messagebox.showwarning("Gabim", "Ju lutem plotësoni të gjitha fushat.")

    def delete_customer(self):
        selected_item = self.customer_tree.selection()
        if selected_item:
            customer_id = self.customer_tree.item(selected_item)["values"][0]
            query = "DELETE FROM customers WHERE id = %s"
            self.cursor.execute(query, (customer_id,))
            self.db.commit()
            messagebox.showinfo("Sukses", "Klienti u fshi me sukses!")
            self.display_data("customers", self.customer_tree)
        else:
            messagebox.showwarning("Gabim", "Ju lutem zgjidhni një klient nga tabela.")

    def update_customer(self):
        selected_item = self.customer_tree.selection()
        if selected_item:
            customer_id = self.customer_tree.item(selected_item)["values"][0]
            name = self.customer_name_entry.get()
            address = self.customer_address_entry.get()
            car_license_plate = self.customer_car_license_entry.get()
            days = self.customer_days_entry.get()

            if name and address and car_license_plate and days:
                query = "SELECT price FROM cars WHERE license_plate = %s"
                self.cursor.execute(query, (car_license_plate,))
                price_data = self.cursor.fetchone()
                if price_data:
                    price = price_data[0]
                    payment = float(days) * float(price)
                    query = "UPDATE customers SET name = %s, address = %s, car_license_plate = %s, days = %s, payment = %s WHERE id = %s"
                    values = (name, address, car_license_plate, days, payment, customer_id)
                    self.cursor.execute(query, values)
                    self.db.commit()
                    messagebox.showinfo("Sukses", "Klienti u përditësua me sukses!")
                    self.customer_name_entry.delete(0, END)
                    self.customer_address_entry.delete(0, END)
                    self.customer_car_license_entry.delete(0, END)
                    self.customer_days_entry.delete(0, END)
                    self.display_data("customers", self.customer_tree)
                else:
                    messagebox.showwarning("Gabim", "Automjeti nuk ekziston.")
            else:
                messagebox.showwarning("Gabim", "Ju lutem plotësoni të gjitha fushat.")
        else:
            messagebox.showwarning("Gabim", "Ju lutem zgjidhni një klient nga tabela.")

root = Tk()
app = RentACarApp(root)
root.mainloop()
