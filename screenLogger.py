import cv2 as cv, numpy as np, os

#········································
#   screenLogger.py
#   
#


# Obtenemos el directorio donde vamos a guardar las imágenes a juntar.
# Para 1920x1080    --> Esquina inferior derecha del chat log   [360,1025]
#                       Esquina superior izquierda del chat log [0,0]



image_folder = "tests"
MAX_COLUMNS = 6
WIDTH_CHATLOG = 360
HEIGHT_CHATLOG = 1025

# Obtenemos rutas absolutas de los archivos en la carpeta "tests"
images = [os.path.abspath(os.path.join(image_folder, image)) for image in os.listdir(image_folder)]

# Calculamos el tamaño de la imagen final
num_images = len(images)                            # Número de chatlogs
num_rows= 1 + num_images//MAX_COLUMNS               # Número de filas de chatlogs.
height_final_image = 1025 * num_rows                
width_final_image = WIDTH_CHATLOG * MAX_COLUMNS

# Creamos una imagen en blanco con las medidas finales.
white_image = np.ones((height_final_image, width_final_image, 3), dtype=np.uint8)
local_counter = 0

print(os.listdir())




for image in images:
    img = cv.imread(image)
    chat_log = img[0:1025, 0:360]

    cv.imshow("displayer", chat_log)
    k = cv.waitKey(0)

    white_image [0:1025, 360*local_counter:360+local_counter*360] = chat_log
    local_counter = local_counter + 1

cv.imshow("displayer", white_image)
k = cv.waitKey(0)
cv.imwrite("log.png", white_image)








