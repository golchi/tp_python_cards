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
    im_bg = Image.open(source_path + "a4.jpg")
    

    # Resize background image
    #im_bg = im_bg.resize((width_im_bg, height_im_bg))
    #default_im_bg = im_bg
    
    return im_bg;


source_path = "../data/" #source
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
MAX_TOTAL_BADGE = 26

pos_x = 20
pos_y = 20

#------------------------
# Get CSV data 
print ("Start badge generation ...")
#with open(data_path + 'staff.csv') as csvfile:
     #reader = csv.reader(csvfile, delimiter=',', quotechar='"')
reader = os.listdir(output_path)
cpte = 0
k = 0

im_a4 = getBgImage()
for row in reader:
    
    """
    #print(', '.join(row))
    if cpte == 0 : 
        cpte += 1
        continue

    #print (len(row))

    if (len(row) < MAX_COLUMNS) : 
        continue

    #Pos,STAFF ID,SURNAME,NAME,NATIONALITY,POSITION
    curr_id = row [1].strip()   
    
    """
    
    k += 1
    
    if (k == 2) :
        x = pos_x
        y = pos_y
    elif (k == 3) :
        x = pos_x + 640
        y = pos_y 
    elif (k == 4) :
        x = pos_x 
        y = pos_y + 420
    elif (k == 5) :
        x = pos_x + 640
        y = pos_y + 640
    elif (k == 6) :
        x = pos_x
        y = pos_y + 840
    elif (k == 7) :
        x = pos_x + 640
        y = pos_y + 900
    elif (k == 8) :
        x = pos_x 
        y = pos_y + 900
    elif (k == 9) :
        x = pos_x  + 640
        y = pos_y + 900
        
    
    
    if (row == "a4_badge_.jpg") :
        continue    
    
    im_staff = Image.open(output_path + row)
    #x = pos_x + (0 * k)
    #y = pos_y + (50 * k)
    
    print (output_path, k, row, x, y)
    
    im_a4.paste(im_staff,(x,y))
    #im_a4.paste(im_staff, (20,20))
    #im_a4.show()    
    im_a4.save(output_path + "a4_badge_.jpg")
    
    
    """
    print (row)
    
    im_staff_path = output_path + "badge_" + curr_id + ".jpg"
    if (not os.path.isfile(im_staff_path)) :
        continue
    im_staff= Image.open(im_staff_path)
    #im_staff= im_staff.resize((width_im_staff, height_im_staff))

    im_badge = getBgImage()
    #im_badge.show()
    im_badge.paste(im_staff,(x_im_staff, y_im_staff))

    im_badge.save(output_path + "a4_badge_" + k + ".jpg")
    im_badge.close
    if ((k % 8) and (k < MAX_TOTAL_BADGE)) :
        k = 0
        pass
    elif (k > MAX_TOTAL_BADGE)

    """
        
print ("Fin generation :-)")


