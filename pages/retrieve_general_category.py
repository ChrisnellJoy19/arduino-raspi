import tkinter as tk
from PIL import Image, ImageTk

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

class RetrieveGeneralCategoryForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='gray', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)
        self.create_text(420, 50, text="RETRIEVE", font=("Georgia", 24, 'bold'), fill="black")
        self.create_image(310, 50, anchor='center', image=self.root.retrieve_icon_sm)

        self.create_text(200, 100, text="Select Item Details:", font=("Georgia", 16, 'bold'), fill="black")

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

        # Creating buttons with rounded rectangles
        self.create_button_with_icon(140, 148, "Academic\nMaterials", root.academic_icon,
                                     self.academic_materials_action, '#FFFFFF', 'black')
        self.create_button_with_icon(360, 145, "Packages", root.packages_icon,
                                     self.packages_action, '#FFFFFF', 'black')
        self.create_button_with_icon(580, 148, "  Personal \nBelongings", root.personal_belongings_icon,
                                     self.personal_belongings_action, '#FFFFFF', 'black')
        self.create_button_with_icon(280, 278, "Electronic\n   Devices", root.electronic_devices_icon,
                                     self.electronic_devices_action, '#FFFFFF', 'black')
        self.create_button_with_icon(500, 278, "  Others \n(Specify):", root.others_icon,
                                     self.other_category_action, '#FFFFFF', 'black')

    def academic_materials_action(self):
        print("Academic Materials Button Clicked")  
        self.root.show_retrieval_compartment_page()
 
    def packages_action(self):
        print("Packages Button Clicked")  
        self.root.show_retrieval_compartment_page()

    def personal_belongings_action(self):
        print("Personal Belongings Button Clicked")  
        self.root.show_retrieval_compartment_page()

    def electronic_devices_action(self):
        print("Electronic Devices Button Clicked")  
        self.root.show_retrieval_compartment_page()

    def other_category_action(self):
        print("Other Category Button Clicked")  
        self.root.show_other_category_page()

    def create_button_with_icon(self, x, y, text, icon_image, command, bg_color, text_color):
        button_bg = create_rounded_rectangle(self, x, y, x + 180, y + 70, radius=15, fill=bg_color, outline='black')
        
        icon_x = x + 35
        icon_y = y + 35
        text_x = icon_x + 70
        text_y = icon_y

        icon = self.create_image(icon_x, icon_y, image=icon_image)
        button_text = self.create_text(text_x, text_y, text=text, font=("Helvetica", 12, "bold"), fill=text_color)
        
        def on_click(event=None):
            print(f"Button clicked: {text}")  
            command()

        for item in (button_bg, icon, button_text):
            self.tag_bind(item, '<Button-1>', on_click)
            self.tag_bind(item, '<Enter>', lambda e: self.itemconfig(button_bg, fill='lightblue'))
            self.tag_bind(item, '<Leave>', lambda e: self.itemconfig(button_bg, fill=bg_color))

