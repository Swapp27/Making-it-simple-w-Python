import tkinter as converter
from tkinter import filedialog
from tkinter import messagebox
import tkinter.font as Tfont

from PIL import Image

window = converter.Tk()

ui = converter.Canvas(window, width=400, height=400, background='lightslateblue')
ui.pack()

lbl = converter.Label(window, text='PDF Converter', bg='lightslateblue', fg='black')
font = Tfont.Font(family='Times New Roman', weight='bold', slant='italic')
lbl.config(font=(font, 25, 'bold'))
ui.create_window(200, 50, window=lbl)

lbl1 = converter.Label(window, text='Created By Swapnil', bg='lightslateblue', fg='black')
lbl1.config(font=(font, 10, 'italic'))
ui.create_window(200, 380, window=lbl1)

def get():
    global pdf
    import_file_path = filedialog.askopenfilename()
    image = Image.open(import_file_path)
    pdf = image.convert('RGB')


browseButton = converter.Button(text="Select File ", command=get, bg='gray', fg='white',
                         font=('helvetica', 12, 'italic'))
ui.create_window(200, 150, window=browseButton)


def convert():
    global pdf
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    pdf.save(export_file_path)


saveAsButton = converter.Button(text='Convert to PDF', command=convert, bg='gray', fg='white',
                         font=('Arial', 12, 'italic'))
ui.create_window(200, 200, window=saveAsButton)


def exitapp():

    msgbox = converter.messagebox.askquestion('Exit Application', 'Are you sure?', icon='warning')
    if msgbox == 'yes':
        window.destroy()


exitButton = converter.Button(window, text='Exit Application', command=exitapp, bg='red', fg='white',
                       font=('helvetica', 12, 'italic'))
ui.create_window(200, 310, window=exitButton)

window.mainloop()
