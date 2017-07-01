from PIL import Image



def change_pixel_colors(my_image,obamacon_colors):
    """
    Your image is coverted to pixels with a certain color (rgb value).
    pixel_data_list is a list of tuples. It is a list of pixels, but every pixel
    has 3 rgb values. 
    (1) Print the pixel_data_list. What do you see? Does it make sense?
    (2) How many pixels does your image have?
    (3) Pixel intensity is defined as the sum of its rgb values. So if the pixel's
    rgb values are (0,51,100) the intensity is 151.
    Your assignment is to calculate the intensity of each pixel. Based on intensity
    make a new list of rgb pixel values with the correct obamacon_color:
    darkBlue if intensity < 182
    red if intensity between 182 and 364
    lightBlue if intensity between 364 and 546
    yellow if intensity > 546
    return the new pixel list
    """
    pixel_data = my_image.getdata() #What happens if you print this?
    pixel_data_list = list(pixel_data) #converting image data to a list

    new_pixel_data = [] #create new empty list

    ### YOUR CODE GOES HERE ###
    for pixel in pixel_data_list:
        intensity = sum(pixel) # Built in function that does the sum
        if intensity < 182:
            new_pixel_data.append(obamacon_colors['darkBlue'])
        elif intensity >= 182 and intensity < 364:
            new_pixel_data.append(obamacon_colors['red'])
        elif intensity >= 364 and intensity <= 546:
            new_pixel_data.append(obamacon_colors['lightBlue'])
        elif intensity > 546:
            new_pixel_data.append(obamacon_colors['yellow'])
    
    return new_pixel_data

def go_crazy(my_image,obamacon_colors):
    """
    What if you only changed half the pixels? or made your new image look
    like a checkerboard? Can you do that? How are the pixels laid out, i.e. how
    is the program reading in the pixels? Like we read a book (starting at 
    upper left corner and ending at bottom right)? Try to implement.
    """
    crazy_pixels = []
    pixel_data = my_image.getdata()
    pixel_data_list = list(pixel_data)

    ### YOUR CODE GOES HERE ###
    """ soln for 1/2 obamacon"""
    for i in range(len(pixel_data_list)):
        if i < len(pixel_data_list)/2:
            crazy_pixels.append(pixel_data_list[i])
        else:
            intensity = sum(pixel_data_list[i])
            if intensity < 182:
                crazy_pixels.append(obamacon_colors['darkBlue'])
            elif intensity >= 182 and intensity < 364:
                crazy_pixels.append(obamacon_colors['red'])
            elif intensity >= 364 and intensity <= 546:
                crazy_pixels.append(obamacon_colors['lightBlue'])
            elif intensity > 546:
                crazy_pixels.append(obamacon_colors['yellow'])

    
    return crazy_pixels


def main():
    """
    dictionary of color values.
    Set rgb values for the standard Obamacon photo
    color = (red_value,green_value,blue_value) i.e. rgb values
    """
    obamacon_colors = {} #create dictionary of colors: dictionary_name[key] = value
    obamacon_colors['darkBlue'] = (0, 51, 76)
    obamacon_colors['red'] = (217, 26, 33)
    obamacon_colors['lightBlue'] = (112, 150, 158)
    obamacon_colors['yellow'] = (252, 227, 166)

    """
    Open image file. Replace IMAGENAME with the name of your pic. If the pic
    is not in the same directory(folder) as this program, make sure you include the
    path to the image. You can see the path by typing (in bash):
    $ pwd
    """
    my_image = Image.open("MrFuzzyPants.jpeg")

    
    """Call the function that changes the pixels"""
    new_pixels = change_pixel_colors(my_image,obamacon_colors)
    #crazy_pixels = go_crazy(my_image,obamacon_colors)

    
    """Functions that create a new image based on your new pixels"""
    new_image = Image.new("RGB", my_image.size)
    new_image.putdata(new_pixels)
    new_image.show()
    new_image.save("newMrFuzzypants.jpg", "jpeg") ### Change NEW-IMAGENAME

    return


"""Call to main()"""
if __name__ == "__main__":
    main()
