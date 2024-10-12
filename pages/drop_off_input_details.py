import tkinter as tk
from tkinter import messagebox

class DropOffForm(tk.Canvas):
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
        title_label = tk.Label(title_frame, text="DROP-OFF", font=("Georgia", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=350, y=15)
        title_icon = tk.Label(title_frame, image=self.root.dropoff_icon, bg='#333')
        title_icon.place(x=250, y=10)

        # Form frame
        form_frame = tk.Frame(self, bg='white', width=600, height=380, highlightbackground='gray', highlightthickness=1)
        form_frame.place(x=100, y=80)

        # Form title
        form_title_label = tk.Label(form_frame, text='Drop-Off Form', font=('Cambria', 18, 'bold'), fg='#333', bg = '#FFFFFF')
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
        self.contact_entry.bind("<KeyRelease>", self.validate_prefix)  # Ensure +639 is not modified

        # Receiver's name label and entry
        receiver_label = tk.Label(form_frame, text='Enter receiver\'s name:', font=('Cambria', 14), fg='#333',  bg = '#FFFFFF')
        receiver_label.place(x=50, y=180)
        self.receiver_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.receiver_entry.place(x=70, y=210)

        # Receiver's contact number label and entry
        receiver_contact_label = tk.Label(form_frame, text='Receiver\'s contact no.:', font=('Cambria', 14), fg='#333', bg = '#FFFFFF')
        receiver_contact_label.place(x=50, y=240)
        self.receiver_contact_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.receiver_contact_entry.place(x=70, y=270)
        self.receiver_contact_entry.insert(0, '+639')  # Automatically insert +639
        self.receiver_contact_entry.bind("<KeyRelease>", self.validate_prefix)  # Ensure +639 is not modified

        # Button frame
        button_frame = tk.Frame(form_frame, bg='white')
        button_frame.place(x=30, y=310)

        def on_back():
            self.root.show_menu_page()  # Go back to the menu page

        back_button = tk.Button(button_frame, text='Back', bg='white', fg='#333', font=('Cambria', 12), command=on_back, highlightbackground='gray', highlightthickness=1)
        back_button.pack(side=tk.LEFT, padx=120)

        # Next button (to validate inputs)
        next_button = tk.Button(button_frame, text='Next', bg='white', fg='#333', font=('Cambria', 12), command=self.validate_inputs, highlightbackground='gray', highlightthickness=1)
        next_button.pack(side=tk.LEFT, padx=75)

    def validate_prefix(self, event):
        """Ensure the contact number always starts with +639 and restrict modification."""
        contact_text = event.widget.get()

        # If the user tries to modify or delete +639, reset it
        if not contact_text.startswith('+639'):
            event.widget.delete(0, tk.END)
            event.widget.insert(0, '+639')

    def validate_inputs(self):
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        receiver = self.receiver_entry.get()
        receiver_contact = self.receiver_contact_entry.get()

        if not name or not contact or not receiver or not receiver_contact:
            messagebox.showerror("Error", "Please fill in all fields")
        elif len(contact) <= 4 or not contact[4:].isdigit() or len(receiver_contact) <= 4 or not receiver_contact[4:].isdigit():
            messagebox.showerror("Error", "Contact numbers must be digits only and follow +639")
        else:
            self.root.memory['dropoff']['sender'] = name
            self.root.memory['dropoff']['sender_contact'] = contact
            self.root.memory['dropoff']['receiver'] = receiver
            self.root.memory['dropoff']['receiver_contact'] = receiver_contact
            self.root.show_drop_off_general_category_page()