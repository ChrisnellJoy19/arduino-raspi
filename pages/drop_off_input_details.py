import tkinter as tk
from tkinter import messagebox

class DropOffForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='#f0f0f0', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Variables for tracking keyboard state
        self.keyboard_frame = None
        self.active_entry = None

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
        form_title_label = tk.Label(form_frame, text='Drop-Off Form', font=('Cambria', 18, 'bold'), fg='#333', bg='white')
        form_title_label.place(x=205, y=20)

        # Name label and entry
        sender_label = tk.Label(form_frame, text='Enter your name:', font=('Cambria', 14), fg='#333', bg='white')
        sender_label.place(x=50, y=60)
        self.sender_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.sender_entry.place(x=70, y=90)
        self.sender_entry.bind("<FocusIn>", lambda event: self.show_keyboard(self.sender_entry))

        # Contact number label and entry
        sender_contact_label = tk.Label(form_frame, text='Contact No.:', font=('Cambria', 14), fg='#333', bg='white')
        sender_contact_label.place(x=50, y=120)
        self.sender_contact_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.sender_contact_entry.place(x=70, y=150)
        self.sender_contact_entry.insert(0, '+639')  # Automatically insert +639
        self.sender_contact_entry.bind("<FocusIn>", lambda event: self.show_keyboard(self.sender_contact_entry))
        self.sender_contact_entry.bind("<KeyRelease>", self.validate_prefix)

        # Receiver's name label and entry
        receiver_label = tk.Label(form_frame, text='Enter receiver\'s name:', font=('Cambria', 14), fg='#333', bg='white')
        receiver_label.place(x=50, y=180)
        self.receiver_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.receiver_entry.place(x=70, y=210)
        self.receiver_entry.bind("<FocusIn>", lambda event: self.show_keyboard(self.receiver_entry))

        # Receiver's contact number label and entry
        receiver_contact_label = tk.Label(form_frame, text='Receiver\'s contact no.:', font=('Cambria', 14), fg='#333', bg='white')
        receiver_contact_label.place(x=50, y=240)
        self.receiver_contact_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.receiver_contact_entry.place(x=70, y=270)
        self.receiver_contact_entry.insert(0, '+639')  # Automatically insert +639
        self.receiver_contact_entry.bind("<FocusIn>", lambda event: self.show_keyboard(self.receiver_contact_entry))
        self.receiver_contact_entry.bind("<KeyRelease>", self.validate_prefix)


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

        # Bind a click event to the whole canvas
        self.bind("<Button-1>", self.hide_keyboard)

    def show_keyboard(self, entry_widget):
        """Display a custom on-screen keyboard at the bottom of the screen."""
        if self.keyboard_frame:
            self.keyboard_frame.destroy()

        self.active_entry = entry_widget
        self.keyboard_frame = tk.Frame(self.root, bg='lightgray')

        # Place keyboard at the bottom, centered
        self.keyboard_frame.place(x=2, y=250, width=800, height=230)

        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '.', '@', '_', '-'
        ]

        # Set the layout parameters
        max_cols = 10  # Maximum number of columns for the keyboard layout

        # Create the key buttons
        for i, key in enumerate(keys):
            button = tk.Button(self.keyboard_frame, text=key, width=4, height=2,
                               command=lambda k=key: self.insert_text(k))
            button.grid(row=i // max_cols, column=i % max_cols, padx=1, pady=1)

        # Add the Spacebar and Backspace buttons in a new row below
        spacebar = tk.Button(self.keyboard_frame, text='Space', width=50, height=1, command=lambda: self.insert_text(' '))
        spacebar.grid(row=4, column=0, columnspan=5, pady=5, padx=2)

        backspace_button = tk.Button(self.keyboard_frame, text='Delete', width=50, height=1, command=self.delete_text)
        backspace_button.grid(row=4, column=5, columnspan=5, pady=5, padx=2)

    def hide_keyboard(self, event):
        """Hide the keyboard if clicking outside the active entry."""
        widget = event.widget
        if not isinstance(widget, tk.Entry) or widget != self.active_entry:
            if self.keyboard_frame:
                self.keyboard_frame.destroy()
                self.keyboard_frame = None

    def insert_text(self, char):
        if self.active_entry:
            self.active_entry.insert(tk.END, char)

    def delete_text(self):
        if self.active_entry:
            current_text = self.active_entry.get()
            if current_text.startswith("+639") and len(current_text) <= 4:
                return
            self.active_entry.delete(len(current_text) - 1)

    def validate_prefix(self, event):
        if self.active_entry in [self.sender_contact_entry, self.receiver_contact_entry]:
            current_text = self.active_entry.get()
            if not current_text.startswith("+639"):
                self.active_entry.delete(0, tk.END)
                self.active_entry.insert(0, "+639")

    def validate_inputs(self):
        sender = self.sender_entry.get().strip()
        sender_contact = self.sender_contact_entry.get().strip()
        receiver = self.receiver_entry.get().strip()
        receiver_contact = self.receiver_contact_entry.get().strip()
        

        if not sender or not sender_contact or not receiver or not receiver_contact:
            messagebox.showerror("Invalid Input", "Please fill in all fields")
            return

        self.root.memory['dropoff']['sender'] = sender
        self.root.memory['dropoff']['sender_contact'] = sender_contact
        self.root.memory['dropoff']['receiver'] = receiver
        self.root.memory['dropoff']['receiver_contact'] = receiver_contact
        self.root.show_drop_off_general_category_page()
