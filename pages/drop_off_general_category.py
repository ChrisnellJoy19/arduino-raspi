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
        
        self.create_text(410, 140, text="Select Item Details:", font=("Helvetica", 18, 'bold'), fill="#333333")

        # Create Buttons
        self.create_button_with_icon(100, 180, "Academic\nMaterials", root.academic_icon,
                                     self.academic_materials_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(320, 180, "Packages", root.packages_icon,
                                     self.packages_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(540, 180, "  Personal \nBelongings", root.personal_belongings_icon,
                                     self.personal_belongings_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(210, 300, "Electronic\n   Devices", root.electronic_devices_icon,
                                     self.electronic_devices_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(430, 300, "  Others \n(Specify):", root.others_icon,
                                     self.other_category_action, '#FFFFFF', '#333333')

    # def create_back_button(self):
    # # Create back button with arrow icon
    #     if self.arrow_icon:
    #         self.back_button = self.create_image(50, 50, anchor='nw', image=self.root.back_button)
    #         self.tag_bind(self.back_button_id, '<Button-1>', self.back_button_action)

    # def back_button_action(self, event):
    #     print("Back Button Clicked")
    #     self.root.show_previous_page()  # Replace this with your method to go back

    def academic_materials_action(self):
        print("Academic Materials Button Clicked")
        self.root.memory['dropoff']['item_category'] = 'Academic Material'
        self.root.show_drop_off_compartment_page()  

    def packages_action(self):
        print("Packages Button Clicked")  
        self.root.memory['dropoff']['item_category'] = 'Packages'
        self.root.show_drop_off_compartment_page() 

    def personal_belongings_action(self):
        print("Personal Belongings Button Clicked")  
        self.root.memory['dropoff']['item_category'] = 'Personal Belongings'
        self.root.show_drop_off_compartment_page() 

    def electronic_devices_action(self):
        print("Electronic Devices Button Clicked")  
        self.root.memory['dropoff']['item_category'] = 'Electronic Devices'
        self.root.show_drop_off_compartment_page() 

    def other_category_action(self):
        # Open a new window asking for specifics
        self.open_other_category_window()

    def open_other_category_window(self):
        # Create a pop-up window
        self.new_window = tk.Toplevel(self.root)
        self.new_window.geometry("400x200")
        self.new_window.title("Specify Other Item")
        
        # Label asking for input
        label = tk.Label(self.new_window, text="Please specify the item:", font=("Helvetica", 14))
        label.pack(pady=20)

        # Entry field for user input
        self.other_item_entry = tk.Entry(self.new_window, font=("Helvetica", 12))
        self.other_item_entry.pack(pady=10)

        # Confirm and Back buttons
        confirm_button = tk.Button(self.new_window, text="Confirm", font=("Helvetica", 12),
                                   command=self.confirm_other_item)
        confirm_button.pack(side='left', padx=40, pady=20)

        back_button = tk.Button(self.new_window, text="Back", font=("Helvetica", 12),
                                command=self.new_window.destroy)
        back_button.pack(side='right', padx=40, pady=20)

    def confirm_other_item(self):
        # Retrieve the entered item
        other_item = self.other_item_entry.get()

        if other_item:
            print(f"Other Category Item: {other_item}")
            self.root.memory['dropoff']['item_category'] = other_item
            self.new_window.destroy()  # Close the window after confirming
            self.root.show_drop_off_compartment_page()  # Continue to the next step
        else:
            # Prompt the user to enter a valid item if empty
            error_label = tk.Label(self.new_window, text="Please enter an item.", fg="red", font=("Helvetica", 12))
            error_label.pack()

    def create_button_with_icon(self, x, y, text, icon_image, command, bg_color, text_color):
        # Creating the button with rounded rectangle
        button_bg = create_rounded_rectangle(self, x, y, x + 180, y + 70, radius=15, fill=bg_color, outline='#CCCCCC', width=2)
        
        # Positioning icon and text
        icon_x = x + 35
        icon_y = y + 35
        text_x = icon_x + 70
        text_y = icon_y

        # Create icon and text
        icon = self.create_image(icon_x, icon_y, image=icon_image)
        button_text = self.create_text(text_x, text_y, text=text, font=("Helvetica", 12, "bold"), fill=text_color)
        
        # Button hover effect and click functionality
        def on_click(event=None):
            print(f"Button clicked: {text}")  
            command()

        # Bind click and hover effects
        for item in (button_bg, icon, button_text):
            self.tag_bind(item, '<Button-1>', on_click)
            self.tag_bind(item, '<Enter>', lambda e, bg=button_bg: self.itemconfig(bg, fill='#D5E4F3'))
            self.tag_bind(item, '<Leave>', lambda e, bg=button_bg: self.itemconfig(bg, fill=bg_color))

