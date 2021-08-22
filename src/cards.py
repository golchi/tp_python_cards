from PIL import Image, ImageDraw, ImageFont

#TODO use constasts for path
#TODO use constasts for main bg image path

#TODO use function for writing text
#TODO use function for saving generated image
#TODO use create a log file of successful images

#rose.jpg
#ladies.jpg

source_path = "../source/"
output_path = "../output/"
fonts_path = "../fonts/"

# Open image using Image module
im_ladies = Image.open(source_path + "ladies.jpg")
im_rose = Image.open(source_path +"rose.jpg")

# Resize both images
im_ladies = im_ladies.resize((600, 400))
im_ladies_size = im_ladies.size
im_rose = im_rose.resize((600, 400))
im_rose_size = im_rose.size

# Merge images
new_image = Image.new('RGB',(2* im_ladies_size[0], im_ladies_size[1]), (250,250,250))
new_image.paste(im_ladies,(0,0)) 
new_image.paste(im_rose,(300,0))
#new_image.save(output_path + "merged_image.jpg","JPEG")
new_image.show()

# Write text on the image
d1 = ImageDraw.Draw(new_image)
myFont = ImageFont.truetype(fonts_path + 'Alef-Bold.ttf', 40)
d1.text((50, 50), "BSL TEACHER CARD", font=myFont, fill=(0, 0, 0))

new_image.save(output_path + "image_text.jpg")