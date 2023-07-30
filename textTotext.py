from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk

# Style window
ctk.set_appearance_mode("System")
#ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def _init_(self):
        super()._init_()

        # initialize app
        self.title("Transivity")
        self.eval('tk::PlaceWindow . center')

        # Create Frame
        frame1 = ctk.CTkFrame(self, width=1200, height=600)
        frame1.grid()
        frame1.pack_propagate(False)

        # Switch Button Function
        def switchFunction(event):

            print("Switch Languages...")

        # Text-Text Translation
        def text_to_text(text, source, destination):
            translator = translator()

 # text = textbox
            # text = "Der Himmel ist blau und ich mag Bananen"
            # translation = translator.translate(text, dest='en')

            # originalLanguage = combobox1
            # destinationLanguage = combobox2

            translation = translator.translate(
                text, src=source, dest=destination)
            textbox1.set_val(translation)
            # textbox2 = translation
            # print(translation.text)

        # Translate Speech to Text
        def translateSpeech():
            print("Speech to Text...")

        # Translate Text to Text
        def translateText():
            text = textbox1.get()
            source = combobox1.get()
            destination = combobox2.get()

            text_to_text(text, source, destination)
            print("Text to Text...")

        # Translate From ComboBox
        languages = ["English", "Afrikaans", "Sesotho"]
        combobox1 = ctk.CTkComboBox(frame1, values=languages)
        combobox1.set("Translate From")
        combobox1.configure(justify='center')
        combobox1.place(anchor='nw', x=310, y=20)

        # Translate To ComboBox
        combobox2 = ctk.CTkComboBox(frame1, values=languages)
        combobox2.set("Translate To")
        combobox2.configure(justify='center')
        combobox2.place(anchor='ne', x=1010, y=20)

        # Translate From TextBox
        textbox1 = ctk.CTkTextbox(frame1,
                                  width=400,
                                  height=400,
                                  corner_radius=15)

        textbox1.place(anchor='s', x=390, y=470)

        # Translate To TextBox
        textbox2 = ctk.CTkTextbox(frame1,
                                  width=400,
                                  height=400,
                                  corner_radius=15)

        textbox2.place(anchor='s', x=940, y=470)

        # Defining images
        swap_horz_image_white = ctk.CTkImage(
            Image.open("Icons\swap_horiz_white.png"))

        mic_image_black = ctk.CTkImage(Image.open("Icons\mic_black.png"))

        text_fields_image_black = ctk.CTkImage(
            Image.open("Icons\_text_fields_black.png"))

        # Switch Language Button
        button_switch = ctk.CTkButton(frame1,
                                      image=swap_horz_image_white,
                                      text="",
                                      fg_color="transparent",
                                      hover=FALSE,
                                      command=switchFunction)

        button_switch.place(anchor='n', x=660, y=20)

        # Translate Speech to Text Left
        button_speech = ctk.CTkButton(frame1,
                                      image=mic_image_black,
                                      text="Mic",
                                      text_color="black",
                                      fg_color="white",
                                      corner_radius=10,
                                      hover=FALSE,
                                      command=translateSpeech)

        button_speech.place(anchor='s', x=100, y=320)

        # Translate Text to Text
        text_field_button = ctk.CTkButton(frame1,
                                          image=text_fields_image_black,
                                          text="Text",
                                          text_color="black",
                                          fg_color="white",
                                          corner_radius=10,
                                          hover=FALSE,
                                          command=translateText)

        text_field_button.place(anchor='s', x=100, y=180)


# run app
#if _name_ == "_main_":
    app = App()
    app.mainloop()