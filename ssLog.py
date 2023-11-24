import cv2 as cv, numpy as np, os

#······················································································
#   ssLog.py
#   
#   Creator: Kalatham
#   
#
#   Usage: 
#
#
#······················································································

output_file_name = input (">> Write the output file name: ")

if output_file_name in os.listdir():
    print ("That file already exists. It will be overwritten." )
    while True:
        safety_flag = input ("Type YES if you want to continue. Type NO to abort: ")

        if safety_flag == "YES":
            break
        elif safety_flag == "NO":
            quit



# We set some costants.
image_folder = "tests"          # Name of the folder where you will put the images

MAX_COLUMNS = 6                 # Each row will have MAX_COLUMNS images

WIDTH_CHATLOG = 360             # These are the dimensions of the chat log
HEIGHT_CHATLOG = 1025           # using a 1920x1080 resolution

# We obtain array of the absolute paths of the files in the image_folder.
images = [os.path.abspath(os.path.join(image_folder, image)) for image in os.listdir(image_folder)]

# We calculate the final size of the resulting image
num_images = len(images)                            # Number of chatlogs obtained.
num_rows= 1 + num_images//MAX_COLUMNS               # Number of rows needed

height_final_image = 1025 * num_rows                # Height of the resulting image
width_final_image = WIDTH_CHATLOG * MAX_COLUMNS     # Width of the resulting image

print(width_final_image)
print(height_final_image)

# Creation of the resulting image.
white_image = np.ones((height_final_image, width_final_image, 3), dtype=np.uint8)
counter_i = 0
counter_j = 0

# Main loop
for image in images:
    img = cv.imread(image)                                                          # We read the image.
    chat_log = img[0:HEIGHT_CHATLOG, 0:WIDTH_CHATLOG]                               # We crop to the image just to the chat_log

    cv.imshow("displayer", chat_log)                                                # Debugging lines
    k = cv.waitKey(0)                                                               #

    px_height = (HEIGHT_CHATLOG*(counter_j//MAX_COLUMNS))
    px_height_end = px_height + HEIGHT_CHATLOG
    px_width = (WIDTH_CHATLOG*(counter_i%MAX_COLUMNS))
    px_width_end = px_width + WIDTH_CHATLOG
    

    print("La imagen se colocarán en: ["+str(px_height)+":"+str(px_height_end)+","+str(px_width)+":"+str(px_width_end)+"]")

    counter_i += 1
    counter_j += 1

    white_image [px_height:px_height_end, px_width:px_width_end] = chat_log          # We paste the chat_log


#
# This are the coords in which the images should be pasted.
#
# [0:1025, 0:360]     [0:1025, 360:720] ...
# [1025: 2050, 0:360] [1025: 2050, 360, 720] ...

cv.imwrite("log.png", white_image)








