import tkinter as tk
from PIL import Image, ImageTk

class OtherCategoryForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='gray', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)
        self.create_text(420, 35, text="RETRIEVE", font=("Georgia", 18), fill="black")
        self.create_image(340, 30, anchor='center', image=self.root.retrieve_icon_sm)

        # Positioning
        tap_screen_x = 800 / 2
        tap_screen_y = 480 / 2 - 20
        text_x = 800 / 2
        text_y = tap_screen_y + 60 + 20

        # Create the black inner border 80 pixels away from the text and icon
        border_padding = 100
        border_thickness = 2

        border_left = tap_screen_x - border_padding - 250  # Adjusting for width of the content
        border_right = tap_screen_x + border_padding + 250
        border_top = tap_screen_y - border_padding - 80  # Adjusting for height of the content
        border_bottom = text_y + border_padding + 40

        self.create_rectangle(border_left, border_top, 
                              border_right, border_bottom, 
                              outline='black', width=border_thickness)

        #self.create_text(170, 100, text="Select Item Details:", font=("Georgia", 16, 'bold'), fill="black")
        form_frame = tk.Frame(self, bg = 'gray', width = 420, height=320)
        form_frame.place(x=180, y=80)

        other_label = tk.Label(form_frame, text = 'Specify Item Detail/s: ', bg='gray', font=('Cambria, 14'))
        other_label.place(x=20, y=20)
        self.other_entry = tk.Entry(form_frame, width = 30, font=("Cambria", 14))
        self.other_entry.place(x=30, y=50)
        self.other_entry.insert(0, '')
        
        def on_enter(e):
            e.widget['background'] = 'light blue'

        def on_leave(e):
            e.widget['background'] = 'white'

        def on_back():
            self.root.show_general_category_page() 

        back_button = tk.Button(form_frame, text='Back', bg='white', fg='black', font=('Cambria', 12), command=on_back)
        back_button.place(x=130, y=280)
        back_button.bind("<Enter>", on_enter)
        back_button.bind("<Leave>", on_leave)

        next_button = tk.Button(form_frame, text='Next', bg='white', fg='black', font=('Cambria', 12))
        next_button.place(x=250, y=280)
        next_button.bind("<Enter>", on_enter)
        next_button.bind("<Leave>", on_leave)

        print("Next button clicked")
        self.root.show_retrieval_compartment_page()