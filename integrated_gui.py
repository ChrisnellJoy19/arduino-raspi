import tkinter as tk
from PIL import Image, ImageTk
from pages.welcome import WelcomePage
from pages.menu import MenuPage
from pages.verification_code import VerificationCode
from pages.retrieve_general_category import RetrieveGeneralCategoryForm
from pages.retrieval_compartment import RetrievalCompartmentForm
from pages.confirm_retrieval import ConfirmRetrieval
from pages.drop_off_input_details import DropOffForm
from pages.drop_off_general_category import DropoffGeneralCategoryForm
from pages.drop_off_compartment import DropOffCompartmentForm
from pages.drop_off_detection import ProceedDropOff
from pages.drop_off_finished import DropOffFinished

from machine import Machine

class Root(tk.Tk):

    # Initialize the GUI
    current_language = 'English'

    def __init__(self, machine: Machine, debug: bool = False):
        super().__init__()
        self.machine = machine
        self.debug = debug
        self.title('URS')
        self.geometry('800x480')
        self.resizable(False, False)
        
        # Initialize assets
        self.bg_image = ImageTk.PhotoImage(Image.open('assets/background.png').resize((800, 480)))
        self.tapscreen_icon = ImageTk.PhotoImage(Image.open('assets/tap-screen.png').resize((154, 125)))
        self.dropoff_icon = ImageTk.PhotoImage(Image.open('assets/drop_off_icon.png').resize((90, 50)))
        self.retrieve_icon = ImageTk.PhotoImage(Image.open('assets/retrieve_icon.png').resize((50, 40)))
        self.retrieve_icon_sm = ImageTk.PhotoImage(Image.open('assets/retrieve_icon.png').resize((30, 30)))
        self.lost_found_icon = ImageTk.PhotoImage(Image.open('assets/lost_found_icon.png').resize((50, 50)))
        self.academic_icon = ImageTk.PhotoImage(Image.open('assets/academic-icon.png').resize((30, 30)))
        self.packages_icon = ImageTk.PhotoImage(Image.open('assets/packages-icon.png').resize((30, 30)))
        self.personal_belongings_icon = ImageTk.PhotoImage(Image.open('assets/personal-belongings-icon.png').resize((30, 30)))
        self.electronic_devices_icon = ImageTk.PhotoImage(Image.open('assets/devices-icon.png').resize((30, 30)))
        self.others_icon = ImageTk.PhotoImage(Image.open('assets/others-icon.png').resize((30, 30)))
        self.confirm_retrieve_image = ImageTk.PhotoImage(Image.open('assets/confirm-retrieve.png').resize((200, 180)))
        self.proceed_drop_off = ImageTk.PhotoImage(Image.open('assets/drop_off_proceed.png').resize((200, 180)))
        self.finish_drop_off= ImageTk.PhotoImage(Image.open('assets/drop_off_finished.png').resize((200, 180)))
        self.back_button= ImageTk.PhotoImage(Image.open('assets/back_arrow.png').resize((30, 30)))
        self.back_button_id= ImageTk.PhotoImage(Image.open('assets/back_arrow.png').resize((30, 30)))

        # Initialize root memmap
        self.initial_memory = {
            'dropoff': {
                'compartment': '',
                'sender': '',
                'sender_contact': '',
                'receiver': '',
                'receiver_contact': '',
                'item': 'Placeholder',
                'item_category': '',
            },
            'retrieve': {
                'compartment': '',
                'otp': ''
            }
        }
        self.memory = self.initial_memory

        self.show_welcome_page()
        self.mainloop()

    def reset_memory(self):
        self.memory = self.initial_memory

    def show_welcome_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = WelcomePage(self)
        homepage.pack()

    def show_menu_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = MenuPage(self)
        homepage.pack()

    def show_verification_code_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = VerificationCode(self)
        homepage.pack()

    def show_retrieve_general_category_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = RetrieveGeneralCategoryForm(self)
        homepage.pack() 
        
    def show_retrieval_compartment_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = RetrievalCompartmentForm(self)
        homepage.pack()

    def show_confirm_retrieval_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = ConfirmRetrieval(self)
        homepage.pack()

    def show_drop_off_input_details_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = DropOffForm(self)
        homepage.pack()

    def show_drop_off_general_category_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = DropoffGeneralCategoryForm(self)
        homepage.pack()

    def show_drop_off_compartment_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = DropOffCompartmentForm(self)
        homepage.pack()

    def show_drop_off_detection_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = ProceedDropOff(self)
        homepage.pack()

    def show_drop_off_finished_page(self):
        for child in self.winfo_children():
            child.destroy()
        homepage = DropOffFinished(self)
        homepage.pack()


if __name__ == '__main__':
    machine = machine = Machine(port=None, debug=True)
    root = Root(machine=machine, debug=True)
