import csv
from os import path
import os.path
from PIL import Image, ImageDraw, ImageFont


# According to type use the correct x and y
def writeText (dimage, text, type, myFont) :
    if type == 'nationality' :  
         x = 145
         y = 207
         dimage.text((x, y), text, font=myFont, fill=(6, 61, 113))
    elif type == 'position' :
        x = 145
        y = 247
        dimage.text((x, y), text, font=myFont, fill=(6, 61, 113))
    elif type == 'matricule' :
        x = 350
        y = 137
        dimage.text((x, y), text, font=myFont, fill=(255, 255, 255))  
    else :    
         x = 145
         y = 167
         dimage.text((x, y), text, font=myFont, fill=(6, 61, 113))
    
    return dimage;

# Get a fresh copy of the background image
def getBgImage() :
    # Open image using Image module
    im_bg = Image.open(source_path + "bg.jpg")

    # Resize background image
    im_bg = im_bg.resize((width_im_bg, height_im_bg))
    #default_im_bg = im_bg
    
    return im_bg;


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

MAX_COLUMNS = 6


#------------------------
# Get CSV data 
print ("Start badge generation ...")
with open(data_path + 'staff.csv') as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='"')
     cpte = 0
     for row in reader:
        #print(', '.join(row))
        if cpte == 0 : 
            cpte += 1
            continue
        
        #print (len(row))
        
        if (len(row) < MAX_COLUMNS) : 
            continue
        
        #Pos,STAFF ID,SURNAME,NAME,NATIONALITY,POSITION
        curr_id = row [1].strip()   
        curr_nom = row [2].strip()   + " " +  row[3].strip()     
        curr_nationality = row [4].strip()     
        curr_position = row [5].strip()       
        
        
        #print (curr_id + " " + curr_nom)
        
        
        im_staff_path = source_path + curr_id + ".jpg"
        im_badge = getBgImage()
        if (not os.path.isfile(im_staff_path)) :
            print ("Mauvais chemin " + curr_id + " " + im_staff_path)
            continue
        im_staff= Image.open(im_staff_path)
        if (len(curr_nom) > 15 ) :
              font_size = 20
              im_staff= im_staff.resize((width_im_staff - 20, height_im_staff - 20))
              im_badge.paste(im_staff,(x_im_staff, y_im_staff + 30))
        else :
            im_staff= im_staff.resize((width_im_staff, height_im_staff))
            im_badge.paste(im_staff,(x_im_staff, y_im_staff))
        
        #im_badge.show()
        


        # Write text on the image
        d1 = ImageDraw.Draw(im_badge)
        
          
        myFont = ImageFont.truetype(fonts_path + default_font , font_size)        

        d1 = writeText(d1, curr_id, 'matricule', myFont)
        d1 = writeText(d1, curr_nom, 'nom', myFont)
        d1 = writeText(d1, curr_nationality, 'nationality', myFont)
        d1 = writeText(d1, curr_position, 'position', myFont)

        im_badge.save(output_path + "badge_" + curr_id + ".jpg")
        im_badge.close
        
print ("Fin generation :-)")
        

