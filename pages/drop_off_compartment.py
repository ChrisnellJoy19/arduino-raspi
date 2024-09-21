import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class DropOffCompartmentForm(tk.Canvas):
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
        title_label = tk.Label(title_frame, text="DROP-OFF COMPARTMENT SELECTION", font=("Segoe UI", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=170, y=10)
        title_icon = tk.Label(title_frame, image=self.root.dropoff_icon, bg='#333')
        title_icon.place(x=80, y=10)

        # Compartments
        self.rectangles = []
        self.compartment_status = []
        self.default_color = "#B3B3B3"
        self.occupied_color = "#ef4444"
        self.available_color = "#22c55e"
        self.selected_color = "#4CAF50"

        # Create all rectangles with default color
        for i in range(9):
            x1 = 180 + (i % 3) * 160
            y1 = 130 + (i // 3) * 80
            if i == 9:
                x1 = 180 + 160
            x2 = x1 + 100
            y2 = y1 + 60

            status = self.root.machine.get_compartment_status(str(i+1))

            if status == "available":
                color = self.available_color
            elif status == "unavailable":
                color = self.occupied_color
            else:
                color = self.default_color

            rect = self.create_rectangle(x1, y1, x2, y2, fill=color, outline="#1D192B", width=2)
            self.rectangles.append(rect)
            self.compartment_status.append(status)
            self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(i + 1), font=("Segoe UI", 18), fill="white")

        # Add a separator line
        self.create_line(0, 90, 800, 90, fill="#333", width=2)

        # Update the message text to include instructions
        self.create_text(400, 110, text="Please select an available compartment to drop off your item.", font=("Segoe UI", 16), fill="#333")

 
        # Add a button to navigate back
        back_button = tk.Button(self, text="Back", font=("Segoe UI", 16), fg='white', bg='#333', command=self.back_button_click)
        back_button.place(x=50, y=420)

        self.bind("<Button-1>", self.rectangle_click)

    def rectangle_click(self, event):
        item = self.find_withtag("current")[0]
        if item in self.rectangles:
            item_index = self.rectangles.index(item) + 1
            current_color = self.itemcget(item, "fill")
            if self.compartment_status[self.rectangles.index(item)] != "available":
                if messagebox.showerror("Compartment Unavailable", f"Compartment no. {item_index} is not available!"):
                    return

            self.itemconfig(item, fill=self.occupied_color, outline="#1D192B") 
            message = f"You selected compartment no. {item_index}. Proceed?"

            # Ask if the user wants to proceed
            proceed = messagebox.askyesno(f"Compartment no. {item_index}", message)
            
            if proceed:
                # Navigate to the next page only if the user confirms
                print(f"Proceeding with compartment {item_index}")
                self.root.memory['dropoff']['compartment'] = item_index
                self.root.show_drop_off_detection_page()
            else:
                # Revert the color back to default if the user cancels
                print("User canceled, reverting color.")
                self.itemconfig(item, fill=current_color)
                    
    #hindi pa nagana back button
    def back_button_click(self):
        print("Back button clicked")
        self.root.show_previous_page()