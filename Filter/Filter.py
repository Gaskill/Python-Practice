#Filter
import PIL #imports code from python that has functions that are used on photos
from PIL import Image #imports the Image functions from PIL (im.function)

def load_img(filename):
    im = Image.open(filename) #opens file
    return im #im is all the pixel data from the photo "filename"
    im.getdata #imports pixel data

def show_img(im): #displays image
    im.show

def save_img(im, filename): #saves image as a jpeg
    im.save(filename, "jpeg")
    show_img(im)

def obamicon(im): #im brings all the pixel data to the function
    pixels = im.getdata() #im.getdata is a function imported from Pil
    new_pixels = [] #makes an empty list for the new pixel values
    darkBlue = (0, 51, 76) #defines RGB values for specific colors
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 277, 166)

    for p in pixels: #for all pixels
        intensity = p[0] + p[1] + p[2] #adds RGB of pixel together in order to find the intensity of the pixels
        if intensity <= 182: #if the pixel intensity is dark put a dark blue pixel at the end of the new_pixels list
            new_pixels.append(darkBlue)
        elif intensity <= 364 and intensity > 182: #if the pixel intensity is medium dark put a red pixel at the end of the new_pixels list
            new_pixels.append(red)
        elif intensity <= 546 and intensity > 364: #if the pixel intensity is medium light put a light blue pixel at the end of the the new_pixels list
            new_pixels.append(lightBlue)
        elif intensity > 546: #if the pixel intensity is light put a yellow pixel at the end of the the new_pixels list
            new_pixels.append(yellow)
    newIm = Image.new("RGB", im.size)
    newIm.putdata(new_pixels) #turns data from a list into an image
    return newIm #exports the new photo
