from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter import ttk
import PyPDF2
import googletrans
from googletrans import LANGUAGES,Translator
from tkinter import messagebox
from PIL import Image, ImageTk
from textblob import TextBlob
import pyttsx3
import gtts
import os

"""Aplication Window"""
# Create the main application window
root = Tk()
root.title("Transivity")

window_height = 500
window_width = 1000
root.resizable(False, False)

if window_height == 500:
    root.overrideredirect(1)

def window_center():
	global screen_height, screen_width, x_cordinate, y_cordinate

	screenWidth = root.winfo_screenwidth()
	screenHeight = root.winfo_screenheight()
	x = int((screenWidth/2) - (window_width/2))
	y = int((screenHeight/2) - (window_height/2))
	root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))


"""File Paths"""
def rel_path(folderName, fileName):
    import os
    absolute_Path = os.path.dirname(__file__)
    relative_Path = folderName
    full_Path = os.path.join(absolute_Path, relative_Path)
    return full_Path + fileName

#pyglet.font.add_file(rel_path("Roboto_Condensed", "/RobotoCondensed-Regular.ttf"))

#Background Image for window
bg = PhotoImage(file = rel_path("assets", "/background.png"), width=1000, height= 500)
label1 = Label(root , image = bg)
label1.place(x= 0, y = 0)

"""Google Resources"""
# Google Translate API
translator = Translator()

# list of language names
languages = googletrans.LANGUAGES
language_list = list(languages.values())
del language_list[1:21]
del language_list[2:61]
del language_list[3:28]

"""Functions"""
# Translate text from one language to another
def textTranslation():
    txtTo.delete(1.0, END)
    
    # Get the selected original language and destination language
    originalLanguage = combo_From.get()
    destinationLanguage = combo_To.get()
    
    # Validate input
    if originalLanguage == "Translate From" or destinationLanguage == "Translate To":
        speakErrorText('Please select both source and destination languages.')
        return
    
    if not txtFrom.get(1.0, END).strip():
        speakErrorText('Please enter the text to be translated.')
        return
    
    #assigning language name from language code
    language_detected = detect_language(txtFrom.get(1.0, END))
    if language_detected != combo_From.get():
         speakErrorText('The text entered does not match the language selected')
    else: 
        try:
            # Perform translation
            for key, value in languages.items():
                if value == originalLanguage:
                    originalLanguage = key
            
            for key, value in languages.items():
                if value == destinationLanguage:
                    destinationLanguage = key
            
            text = TextBlob(txtFrom.get(1.0, END))
            text = text.translate(from_lang=originalLanguage, to=destinationLanguage)
            # Insert the translated text into the destination text box
            txtTo.insert(1.0, text)
            
        except Exception as e:
           speakErrorText('The selected language is the same as the desired language. Please select another language.')

#Converting text to speech
def text_to_speech(language, _text):

    speech = gtts.gTTS(text=_text, lang=language, slow=False)
    filename = "sound.mp3"
    speech.save(filename)
    os.system(filename)
 
#Detect language mismatch
def detect_language(text):
    translator = Translator()
    result = translator.detect(text)

    if result.lang == "en":
        return "english"
    elif result.lang == "af":
        return "afrikaans"
    else:
        return "sesotho"


# Switch languages
def switchLanguages():
    from_text = txtFrom.get(1.0, END)
    to_text = txtTo.get(1.0, END)

    txtFrom.delete(1.0, END)
    txtFrom.insert(1.0, to_text)
    txtTo.delete(1.0, END)
    txtTo.insert(1.0, from_text)
    
    from_language = combo_From.get()
    to_language = combo_To.get()

    combo_From.set(to_language)
    combo_To.set(from_language)



# Clear text boxes
def clear():
    txtFrom.delete("1.0", END)
    txtTo.delete("1.0", END)


# Open PDF file
def openFile():
    file = askopenfile(parent=root, mode='rb', title='Choose a file', filetype=[('Pdf file', '*.pdf')])
    if file:
        read_file = PyPDF2.PdfReader(file)
        page = read_file.pages[0]
        page_content = page.extract_text()
        txtFrom.insert("1.0", page_content)

# Bind Enter key to text Translation function
def enter_key_pressed(event):
    textTranslation()
    
def minimize_window():
    root.overrideredirect(0)
    root.resizable(True, True)  # Allow window resizing
    root.iconify()

def enlarge_window():
    root.overrideredirect(1)

def close_window():
    root.destroy()
 
engine = pyttsx3.init()
   
def speakErrorText(text):
    engine.say(text)
    engine.runAndWait()

#Extracts the language code from the language  
def extractLang(text):
    returnCode = ''
    if text == "english":
        returnCode = 'en'
    
    elif text == "afrikaans":
        returnCode = 'af'
    
    elif text == "sesotho":
        speakErrorText("The selected language not currently supported")  
    
    return returnCode
        
    
"""Buttons"""
# Load icons for buttons
swap_horz_image_white = ImageTk.PhotoImage(Image.open(rel_path("Icons","/swap_horiz_white.png")))
mic_image_black = ImageTk.PhotoImage(Image.open(rel_path("Icons", "/mic_black.png")))
speaker_image_black = ImageTk.PhotoImage(Image.open(rel_path("Icons","/Speaker_Icon2.png")))
text_fields_image_black = ImageTk.PhotoImage(Image.open(rel_path("Icons","/_text_fields_black.png")))
open_folder_icon_file = ImageTk.PhotoImage(Image.open(rel_path("Icons",'/open-folder-icon-file.png')))
clear_text_icon = ImageTk.PhotoImage(Image.open(rel_path("Icons", "/backspace.png")))
close_icon = ImageTk.PhotoImage(Image.open(rel_path("Icons", "/close.png" )))

# Translate From
combo_From = ttk.Combobox(root, values=language_list)
combo_From.set("Translate From")
combo_From.configure(justify='center')
combo_From.place(anchor='nw', x=230, y=60)
combo_From['state'] = 'readonly'

# Translate To
combo_To = ttk.Combobox(root, values=language_list)
combo_To.set("Translate To")
combo_To.configure(justify='center')
combo_To.place(anchor='ne', x=870, y=60)
combo_To['state'] = 'readonly'

# Translate From TextBox
txtFrom = Text(root, width=40, height=20, font=("RobotoCondensed-Regular", 10))
txtFrom.place(anchor='s', x=300, y=450)

# Translate To TextBox
txtTo = Text(root, width=40, height=20, font=("RobotoCondensed-Regular", 10))
txtTo.place(anchor='s', x=800, y=450)
#txtTo['state'] = 'readonly'

# Switch Language
button_switch = Button(root, image=swap_horz_image_white, text="", fg="white", bg="black", command=switchLanguages)
button_switch.place(anchor='n', x=550, y=50)

# Clear 
btn_Clear = Button(root, text="Clear", image=clear_text_icon, fg="black", command=clear, compound= LEFT, width= 70)
btn_Clear.place(anchor='s', x=80, y=345)


# Open PDF File Button
btn_openFile = Button(root, image=open_folder_icon_file, text=" file", fg="black", compound= LEFT, width= 70, command= openFile)
btn_openFile.place(anchor='sw', x=40,  y=185)

# Speech to Text Buttons
btn_Audio = Button(root, image=speaker_image_black, text=" Audio", fg="black", compound=LEFT, width=70,
                   command=lambda: text_to_speech(extractLang(combo_To.get()),txtTo.get(1.0, END)))
btn_Audio.place(anchor='s', x=80, y=265)

root.bind("<Return>", enter_key_pressed)

#btn_closeWindow = Button(root, image = close_icon, text="", fg="black",bg= "white", width= 24, height= 24)
#btn_closeWindow.place(anchor='ne', x = 980, y = 10)

#Control window
minimize_button = Button(root, text="-", width = 3, command=minimize_window, bg = "green")
minimize_button.place(anchor='ne', x = 900, y = 10)
enlarge_button = Button(root, text="+", width = 3, command=enlarge_window, bg = "yellow")
enlarge_button.place(anchor='ne', x = 940, y = 10)
close_button = Button(root, text="x", width = 3, command=close_window, bg = "red")
close_button.place(anchor='ne', x = 980, y = 10)

# Run the application
window_center()
root.mainloop()
