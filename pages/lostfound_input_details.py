import tkinter as tk
from tkinter import messagebox

class LostFoundForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='#f0f0f0', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Variables for tracking keyboard state
        self.keyboard_frame = None
        self.active_entry = None
        self.form_frame = None  # Keep a reference to the form frame

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
        self.name_entry.bind("<FocusIn>", lambda event: self.show_keyboard(self.name_entry))

        # Contact number label and entry
        contact_label = tk.Label(form_frame, text='Contact No.:', font=('Cambria', 14), fg='#333', bg = '#FFFFFF')
        contact_label.place(x=50, y=120)

        self.contact_entry = tk.Entry(form_frame, width=40, font=('Cambria', 14), highlightbackground='gray', highlightthickness=1)
        self.contact_entry.place(x=70, y=150)
        self.contact_entry.insert(0, '+639')  # Automatically insert +639
        self.contact_entry.bind("<FocusIn>", lambda event: self.show_keyboard(self.contact_entry))

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

        # Bind a click event to the whole canvas
        self.bind("<Button-1>", self.hide_keyboard)

    def show_keyboard(self, entry_widget):
        """Display a custom on-screen keyboard at the bottom of the screen."""
        if self.keyboard_frame:
            self.keyboard_frame.destroy()

        self.active_entry = entry_widget
        self.keyboard_frame = tk.Frame(self.root, bg='lightgray')

        # Place keyboard at the bottom, centered
        self.keyboard_frame.place(x=2, y=300, width=800, height=180)

        keys = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '.', '@', '_', '-'
        ]

        # Set the layout parameters
        max_cols = 10  # Maximum number of columns for the keyboard layout

        # Configure columns and rows to have equal weight (to eliminate gaps)
        for i in range(max_cols):
            self.keyboard_frame.grid_columnconfigure(i, weight=1, uniform="equal")
        self.keyboard_frame.grid_rowconfigure(0, weight=1, uniform="equal")
        self.keyboard_frame.grid_rowconfigure(1, weight=1, uniform="equal")
        self.keyboard_frame.grid_rowconfigure(2, weight=1, uniform="equal")
        self.keyboard_frame.grid_rowconfigure(3, weight=1, uniform="equal")
        self.keyboard_frame.grid_rowconfigure(4, weight=1, uniform="equal")

        # Create the key buttons with reduced gaps
        for i, key in enumerate(keys):
            button = tk.Button(self.keyboard_frame, text=key, width=4, height=1,
                            command=lambda k=key: self.insert_text(k))
            button.grid(row=i // max_cols, column=i % max_cols, padx=0, pady=0, sticky="nsew")  # sticky="nsew" makes buttons stretch

        # Add the Spacebar and Backspace buttons in a new row below
        spacebar = tk.Button(self.keyboard_frame, text='Space', width=50, height=1, command=lambda: self.insert_text(' '))
        spacebar.grid(row=4, column=0, columnspan=5, pady=5, padx=0, sticky="nsew")  # Use sticky to make it fill the space

        backspace_button = tk.Button(self.keyboard_frame, text='Delete', width=50, height=1, command=self.delete_text)
        backspace_button.grid(row=4, column=5, columnspan=5, pady=5, padx=0, sticky="nsew")  # Use sticky to make it fill the space

        # Reposition the form frame to stay above the keyboard
        #self.move_form_up()

    def hide_keyboard(self, event):
        """Hide the keyboard if clicking outside the active entry."""
        widget = event.widget
        if not isinstance(widget, tk.Entry) or widget != self.active_entry:
            if self.keyboard_frame:
                self.keyboard_frame.destroy()
                self.keyboard_frame = None
            #self.move_form_down()

    # def move_form_up(self):
    #     """Move the form frame up when the keyboard is visible."""
    #     self.form_frame.place(x=100, y=0)  # Move form up when keyboard appears

    # def move_form_down(self):
    #     """Move the form frame back down when the keyboard is hidden."""
    #     self.form_frame.place(x=100, y=80)  # Reset position after keyboard disappears

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