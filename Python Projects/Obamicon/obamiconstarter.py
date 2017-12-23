from PIL import Image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

lemon = (236, 232, 26)
aquamarine = (110, 206, 178)
navy = (1, 66, 106)
pink = (244, 54, 76)

im = Image.open("junhee.png") #insert image
width, height = im.size #determines size 
print("Width: {} \nHeight: {}".format(width, height))

data = im.getdata()
data_list = list(data) #data_list puts content of image as a sequence object containing pixel values
print("Data length: {}".format(len(data_list)))


def colorize(image_data):
    
    new_pic = []
    for i in range(len(image_data)-1):
        line = image_data[i]
        dataIntensity = line[0] + line[1] + line[2]
        
        if dataIntensity < 182:
            line = darkBlue
        if dataIntensity > 182 and dataIntensity<364:
            line=red
        if dataIntensity >364 and dataIntensity<546:
            line= lightBlue
        if dataIntensity >546:
            line = yellow  
        new_pic.append(line)
    

    return new_pic

data_colorized = colorize(data_list)
print("Colorized data length: {}".format(len(data_colorized)))

new_image = Image.new(im.mode, im.size) #make them read the documentation group activity to understand that documentation literacy
new_image.putdata(data_colorized)
new_image.show()
new_image.save("output", "jpeg")
 
