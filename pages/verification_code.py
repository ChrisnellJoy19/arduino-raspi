import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont

class VerificationCode(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.pack(fill='both', expand=True)
        # Use the same background image as the WelcomePage
        self.bg_image = root.bg_image
        self.bg_label = tk.Label(self, image=self.bg_image)
        self.bg_label.pack(fill='both', expand=True)

        # Create the header
        header_frame = tk.Frame(self.bg_label, bg='#333')
        header_frame.pack(fill='x')

        icon_text_frame = tk.Frame(header_frame, bg = '#333')
        icon_text_frame.pack(pady=10)

        icon_label = tk.Label(icon_text_frame, image=self.root.retrieve_icon_sm, bg='#333')
        icon_label.pack(side='left', padx=10)

        header_label = tk.Label(icon_text_frame, text='RETRIEVE', font=('Arial', 24, 'bold'), fg='white', bg='#333')
        header_label.pack(side='left')

        # Correctly bind the back button to back_button_click
        back_button = tk.Button(self, text="Cancel", font=("Segoe UI", 16), fg='white', bg='#333', command=self.back_button_click)
        back_button.place(x=50, y=420)
        
        self.entry_frame = tk.Frame(self, bg=self.root.cget('bg'), highlightthickness=0)
        self.create_window(400, 120, window=self.entry_frame, anchor='center')
        tk.Label(self.entry_frame, text="Enter Verification Code:", font=('Vani', 20, 'bold'), fg='#333').pack(pady=5)
        self.code = tk.StringVar()
        self.entry = tk.Entry(self.entry_frame, textvariable=self.code, font=('Arial', 24), width=18, justify='center', highlightthickness=0, bd=2, bg='#fff', fg='#333')
        self.entry.pack(pady=5)

        keypad_frame = tk.Frame(self, bg='#f7f7f7', highlightthickness=0)
        self.create_window(400, 310, window=keypad_frame, anchor='center')
        self.create_keypad(keypad_frame)

    def create_rounded_button(self, frame, text, row, column, command=None):
        width, height = 70, 60
        radius = 10

        def draw_button(fill_color, text_color):
            image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(image)
            draw.rounded_rectangle((0, 0, width, height), radius, fill=fill_color, outline='#333', width=2)

            font = ImageFont.truetype("arial.ttf", 20)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
            text_x = (width - text_width) / 2
            text_y = (height - text_height) / 2
            draw.text((text_x, text_y), text, font=font, fill=text_color)

            return ImageTk.PhotoImage(image)

        normal_image = draw_button((105, 105, 105, 255), 'white')
        pressed_image = draw_button((169, 169, 169, 255), 'black')

        button = tk.Label(frame, image=normal_image, bd=0, bg=self.root.cget('bg'))
        button.image = normal_image

        def on_press(event):
            button.config(image=pressed_image)

        def on_release(event):
            button.config(image=normal_image)
            if command:
                command()

        button.bind("<Button-1>", on_press)
        button.bind("<ButtonRelease-1>", on_release)
        button.grid(row=row, column=column, padx=10, pady=5)

    def create_keypad(self, frame):
        buttons = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('0', 3, 1), ('Clear', 3, 0), ('Done', 3, 2)
        ]

        for (text, row, column) in buttons:
            if text == 'Clear':
                self.create_rounded_button(frame, text, row, column, command=lambda: self.entry.delete(0, tk.END))
            elif text == 'Done':
                self.create_rounded_button(frame, text, row, column, command=self.on_done)
            else:
                self.create_rounded_button(frame, text, row, column, command=lambda t=text: self.entry.insert(tk.END, t))

    def on_done(self):
        otp = self.code.get()
        self.root.memory['retrieve']['otp'] = otp
        print(f"OTP entered: {otp}")
        self.root.show_retrieval_compartment_page()

    def back_button_click(self):
        print("Back button clicked")
        self.root.show_menu_page()
