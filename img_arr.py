import numpy as np
from PIL import Image

def ImgArr(image_arr,top,left,width,height):

    #Convert image into numpy array
    # image_arr = np.array(img)

    #Cropping image according to window
    image_arr = image_arr[top:top+height,left:left+width]
    #Converting numpy array into RGB image
    image = Image.fromarray(image_arr,'RGB')

    # print(image_arr.shape)
    # Converting RGB into Grayscale
    image_gray = image.convert('L')

    # Converting Grayscale image into numpy array
    image_gray_arr = np.array(image_gray)
    print(image_gray_arr.shape)

    # Cropped Grayscale image
    image_gray.show()
    return image_gray_arr

# ImgArr('Image.jpg',500,100,100,200)