import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ProceedDropOff(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='gray', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Load and display the background image
        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        # Coordinates and dimensions for the custom rectangle
        proceed_drop_off_x = 400
        proceed_drop_off_y = 270

        rect_width = 430
        rect_height = 300

        move_up_amount = 45
        rect_x1 = proceed_drop_off_x - rect_width // 2
        rect_y1 = proceed_drop_off_y - rect_height // 2 - move_up_amount
        rect_x2 = proceed_drop_off_x + rect_width // 2
        rect_y2 = proceed_drop_off_y + rect_height // 2 - move_up_amount


        # Create the rectangle
        custom_color = "#2C2C2C"
        self.rect = self.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=custom_color, outline="black")
        self.create_text(proceed_drop_off_x, rect_y1 + 30, text="PROCEED TO DROP OFF", font=("Georgia", 24), fill="white")
        self.proceed_drop_off_image = self.create_image(proceed_drop_off_x, proceed_drop_off_y, anchor='center', image=self.root.proceed_drop_off)

        custom_color = "#1E1E1E"
        label = tk.Label(self, text="Position the item close for accurate detection", font=("Arial", 14, 'italic'), bg="gray", fg=custom_color)
        label.place(x=220, y=385)

        
        self.tag_bind(self.rect, "<Button-1>", self.on_click)
        self.tag_bind(self.proceed_drop_off_image, "<Button-1>", self.on_click)
        
    def on_click(self, event=None):
        # compartment = self.root.memory['dropoff']['compartment']
        # if not self.root.debug:
        #     self.root.machine.compartments[str(compartment)].turn_on_relay()
        # print("Compartment relay turned on")

        if self.root.debug:
            print("Item Detected!")
        else:
            print("Detecting Item")
            while not self.root.machine.compartments[str(compartment)].item_detection():
                pass
            print("Item detected")

        self.itemconfig(self.rect, fill="#0D2646")
        messagebox.showinfo("Thank you!", "Detected.")
        
        # Show the next page
        self.root.show_drop_off_finished_page()

  