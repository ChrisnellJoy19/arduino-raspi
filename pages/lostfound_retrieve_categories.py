import tkinter as tk
from tkinter import simpledialog, messagebox

class LostRetrieveForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='#f0f0f0', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Background image
        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)
   
        title_frame = tk.Frame(self, bg='#333', width=800, height=60)
        title_frame.place(x=0, y=0)

        title_label = tk.Label(title_frame, text="RETRIEVE", font=("Georgia", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=350, y=15)
        title_icon = tk.Label(title_frame, image=self.root.retrieve_icon, bg='#333')
        title_icon.place(x=250, y=10)

        form_frame = tk.Frame(self, bg='white', width=600, height=380, highlightbackground='gray', highlightthickness=1)
        form_frame.place(x=100, y=80)
        form_title_label = tk.Label(form_frame, text='Select the right category for the item.', font=('Cambria', 16, 'bold'), fg='#333', bg='#FFFFFF')
        form_title_label.place(x=80, y=20)
        
        submit_button = tk.Button(form_frame, text="Submit", font=('Cambria', 14, 'bold' ), fg='white', bg='#333', command=self.submit_form)
        submit_button.place(x=250, y=300)

        # Dictionary for categories
        self.categories = {
            "Academic Materials": ["Books", "Notebooks", "Calculator", "Documents", "Other/s"],
            "Electronic Devices": ["Laptops", "Smartphones", "Tablet", "USB Drives", "Chargers & Cables", "Headphones", "Other/s"],
            "ID's and Finance": ["Money", "Wallet", "Student ID Card", "Driver's License", "Credit/Debit Card", "Passport", "Other/s"],
            "Clothing & Accessories": ["Headwear", "Eyewear", "Watches", "Necklace or Bracelets", "Umbrellas", "Other/s"],
            "Bags and Containers": ["Backpack", "Handbag", "Tote", "Other/s"],
            "Health & Personal Care": ["Toiletries", "Makeup", "First Aid Kit" "Other/s"],
        }

        self.subcategories = {
            "Books": ["Red", "Blue", "Green", "Yellow", "Black", "White", "Other/s"],
            "Notebooks": ["Red", "Blue", "Green", "Yellow", "Black", "White", "Other/s"],
            "Calculator": ["Red", "Blue", "Green", "Yellow", "Black", "White", "Other/s"],
            "Documents": ["Long Paper", "Short Paper"],
            "Laptops": ["Apple", "Dell", "HP", "Lenovo", "ASUS", "Acer", "Other/s"],
            "Smartphones": ["Apple", "Samsung", "Oppo", "Vivo", "Other/s"],
            "Tablet": ["Apple", "Samsung", "Huawei", "Xiaomi", "Other/s"],
            "USB Drives": ["Flash Drive", "External Hard Drive", "SSD", "Other/s"],
            "Chargers & Cables": ["Headphones Charger", "Power Adapter", "Micro USB Cable", "Other/s"],
            "Headphones": ["Bluetooth Headphones", "Wired Headphones", "Earbuds", "Other/s"],
            "Money": ["50-100", "100-200", "250-300", "350-400", "450-500", "550-900", "1000-1500", "1600-2000", "2500-3000", "more than 3000"],
            "Wallet": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "White", "Other/s"],
            "Headwear": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "White", "Other/s"],
            "Eyewear": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "White", "Other/s"],
            "Watches": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "Silver", "Other/s"],
            "Necklace or Bracelets": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "Silver", "Other/s"],
            "Umbrellas": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "Silver", "Other/s"],
            "Backpack": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "Silver", "Other/s"],
            "Handbag": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "Silver", "Other/s"],
            "Tote": ["Red", "Blue", "Green", "Black", "Yellow/Gold", "Silver", "Other/s"],
            "Toiletries": ["Small", "Medium", "Large"],
            "Makeup": ["Mascara", "Foundation", "Concealer", "Blush", "Pencil", "Lipstick", "Eye Shadow", "Make-up Set", "Other/s"],
            "First Aid Kit": ["First Aid Box", "Nursing/Medicine Bag", "Other/s"]

        
        }

        # Dropdown variables
        self.selected_category = tk.StringVar()
        self.selected_subcategory = tk.StringVar()
        self.selected_detail = tk.StringVar()

        # Category Dropdown
        category_label = tk.Label(form_frame, text="Select Category:", font=('Cambria', 14), fg='#333', bg='#FFFFFF')
        category_label.place(x=100, y=70)
        self.category_menu = tk.OptionMenu(form_frame, self.selected_category, *self.categories.keys(), command=self.update_subcategories)
        self.category_menu.config(width=20)
        self.category_menu.place(x=300, y=70)

        # Subcategory Dropdown
        subcategory_label = tk.Label(form_frame, text="Select Subcategory:", font=('Cambria', 14), fg='#333', bg='#FFFFFF')
        subcategory_label.place(x=100, y=130)
        self.subcategory_menu = tk.OptionMenu(form_frame, self.selected_subcategory, "")
        self.subcategory_menu.config(width=20)
        self.subcategory_menu.place(x=300, y=130)

        # Detail Dropdown
        detail_label = tk.Label(form_frame, text="Select Detail:", font=('Cambria', 14), fg='#333', bg='#FFFFFF')
        detail_label.place(x=100, y=190)
        self.detail_menu = tk.OptionMenu(form_frame, self.selected_detail, "")
        self.detail_menu.config(width=20)
        self.detail_menu.place(x=300, y=190)

    def update_subcategories(self, selected_category):
        subcategories = self.categories.get(selected_category, [])
        self.selected_subcategory.set('')  
        menu = self.subcategory_menu["menu"]
        menu.delete(0, "end")

        for sub in subcategories:
            menu.add_command(label=sub, command=lambda value=sub: self.subcategory_selected(value))

        self.selected_detail.set('')
        self.update_details('')

    def subcategory_selected(self, selected_subcategory):
        self.selected_subcategory.set(selected_subcategory)

        if selected_subcategory == "Other/s":
            other_detail = simpledialog.askstring("Input", "Please specify the item:")
            if other_detail:
                self.selected_subcategory.set(f"Other/s ({other_detail})")
                self.update_details(f"Other/s ({other_detail})")
        else:
            self.update_details(selected_subcategory)

    def update_details(self, selected_subcategory):
        self.detail_menu.config(state='normal')

        if selected_subcategory.startswith("Other/s"):
            self.detail_menu.config(state='disabled')
            self.selected_detail.set('Proceed to Next') 
        elif selected_subcategory in ["Student ID Card", "Driver's License", "Credit/Debit Card", "Passport"]:
            full_name = simpledialog.askstring("Input", f"Please enter the full name for the {selected_subcategory}:")
            if full_name:
                self.selected_detail.set(f"Name: {full_name}")
            self.detail_menu.config(state='disabled')  
        else:
            details = self.subcategories.get(selected_subcategory, [])
            self.selected_detail.set('')  
            menu = self.detail_menu["menu"]
            menu.delete(0, "end")

            for detail in details:
                menu.add_command(label=detail, command=lambda value=detail: self.detail_selected(value))

    def detail_selected(self, selected_detail):
        self.selected_detail.set(selected_detail)
        if selected_detail == "Other/s":
            specific_detail = simpledialog.askstring("Input", "Please specify the detail:")
            if specific_detail:
                self.selected_detail.set(f"Other/s ({specific_detail})")

    def submit_form(self):
        if not self.selected_category.get():
            messagebox.showerror("Error", "Please select a category")
            return
        if not self.selected_subcategory.get():
            messagebox.showerror("Error", "Please select a subcategory")
            return
        if not self.selected_detail.get():
            messagebox.showerror("Error", "Please select a detail")
            return
        
        messagebox.showinfo("Success", "Your item will be retrieved!")
        print(f"Category: {self.selected_category.get()}, Subcategory: {self.selected_subcategory.get()}, Detail: {self.selected_detail.get()}")

        self.root.show_lostfound_retrieval_compartment_page()