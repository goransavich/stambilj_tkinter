########  UNOS DATUMA I BROJA PREDMETA NA STAMBILJ #######
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('slika.png')

# Custom font style and font size
myFont1 = ImageFont.truetype('arial.ttf', 28)
myFont2 = ImageFont.truetype('arial.ttf', 38)

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

datum = "24.12.2021."
broj = "906-401-1/2021"

# Add Text to an image
I1.text((140, 80), datum, font=myFont1, fill=(7, 60, 145))
I1.text((10, 140), broj, font=myFont2, fill=(7, 60, 145))

# Display edited image
img.show()

# Save the edited image
img.save("stambilj.png")


############## STAVLJANJE STAMBILJA NA PDF PRIJAVU ####################
import fitz

input_file = "example.pdf"
output_file = "example-with-barcode.pdf"
barcode_file = "stambilj.png"

# define the position (upper-right corner)
image_rectangle = fitz.Rect(450,20,550,120)

# retrieve the first page of the PDF
file_handle = fitz.open(input_file)
first_page = file_handle[0]

# add the image
first_page.insertImage(image_rectangle, fileName=barcode_file)

file_handle.save(output_file)