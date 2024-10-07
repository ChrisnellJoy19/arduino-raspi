import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LostFoundDropOffCompartment(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='#f0f0f0', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        title_frame = tk.Frame(self, bg='#333', width=800, height=60)
        title_frame.place(x=0, y=0)

        title_label = tk.Label(title_frame, text="LOST & FOUND COMPARTMENT SELECTION", font=("Segoe UI", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=130, y=10)
        title_icon = tk.Label(title_frame, image=self.root.lost_found_icon, bg='#333')
        title_icon.place(x=70, y=10)

        # Compartments
        self.rectangles = []
        self.compartment_status = []
        self.default_color = "#cbd5e1"
        self.occupied_color = "#f87171"
        self.available_color = "#4ade80"
        self.selected_color = "#4CAF50"


        for i in range(9):
            x1 = 180 + (i % 3) * 160
            y1 = 150 + (i // 3) * 80
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
        self.create_text(400, 110, text="Please select an available compartment to drop off the item.", font=("Segoe UI", 16), fill="#333")

        # Add a button to navigate back
        back_button = tk.Button(self, text="Back", font=("Segoe UI", 16), fg='white', bg='#333', command=self.back_button_click)
        back_button.place(x=50, y=420)

        # Add the horizontal legend for compartment statuses below the rectangles
        self.create_legend()

        self.bind("<Button-1>", self.rectangle_click)

    def create_legend(self):
        # Legend
        legend_frame = tk.Frame(self, bg='#f0f0f0')
        legend_frame.place(x=180, y=420)  # Positioned below the rectangles

        # Available (green)
        green_box = tk.Label(legend_frame, bg=self.available_color, width=3, height=1)
        green_box.grid(row=0, column=0, padx=10)
        green_label = tk.Label(legend_frame, text="Available", font=("Segoe UI", 14), bg='#f0f0f0')
        green_label.grid(row=0, column=1, padx=10)

        # Occupied (red)
        red_box = tk.Label(legend_frame, bg=self.occupied_color, width=3, height=1)
        red_box.grid(row=0, column=2, padx=10)
        red_label = tk.Label(legend_frame, text="Occupied", font=("Segoe UI", 14), bg='#f0f0f0')
        red_label.grid(row=0, column=3, padx=10)

        # Under Maintenance (white)
        white_box = tk.Label(legend_frame, bg=self.default_color, width=3, height=1)
        white_box.grid(row=0, column=4, padx=10)
        white_label = tk.Label(legend_frame, text="Under Maintenance", font=("Segoe UI", 14), bg='#f0f0f0')
        white_label.grid(row=0, column=5, padx=10)

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
                self.root.memory['lost_and_found_dropoff']['compartment'] = item_index
                self.root.show_lostfound_dropoff_detection_page()
            else:
                # Revert the color back to default if the user cancels
                print("User canceled, reverting color.")
                self.itemconfig(item, fill=current_color)
            
        compartment = self.root.memory['lost_and_found_dropoff']['compartment']
        if not self.root.debug:
            self.root.machine.compartments[str(compartment)].turn_on_relay()
        print("Compartment relay turned on")

    def back_button_click(self):
        print("Back button clicked")
        self.root.show_lostfound_dropoff_categories_page()
