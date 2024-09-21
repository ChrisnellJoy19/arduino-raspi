import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class RetrievalCompartmentForm(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg='#f0f0f0', highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        title_frame = tk.Frame(self, bg='#333', width=800, height=60)
        title_frame.place(x=0, y=0)
        title_label = tk.Label(title_frame, text="RETRIEVE COMPARTMENT SELECTION", font=("Segoe UI", 24, 'bold'), fg='white', bg='#333')
        title_label.place(x=170, y=10)
        title_icon = tk.Label(title_frame, image=self.root.retrieve_icon, bg='#333')
        title_icon.place(x=110, y=10)

        # Compartments
        self.rectangles = []
        self.compartment_status = []
        self.default_color = "#B3B3B3"
        self.occupied_color = "#ef4444"
        self.available_color = "#22c55e"
        self.selected_color = "#4CAF50"

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

        self.create_line(0, 90, 800, 90, fill="#333", width=2)

        # Update the message text to include instructions
        self.create_text(400, 110, text="Please select the compartment to retrieve your item from.", font=("Segoe UI", 16), fill="#333")

        # Add a button to navigate back
        back_button = tk.Button(self, text="Back", font=("Segoe UI", 16), fg='white', bg='#333', command=self.back_button_click)
        back_button.place(x=50, y=400)
 

        self.bind("<Button-1>", self.rectangle_click)

    def rectangle_click(self, event):
        item = self.find_withtag("current")[0]
        if item in self.rectangles:
            item_index = self.rectangles.index(item) + 1

            if self.compartment_status[self.rectangles.index(item)] != "unavailable":
                if messagebox.showerror("Vacant Compartment", f"Compartment no. {item_index} is vacant!"):
                    return
                
            # Ask the user if they want to proceed
            proceed = messagebox.askyesno(f"Compartment no. {item_index}",
                                        f"Do you want to retrieve from Compartment no. {item_index}?")
            
            compartment = item_index
            otp = self.root.memory['retrieve']['otp']
            self.root.memory['retrieve']['compartment'] = str(compartment)

            if proceed:
                otp_valid = self.root.machine.validate_otp(str(compartment), otp)
                if not otp_valid:
                    messagebox.showerror("Incorrect OTP", "The OTP you entered is not correct!")
                    return
                
                if not self.root.debug:
                    self.root.machine.compartments[str(compartment)].turn_on_relay()
                print("Compartment relay turned on")

                self.root.machine.release_item(str(compartment), otp)
                message = f"You unlocked Compartment no. {item_index}"
                messagebox.showinfo(f"Compartment no. {item_index}", message)
                self.root.show_confirm_retrieval_page() 
            else:
                print("User chose not to retrieve the item")

    def back_button_click(self):
        print("Back button clicked")
        # Ensure that the root has the method for showing the previous page
        self.root.show_previous_page()