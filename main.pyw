#Importing tk libraty
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import fitz
import os
import pathlib

# root window
root = tk.Tk()
root.geometry("300x200")
root.title('Štambilj')
root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(0, weight=4)
root.rowconfigure(3, weight=4)

# Prozor za učitavanje prijave

def select_file():
    filetypes = (
        ('PDF files', '*.pdf'),
    )

    filename = fd.askopenfilename(
        title='Učitaj prijavu',
        initialdir='/',
        filetypes=filetypes)
    global proba
    proba = filename

# Dugme za učitavanje prijave

open_button = ttk.Button(
    root,
    text='Učitaj prijavu',
    command=select_file
)

open_button.pack(expand=True)
open_button.grid(column=0, row=0, columnspan = 4, sticky=tk.EW, padx=5, pady=5)

# datum prijave
datum_label = ttk.Label(root, text="Datum prijave")
datum_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

datum_entry = ttk.Entry(root)
datum_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

# broj prijave
broj_label = ttk.Label(root, text="Broj prijave")
broj_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

broj_entry = ttk.Entry(root)
broj_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

def stavi_stambilj():
    ########  UNOS DATUMA I BROJA PREDMETA NA STAMBILJ #######
    # Open an Image
    img = Image.open('slika.png')

    # Custom font style and font size
    myFont1 = ImageFont.truetype('arial.ttf', 62)
    myFont2 = ImageFont.truetype('arial.ttf', 72)

    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)

    datum = str(datum_entry.get())
    broj = str(broj_entry.get())

    # Add Text to an image
    I1.text((350, 173), datum, font=myFont1, fill=(7, 60, 145))
    I1.text((30, 340), broj, font=myFont2, fill=(7, 60, 145))

    # Display edited image
    # img.show()

    izmenjen_broj = broj.replace("/", "-")

    # Save the edited image
    img.save("stambilj.png")

    ############## STAVLJANJE STAMBILJA NA PDF PRIJAVU ####################

    input_file = str(proba)
    output_file = "prijava" + izmenjen_broj + ".pdf"
    barcode_file = "stambilj.png"

    # define the position (upper-right corner)
    image_rectangle = fitz.Rect(350, 20, 600, 100)

    # retrieve the first page of the PDF
    file_handle = fitz.open(input_file)
    first_page = file_handle[0]

    # add the image
    first_page.insert_image(image_rectangle, filename=barcode_file)

    # brisanje iskorišćenog stambilja
    if os.path.exists("stambilj.png"):
        os.remove("stambilj.png")
    else:
        print("The file does not exist")

    radna_povrsina = os.path.join((os.environ['USERPROFILE']), 'Desktop')

    overena_prijava = os.path.join(radna_povrsina, output_file)

    file_handle.save(overena_prijava)

    #os.system(overena_prijava)

# Završi button
zavrsi_button = ttk.Button(root, text="Završi", command=stavi_stambilj)
zavrsi_button.grid(column=0, row=3, columnspan = 4, sticky=tk.EW, padx=5, pady=5)



root.mainloop()




