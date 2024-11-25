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


class DropoffGeneralCategoryForm(tk.Canvas):
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

        self.create_text(410, 140, text="Select Item Size:", font=("Helvetica", 18, 'bold'), fill="#333333")

        # Create Buttons with Click to Show Specifications
        self.create_button_with_icon(100, 180, "Extra Small", root.personal_belongings_icon, self.extra_small_size_action, '#FFFFFF', '#333333', "Small size (up to 10kg, max 40x30x30 cm)")
        self.create_button_with_icon(320, 180, "Small", root.personal_belongings_icon, self.small_size_action, '#FFFFFF', '#333333', "Small size (up to 10kg, max 40x30x30 cm)")
        self.create_button_with_icon(540, 180, "Medium", root.electronic_devices_icon, self.medium_size_action, '#FFFFFF', '#333333', "Medium size (up to 20kg, max 50x40x40 cm)")
        self.create_button_with_icon(150, 300, "Large", root.academic_icon, self.large_size_action, '#FFFFFF', '#333333', "Large size (up to 30kg, max 60x50x50 cm)")
        self.create_button_with_icon(370, 300, "Extra Large", root.packages_icon, self.extra_large_action, '#FFFFFF', '#333333', "Extra Large (up to 50kg, max 80x60x60 cm)")

        # Back Button
        back_button = tk.Button(self, text="Back", font="Helvetica", command=self.back_button_click, bg='#333', fg='white')
        back_button.place(x=40, y=420)  # Positioning the back button

        # Track currently visible hover text box
        self.current_hover_text_box = None

    def extra_small_size_action(self):
        print("Extra Small Size Selected")
        self.root.show_drop_off_compartment_page()

    def small_size_action(self):
        print("Small Size Selected")
        self.root.show_drop_off_compartment_page()

    def medium_size_action(self):
        print("Medium Size Selected")
        self.root.show_drop_off_compartment_page()

    def large_size_action(self):
        print("Large Size Selected")
        self.root.show_drop_off_compartment_page()

    def extra_large_action(self):
        print("Extra Large Size Selected")
        self.root.show_drop_off_compartment_page()

    def create_button_with_icon(self, x, y, text, icon_image, command, bg_color, text_color, hover_text):
        button_bg = create_rounded_rectangle(self, x, y, x + 180, y + 70, radius=15, fill=bg_color, outline='#CCCCCC', width=2)

        icon_x = x + 35
        icon_y = y + 35
        text_x = icon_x + 70
        text_y = icon_y

        icon = self.create_image(icon_x, icon_y, image=icon_image)
        button_text = self.create_text(text_x, text_y, text=text, font=("Helvetica", 12, "bold"), fill=text_color)

        hover_text_box = tk.Label(self, text=hover_text, font=("Helvetica", 10), bg="#f0f0f0", fg="#333333", bd=1, relief="solid", width=30, height=2)
        hover_text_box.place_forget()  
     
        def on_click(event=None):
            print(f"Button clicked: {text}")
            if self.current_hover_text_box:
                self.current_hover_text_box.place_forget()

            hover_text_box.place(x=x + 10, y=y + 90)  

            self.current_hover_text_box = hover_text_box
            command()

        for item in (button_bg, icon, button_text):
            self.tag_bind(item, '<Button-1>', on_click)

    def back_button_click(self):
        """Function to go back to the drop-off input details page."""
        self.root.show_drop_off_input_details_page()  # Navigate back to the previous page
