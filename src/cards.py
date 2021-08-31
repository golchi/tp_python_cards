import csv
from PIL import Image, ImageDraw, ImageFont

"""
#TODO use function for writing text
#TODO use function for saving generated image
#TODO use create a log file of successful images

open bg image
open csv file
loop csv list
 - get current row
 - get current id or image_id_value
 - open current image_id.jpg
 - write all textes
 - merge images
 - generate new image

"""

# Functions
def writeText (dimage, text, type, myFont) :
    #According to type use the correct x and y
   
    """
    nom //  prenom -- concatener avec nom
    nationalite
    matricule
    delai
    """ 
    if type == 'nationality' :  
         x = 150
         y = 205
         dimage.text((x, y), text, font=myFont, fill=(6, 61, 113))
    elif type == 'position' :
        x = 150
        y = 245
        dimage.text((x, y), text, font=myFont, fill=(6, 61, 113))
    elif type == 'matricule' :
        x = 350
        y = 135
        dimage.text((x, y), text, font=myFont, fill=(255, 255, 255))
    elif type == 'delai' :
        y = 60    
    else :    
         x = 150
         y = 165
         dimage.text((x, y), text, font=myFont, fill=(6, 61, 113))
    
    return dimage;


source_path = "../source/"
output_path = "../output/"
fonts_path  = "../fonts/"
data_path   = "../data/"


width_im_bg = 648
height_im_bg = 420
width_im_staff = 178
height_im_staff = 180
x_im_staff = 448
y_im_staff = 170

font_size = 24
default_font = 'arial_black.ttf'

# Open image using Image module
im_bg = Image.open(source_path + "bg.jpg")

# Resize background image
im_bg = im_bg.resize((width_im_bg, height_im_bg))

#------------------------
# Get CSV data 

with open(data_path + 'sample1.csv') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
     cpte = 0
     for row in reader:
         #print(', '.join(row))
        if cpte == 0 : 
            cpte += 1
            continue
        
        #print (len(row))
        
        if (len(row) < 7) : 
            continue
        
        #"Pos", "ID","Surname", "Firstname", "Nationality","Position","Phone"
        curr_id = row [1].strip()   
        curr_nom = row [2].strip()   + " " + row[3].strip()       
        curr_nationality = row [4].strip()     
        curr_position = row [5].strip()       
        
        im_staff= Image.open(source_path + curr_id + ".jpg")
        im_staff= im_staff.resize((width_im_staff, height_im_staff))
        
        im_bg.paste(im_bg,(0,0)) 
        im_bg.paste(im_staff,(x_im_staff, y_im_staff))


        print (curr_position + "---")

        # Write text on the image
        d1 = ImageDraw.Draw(im_bg)
        #Arial Black
        myFont = ImageFont.truetype(fonts_path + default_font , font_size)        

        d1 = writeText(d1, curr_id, 'matricule', myFont)
        d1 = writeText(d1, curr_nom, 'nom', myFont)
        d1 = writeText(d1, curr_nationality, 'nationality', myFont)
        d1 = writeText(d1, curr_position, 'position', myFont)

        im_bg.save(output_path + "badge_" + curr_id + ".jpg")
        

