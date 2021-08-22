import csv
from PIL import Image, ImageDraw, ImageFont


# Functions
def writeName (dimage, text, type, myFont) :
    #According to type use the correct x and y
   
    """
    nom //  prenom -- concatener avec nom
    nationalite
    matricule
    delai
    """
    if type == 'nationalite' :        
        y = 40
    elif type == 'matricule' :
        x = 40
        y = 10
    elif type == 'delai' :
        y = 60    
    else :    
         x = 10
         y = 20

    #print ("Voici le nom : " + text)
    d1.text((x, y), text, font=myFont, fill=(0, 0, 0))
    #print(', '.join(row))
    return d1;


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

#rose.jpg
#ladies.jpg

source_path = "../source/"
output_path = "../output/"
fonts_path  = "../fonts/"
data_path   = "../data/"

# Open image using Image module
im_ladies = Image.open(source_path + "ladies.jpg")
im_rose = Image.open(source_path +"rose.jpg")

# Resize both images
im_ladies = im_ladies.resize((400, 250))
im_ladies_size = im_ladies.size
im_rose = im_rose.resize((80, 120))
im_rose_size = im_rose.size

# Merge images
new_image = Image.new('RGB',(im_ladies_size[0], im_ladies_size[1]), (250,250,250))

#new_image.save(output_path + "merged_image.jpg","JPEG")
#new_image.show()


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

        new_image.paste(im_ladies,(0,0)) 
        new_image.paste(im_rose,(200,20))

        curr_nom = row [0]   
        curr_id = row [1]   
        #curr_nom = row [0]   
        #curr_nom = row [0]   

        #print (curr_id + "---")

        # Write text on the image
        d1 = ImageDraw.Draw(new_image)
        myFont = ImageFont.truetype(fonts_path + 'Alef-Bold.ttf', 40)        

        d1 = writeName(d1, curr_nom, 'nom', myFont)

        new_image.save(output_path + "image_text_" + curr_id + ".jpg")
        

