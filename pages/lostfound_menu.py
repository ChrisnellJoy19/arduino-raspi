import tkinter as tk
from PIL import Image, ImageTk

class LostFoundMenuPage(tk.Frame):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.pack(fill='both', expand=True)

        # Use the same background image as the WelcomePage
        self.bg_image = root.bg_image
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.pack(fill='both', expand=True)

        # Create the header
        header_frame = tk.Frame(self.bg_label, bg='#333')
        header_frame.pack(fill='x')

        header_label = tk.Label(header_frame, text='UniLOCK', font=('Arial', 24, 'bold'), fg='white', bg='#333')
        header_label.pack(pady=20)

        # Create the menu options
        menu_frame = tk.Frame(self.bg_label, bg='')
        menu_frame.pack(fill='both', expand=True, pady=35)

        drop_off_button = tk.Button(menu_frame, text='Drop Off', font=('Arial', 18), fg='white', bg='#8B0A1A', width=20, height=3, command=self.drop_off_action)
        drop_off_button.pack(pady=20)

        retrieve_button = tk.Button(menu_frame, text='Retrieve', font=('Arial', 18), fg='white', bg='#8B0A1A', width=20, height=3, command=self.retrieve_action)
        retrieve_button.pack(pady=5)

        # Create the footer
        footer_frame = tk.Frame(self.bg_label, bg='#333')
        footer_frame.pack(fill='x')

        footer_label = tk.Label(footer_frame, text='Marinduque State University', font=('Arial', 12), fg='white', bg='#333')
        footer_label.pack(pady=10)


    def drop_off_action(self):
        # Replace with the actual method that shows the drop off page
        print("Drop Off button clicked")
        self.root.show_lostfound_dropoff_categories_page()

    def retrieve_action(self):
        print("Retrieve button clicked")
        self.root.show_lostfound_retrieve_categories_page()
    


