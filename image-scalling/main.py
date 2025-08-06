import numpy as np
import imageio
import matplotlib.pyplot as plt

# Convert a color image to grayscale 
def convert_to_grayscale(rgb_image):

    red, green, blue = rgb_image[:,:,0], rgb_image[:,:,1], rgb_image[:,:,2]

    # Grayscale conversion equation
    grayscale = 0.299 * red + 0.5870 * green + 0.1140 * blue
    print('Converted to grayscale: Done')
    return grayscale.astype(np.uint8)

# Resize an image to a specified percentage of its original dimensions
def resize_image(input_image, orig_height, orig_width, new_height, new_width):
    resized_image = np.zeros((new_height, new_width), dtype=np.float32)
    print(orig_height, 'x', orig_width, ' --> ', new_height, 'x', new_width, '\n')

    for i in range(new_height):
        for j in range(new_width):
            x = i / new_height * (orig_height - 1)
            y = j / new_width * (orig_width - 1)
            x0, x1 = int(x), int(x) + 1
            y0, y1 = int(y), int(y) + 1
            dx, dy = x - x0, y - y0

            topLeft = input_image[x0, y0]
            topRight = input_image[x0, y1]
            bottomLeft = input_image[x1, y0]
            bottomRight = input_image[x1, y1]

            interpolated_value = (
                topLeft * (1 - dx) * (1 - dy) +
                topRight * dx * (1 - dy) +
                bottomLeft * (1 - dx) * dy +
                bottomRight * dx * dy
            )

            resized_image[i, j] = interpolated_value
    print('Image resized: Done')
    return resized_image.astype(np.uint8)

# Load the original image
original_image = plt.imread("image.jpg")

# Convert the image to grayscale
grayscale_image = convert_to_grayscale(original_image)
imageio.imsave("gray_image.jpg", grayscale_image)

orig_height, orig_width = grayscale_image.shape

# Calculate the new dimensions after resizing to 70% of the original size
new_height_resized = int(orig_height * 0.7)
new_width_resized = int(orig_width * 0.7)

# Resize the image
resized_image = resize_image(grayscale_image, orig_height, orig_width, new_height_resized, new_width_resized)
imageio.imsave("resized_image.jpg", resized_image)

# Resize the image back to its original dimensions
resized_back_image = resize_image(resized_image, new_height_resized, new_width_resized, orig_height, orig_width)
imageio.imsave("resized_back_image.jpg", resized_back_image)

# Calculate the Sum of Squared Differences (SSD) between two images
def calculate_ssd(image1, image2):

    print(image1.shape, image2.shape)
    difference = image1 - image2
    squared_difference = difference ** 2
    ssd_value = np.sum(squared_difference)

    print('The Sum of Squared Differences:', ssd_value)
    print('The average of squared differences:', np.mean(squared_difference))
    return ssd_value


# Compute the SSD between the original grayscale image and the resized-back grayscale image
calculate_ssd(grayscale_image, resized_back_image)
