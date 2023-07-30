from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, PhotoImage
import subprocess


directory = Path(__file__).parent
#CHANGE THE DIRECTORY BELOW!!!!
canvasFiles = directory / Path(r"C:\Users\OEM\Desktop\AI Project\build\assets")


def relative_to_assets(path: str) -> Path:
    return canvasFiles / Path(path)


screen = Tk()
 
screen.geometry("1220x1000")
screen.configure(bg = "#FFFFFF")
screen.title('Transivity Translation GUI')

canvas = Canvas(screen, bg = "#FAEBD7", height = 1000, width = 1400, highlightthickness = 0, bd=0, relief = "ridge")
canvas.place(x=0, y=0)


#Pictures
backgroundImg = PhotoImage(file=relative_to_assets("image_1.png"))
firstImg = canvas.create_image(712, 475, image=backgroundImg)

logo = PhotoImage(file=relative_to_assets("image_2.png"))
secondImg = canvas.create_image(55.0, 70.0, image=logo)

newimage = PhotoImage(file=relative_to_assets("c197fca1-1e6c-41eb-a196-b261f7bc72b8.png"))
wlb = canvas.create_image(1000.0, 340.0, image=newimage)



def runProgram():
    subprocess.call(['python', 'GUI.py'])



#BUTTON

TText = tk.StringVar()
TextSpeech_btn = tk.Button(screen, textvariable=TText, fg='white', height=2, width=15, bg='MediumPurple4', font=('Helvetica', 10, 'bold'), border=0, command=runProgram)
TText.set('Translate')
TextSpeech_btn.place(x=980, y=33, width=170, height=50)


#TOP & BOTTOM LINE
canvas.create_rectangle(-1.0, 120.0, 1440.0, 120.0,  fill="#4A424E", outline="")

canvas.create_rectangle(-1.0, 560.0, 1440.0, 560.0, fill="#4A424E", outline="")


#PAGE TEXTS
canvas.create_text(85.0, 45.0, anchor="nw", text="Transivity", fill="#FFFFFF", font=("Segoe Script", 40 * -1, 'italic')) 

canvas.create_text(64.0, 240.0, anchor="nw", text="Bringing Creativity to\n          Translation",
    fill="#FFFFFF", font=("Calibri", 55 * -1, 'bold'))

canvas.create_text(64.0, 400.0, anchor="nw", text="Addressing issues regarding Grammar use with reagrds to\n language-to-language translation with the help of TRANSIVITY",
    fill="thistle4", font=("Calibri", 17))

canvas.create_text(64.0, 670.0, anchor="sw", text="Contact Us\nProgramming                                             Graphical User Interface\nL. Radebe                                                 A. Nhlanhla\nTel: (011) 785 1005                                    Tel: (011) 992 1742\nradebel@gmail.com                                   angeln@gmail.com",
    fill="#FFFFFF", font=("Helvetica", 10))



screen.resizable(True, True)
screen.mainloop()
