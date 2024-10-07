import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LostFoundDropOffFinished(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='gray', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Load and display the background image
        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        # Coordinates and dimensions for the custom rectangle
        drop_off_finished_x = 400
        drop_off_finished_y = 270

        rect_width = 430
        rect_height = 300

        move_up_amount = 45
        rect_x1 = drop_off_finished_x - rect_width // 2
        rect_y1 = drop_off_finished_y - rect_height // 2 - move_up_amount
        rect_x2 = drop_off_finished_x + rect_width // 2
        rect_y2 = drop_off_finished_y + rect_height // 2 - move_up_amount

        # Create the rectangle
        custom_color = "#2C2C2C"
        self.rect = self.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=custom_color, outline="black")
        self.create_text(drop_off_finished_x, rect_y1 + 30, text="DROP-OFF FINISHED", font=("Georgia", 24), fill="white")
        self.drop_off_finished_image = self.create_image(drop_off_finished_x, drop_off_finished_y, anchor='center', image=self.root.finish_drop_off)

        custom_color = "#1E1E1E"
        label = tk.Label(self, text="Click the button to lock the compartment.", font=("Arial", 14, 'italic'), bg="gray", fg=custom_color)
        label.place(x=220, y=385)

        self.tag_bind(self.rect, "<Button-1>", self.on_click)
        self.tag_bind(self.drop_off_finished_image, "<Button-1>", self.on_click)

    def on_click(self, event=None):
        compartment = self.root.memory['dropoff']['compartment']
        self.itemconfig(self.rect, fill="#0D2646")

        if not self.root.debug:
            self.root.machine.compartments[str(compartment)].turn_off_relay()
        print("Compartment relay turned off")
        # Show the next page
        self.root.show_welcome_page()
