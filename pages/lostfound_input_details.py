import tkinter as tk
from tkinter import messagebox

class LostFoundForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='#f0f0f0', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Background image
        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        # Title frame
        title_frame = tk.Frame(self, bg='#333', width=800, height=60)
        title_frame.place(x=0, y=0)

        # Title text and icon
        title_label = tk.Label(title_frame, text="UNILOCK", font=("Georgia", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=320, y=10)
        title_icon = tk.Label(title_frame, image=self.root.lost_found_icon, bg='#333')
        title_icon.place(x=250, y=10)

        # Form frame
        form_frame = tk.Frame(self, bg='white', width=600, height=380, highlightbackground='gray', highlightthickness=1)
        form_frame.place(x=100, y=80)

        # Form title
        form_title_label = tk.Label(form_frame, text='LOST & FOUND', font=('Cambria', 18, 'bold'), fg='#333', bg = '#FFFFFF')
        form_title_label.place(x=205, y=20)

        # Name label and entry
        name_label = tk.Label(form_frame, text='Enter your name:', font=('Cambria', 14), fg='#333', bg = '#FFFFFF')
        name_label.place(x=50, y=60)
        self.name_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.name_entry.place(x=70, y=90)

        # Contact number label and entry
        contact_label = tk.Label(form_frame, text='Contact No.:', font=('Cambria', 14), fg='#333', bg = '#FFFFFF')
        contact_label.place(x=50, y=120)

        self.contact_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.contact_entry.place(x=70, y=150)
        self.contact_entry.insert(0, '+639')  # Automatically insert +639

        # Bind event to restrict editing of +639
        self.contact_entry.bind("<KeyRelease>", self.validate_prefix)

        # Button frame
        button_frame = tk.Frame(form_frame, bg='white')
        button_frame.place(x=30, y=220)

        # Back button
        def on_back():
            self.root.show_menu_page()  

        back_button = tk.Button(button_frame, text='Back', bg='white', fg='#333', font=('Cambria', 12), command=on_back, highlightbackground='gray', highlightthickness=1)
        back_button.pack(side=tk.LEFT, padx=120)

        # Next button (to validate inputs)
        next_button = tk.Button(button_frame, text='Next', bg='white', fg='#333', font=('Cambria', 12), command=self.validate_inputs, highlightbackground='gray', highlightthickness=1)
        next_button.pack(side=tk.LEFT, padx=75)

    def validate_prefix(self, event):
        """Ensure the contact number always starts with +639 and restrict modification."""
        contact_text = self.contact_entry.get()

        
        if not contact_text.startswith('+639'):
            self.contact_entry.delete(0, tk.END)
            self.contact_entry.insert(0, '+639')

    def validate_inputs(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()

        if not name or not contact:
            messagebox.showerror("Error", "Please fill in all fields")
            return
        elif len(contact) <= 4 or not contact[4:].isdigit():  # Ensure digits follow +639
            messagebox.showerror("Error", "Contact number must be digits only and follow +639")
            return
        
        self.root.memory['lost_and_found']['name'] = name
        self.root.memory['lost_and_found']['contact'] = contact

        # Only proceed to the next page if validation passes
        self.root.show_lostfound_menu_page()