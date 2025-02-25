import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LostFoundConfirmRetrieval(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='gray', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Load and display the background image
        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        # Coordinates and dimensions for the custom rectangle
        confirm_retrieve_x = 400
        confirm_retrieve_y = 270

        rect_width = 430
        rect_height = 300

        move_up_amount = 45
        rect_x1 = confirm_retrieve_x - rect_width // 2
        rect_y1 = confirm_retrieve_y - rect_height // 2 - move_up_amount
        rect_x2 = confirm_retrieve_x + rect_width // 2
        rect_y2 = confirm_retrieve_y + rect_height // 2 - move_up_amount

        # Create the rectangle
        custom_color = "#2C2C2C"
        self.rect = self.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill=custom_color, outline="black")
        self.create_text(confirm_retrieve_x, rect_y1 + 30, text="RETRIEVED", font=("Georgia", 24), fill="white")
        self.confirm_retrieve_image = self.create_image(confirm_retrieve_x, confirm_retrieve_y, anchor='center', image=self.root.confirm_retrieve_image)

        custom_color = "#1E1E1E"
        label = tk.Label(self, text="Click the button to lock the compartment", font=("Arial", 14, 'italic'), bg="gray", fg=custom_color)
        label.place(x=220, y=385)

        # Positioning
        tap_screen_x = 800 / 2
        tap_screen_y = 480 / 2 - 20
        text_x = 800 / 2
        text_y = tap_screen_y + 60 + 20

        self.tag_bind(self.rect, "<Button-1>", self.on_click)
        self.tag_bind(self.confirm_retrieve_image, "<Button-1>", self.on_click)

    def on_click(self, event=None):
        compartment = self.root.memory['lost_and_found_retrieve']['compartment']
        sender = self.root.memory['lost_and_found_dropoff']['sender']
        sender_contact = self.root.memory['lost_and_found_dropoff']['sender_contact']
        receiver = self.root.memory['lost_and_found_retrieve']['receiver']
        receiver_contact = self.root.memory['lost_and_found_retrieve']['receiver_contact']
        self.itemconfig(self.rect, fill="#0D2646")

        
        if not self.root.debug:
            self.root.machine.compartments[str(compartment)].turn_off_relay()
        print("Compartment relay turned off")
        
        msg = f'Hello {sender}, Thank you for using UniLOCK! Your item has been retrieved by {receiver}. For more details you can contact the receiver on {receiver_contact}'
        self.root.machine.send_message(sender_contact, msg)
        messagebox.showinfo("Thank you!", "The sender will be notified that the item has been retrieved.")
        
        msg = f'Hello {receiver}, Thank you for using UniLOCK! Your item was left by {sender}. For more details you can contact the sender on {sender_contact}'
        self.root.machine.send_message(receiver_contact, msg)
        # Show the next page
        self.root.show_welcome_page()
