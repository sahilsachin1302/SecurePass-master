from src.entropy import encode
from src.generate import password_generator
from src.score import checkSimilarity, TotalProbability
import tkinter
from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class ExampleApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("Password Utility")
        self.resizable(False, False)
        self.button = customtkinter.CTkButton(
            self, text="Check Password Strength", command=self.passStrength)
        self.button.pack(side="top", padx=10, pady=40)
        self.button1 = customtkinter.CTkButton(
            self, text="Generate Strong Password", command=self.passGenerate)
        self.button1.pack()

    def passStrength(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("600x350")
        window.title("Check Password Strength")
        window.resizable(False, False)

        def strength():
            username = my_entry.get()
            password = my_entry1.get()
            my_text.insert(
                END, f"The strength of password is {round(TotalProbability(encode(password), checkSimilarity(username, password)))} out of 100")

        my_font = customtkinter.CTkFont(family="Arial", size=18)
        my_labelframe = customtkinter.CTkFrame(window, corner_radius=10)
        my_labelframe.pack(pady=20)

        my_label = customtkinter.CTkLabel(
            my_labelframe, text="Enter Username", font=my_font)
        my_label.grid(row=0, column=0, padx=10, pady=10)
        my_entry = customtkinter.CTkEntry(my_labelframe, font=my_font)
        my_entry.grid(row=0, column=1, padx=10, pady=10)

        my_label1 = customtkinter.CTkLabel(
            my_labelframe, text="Enter Password", font=my_font)
        my_label1.grid(row=1, column=0, padx=10, pady=10)
        my_entry1 = customtkinter.CTkEntry(my_labelframe, font=my_font)
        my_entry1.grid(row=1, column=1, padx=10, pady=10)

        my_button = customtkinter.CTkButton(
            my_labelframe, text="Check the Password Strength", command=strength)
        my_button.grid(row=2, column=0, columnspan=2,  padx=10, pady=10)

        text_frame = customtkinter.CTkFrame(window, corner_radius=10)
        text_frame.pack(pady=10)

        my_text = Text(text_frame, padx=5, pady=5, width=60, height=5,
                       wrap=WORD, bd=0, bg="#292929", fg="silver", font=("Arial", 18))
        my_text.pack(pady=10, padx=10)
        window.mainloop()

    def passGenerate(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("600x350")
        window.title("Generate Strong Password")
        window.resizable(False, False)

        def generate():
            for i in range(10):
                my_text.insert(END, "{0}. {1}.\n".format(
                    i+1, password_generator()))

        my_font = customtkinter.CTkFont(family="Arial", size=18)

        text_frame = customtkinter.CTkFrame(window, corner_radius=10)
        text_frame.pack(pady=10)

        my_text = Text(text_frame, padx=5, pady=5, width=60, height=10,
                       wrap=WORD, bd=0, bg="#292929", fg="silver", font=("Arial", 18))

        my_text.pack(pady=10, padx=10)
        my_labelframe = customtkinter.CTkFrame(window, corner_radius=10)
        my_labelframe.pack(pady=20)

        my_button = customtkinter.CTkButton(
            my_labelframe, text="Generate the Strong Passwords", command=generate)
        my_button.grid(row=2, column=0, columnspan=2,  padx=10, pady=10)
        window.mainloop()


app = ExampleApp()
app.mainloop()
