import tkinter as tk

class WelcomePage(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, width=800, height=480, bg="#D3D3D3", highlightthickness=0, **kwargs)
        self.root = root
        self.place(x=0, y=0)

        # Positioning
        tap_screen_x = 800 / 2
        tap_screen_y = 480 / 2 - 20
        text_x = 800 / 2
        text_y = tap_screen_y + 60 + 20

        # Create the black inner border 80 pixels away from the text and icon
        border_padding = 100
        border_thickness = 2

        border_left = tap_screen_x - border_padding - 250  # Adjusting for width of the content
        border_right = tap_screen_x + border_padding + 250
        border_top = tap_screen_y - border_padding - 80  # Adjusting for height of the content
        border_bottom = text_y + border_padding + 40

        self.create_rectangle(border_left, border_top, 
                              border_right, border_bottom, 
                              outline='black', width=border_thickness)

        # Background image
        self.create_image(0, 0, anchor='nw', image=self.root.bg_image)

        # Icon in the center
        self.create_image(tap_screen_x, tap_screen_y, anchor='center', image=self.root.tapscreen_icon)

        # Text below the icon
        custom_color = "#1E1E1E"
        self.create_text(text_x, text_y, text="TAP ANYWHERE TO START", font=("Georgia", 22, 'bold'), fill=custom_color)

        self.bind("<Button-1>", self.on_screen_tap)

    def on_screen_tap(self, event):
        self.root.show_menu_page()
