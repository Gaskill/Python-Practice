#Filtergram
#Main Function
import Filter #imports code from Filters.py file

def main():
    filename = input("Enter the name of the image file to edit.")
    im = Filter.load_img(filename)
    newImg = Filter.obamicon(im) #applies obamicon filter to image
    Filter.save_img(newImg, "edited.jpeg")

if __name__ == "__main__": #runs main function
    main()
