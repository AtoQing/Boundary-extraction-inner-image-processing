import cv2
import numpy as np

def erosion():


    img = cv2.imread("image.jpg")
    cv2.imshow("original", img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, binary) = cv2.threshold(gray, 177, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((7, 7))

    image_shape = binary.shape
    kernel_shape = kernel.shape
    original_binary=binary
    binary = binary / 255  # 0-1 arasında olması için
    original_binary= original_binary / 255
    output_row = image_shape[0] + kernel_shape[0] - 1  # output image boyutları. Resme bak
    output_column = image_shape[1] + kernel_shape[1] - 1
    output_image = np.zeros((output_row, output_column))

    # Padding image.
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            output_image[i + int((kernel_shape[0] - 1) / 2), j + int((kernel_shape[1] - 1) / 2)] = binary[i, j]

            
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            window = output_image[i:i + kernel_shape[0], j:j + kernel_shape[1]]  # resime bak
            result = (window == kernel)  # filtre ile parça aynı ise result 1 olcak.
            new_value = np.all(result == True)  # erosion da result 1 ise yeni değerde 1 olcak

            if new_value:
                binary[i, j] = 1
            else:
                binary[i, j] = 0

    new=np.zeros((image_shape[0],image_shape[1]))
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            new[i,j]= original_binary[i, j] - binary[i, j]

    cv2.imshow("boundry",new)
    cv2.imshow("erosion", binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

erosion()
