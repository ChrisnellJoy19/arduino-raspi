import tkinter as tk
from tkinter import scrolledtext

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

        title_label = tk.Label(title_frame, text="DROP-OFF", font=("Georgia", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=350, y=15)
        title_icon = tk.Label(title_frame, image=self.root.dropoff_icon, bg='#333')
        title_icon.place(x=250, y=10)

        self.create_text(410, 140, text="Select Item Size:", font=("Helvetica", 18, 'bold'), fill="#333333")

        # Create buttons for different sizes
        self.create_button_with_icon(100, 180, "Extra Small", root.personal_belongings_icon, self.extra_small_size_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(320, 180, "Small", root.personal_belongings_icon, self.small_size_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(540, 180, "Medium", root.electronic_devices_icon, self.medium_size_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(100, 300, "Large", root.academic_icon, self.large_size_action, '#FFFFFF', '#333333')
        self.create_button_with_icon(320, 300, "Extra Large", root.packages_icon, self.extra_large_action, '#FFFFFF', '#333333')

        # Create a ScrolledText widget to display the description (initially hidden)
        self.description_text_box = scrolledtext.ScrolledText(self, width=60, height=8, wrap=tk.WORD, font=("Helvetica", 12))
        self.description_text_box.place(x=100, y=180)
        self.description_text_box.config(state=tk.DISABLED)  # Initially set as disabled to prevent editing
        self.description_text_box.place_forget()  # Hide it initially

        # Create a "Select" button (initially hidden)
        self.select_button = tk.Button(self, text="Select", font=("Helvetica", 14), command=self.select_button_click)
        self.select_button.place(x=600, y=350)
        self.select_button.place_forget()  # Hide it initially

        # Create an "X" button at the top-right of the description box (initially hidden)
        self.close_button = tk.Button(self, text="X", font=("Helvetica", 14), command=self.close_button_click, fg="white", bg="red", width=2, height=1)
        self.close_button.place(x=650, y=150)  # Positioned at the top-right of the description box
        self.close_button.place_forget()  # Hide it initially

        # Corrected back button functionality
        back_button = tk.Button(self, text="Cancel", font=("Segoe UI", 16), fg='white', bg='#333', command=self.back_button_click)
        back_button.place(x=50, y=420)

    def update_description(self, description):
        """Update the description text in the scrollable text box when a size is selected."""
        self.description_text_box.config(state=tk.NORMAL)  # Enable editing (temporarily)
        self.description_text_box.delete(1.0, tk.END)  # Clear previous text
        self.description_text_box.insert(tk.END, description)  # Insert the new description
        self.description_text_box.config(state=tk.DISABLED)  # Disable editing again

    def show_description_box(self):
        """Show the description box when a size is selected."""
        self.description_text_box.place(x=100, y=180)  # Make the description box visible
        self.description_text_box.lift()  # Ensure the text box is on top of other elements
        self.select_button.place(x=650, y=380)  # Show the Select button
        self.close_button.place(x=720, y=180)  # Show the "X" close button at the top-right of the description box

    def hide_description_box(self):
        """Hide the description box."""
        self.description_text_box.place_forget()  # Hide the description box
        self.select_button.place_forget()  # Hide the Select button
        self.close_button.place_forget()  # Hide the "X" button

    def extra_small_size_action(self):
        print("Extra Small Size Selected")
        description = """
        COMPARTMENT 5 & 6
        • Documents 
        • Laptop
        • Books/Notebooks
        • Clothes
        • Others fit in 12" x 9" x 3"
        """
        self.update_description(description)
        self.show_description_box()

    def small_size_action(self):
        print("Small Size Selected")
        description = """
        COMPARTMENT 3 & 4
        • Small Parcels
        • Small Boxes
        • Cup-sized items
        • Small Electronics (e.g., charger, accessories)
        • Clothes and Shoes
        • Others fit in 5" x 9" x 7"
        """
        self.update_description(description)
        self.show_description_box()

    def medium_size_action(self):
        print("Medium Size Selected")
        description = """
        COMPARTMENT 1 & 2
        • Medium-sized Parcels
        • Medium-sized Boxes
        • Books
        • Small Appliances (e.g., toaster, blender)
        • Electronics (e.g., small speaker, camera)
        • Clothes
        • Others fit in 12" x 9" x 7"
        """
        self.update_description(description)
        self.show_description_box()

    def large_size_action(self):
        print("Large Size Selected")
        description = """
        COMPARTMENT 7 & 8
        • Large Parcels 
        • Boxes
        • Large Bags (e.g., duffel bags, gym bags)
        • Others fit in 12" x 9" x 15"
        """
        self.update_description(description)
        self.show_description_box()

    def extra_large_action(self):
        print("Extra Large Size Selected")
        description = """
        COMPARTMENT 9
        • Luggage (e.g., suitcases, travel bags)
        • Larger Electronics (e.g. printers)
        • Large Bags (e.g., duffel bags, gym bags)
        • Others fit in 24" x 9" x 15"
        """
        self.update_description(description)
        self.show_description_box()

    def select_button_click(self):
        """Handler for the Select button click."""
        print("Select button clicked")
        self.hide_description_box()  # Hide description box and button
        self.root.show_drop_off_compartment_page()  # Proceed to next page

    def close_button_click(self):
        """Handler for the 'X' button click to close the description box."""
        print("Close (X) button clicked")
        self.hide_description_box()  # Hide the description box and Select button
        # Optionally reset any selected size or return to the size selection
        # (or just show the size selection options again)
        self.show_size_selection()

    def show_size_selection(self):
        """Optionally show size selection options again if the user closes the description box."""
        # This method is just a placeholder, you can reset state or re-enable size buttons here
        pass

    def create_button_with_icon(self, x, y, text, icon_image, command, bg_color, text_color):
        button_bg = create_rounded_rectangle(self, x, y, x + 180, y + 70, radius=15, fill=bg_color, outline='#CCCCCC', width=2)

        icon_x = x + 35
        icon_y = y + 35
        text_x = icon_x + 70
        text_y = icon_y

        
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

    def back_button_click(self):
        self.root.show_drop_off_input_details_page()  # This method will go back to the previous page
