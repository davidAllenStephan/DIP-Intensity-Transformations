# Created by David Allen Stephan Marino
# University of Missouri
# 2025-09-08

import sys
import pathlib
import cv2 as cv
import matplotlib.pyplot as plt


# Saves the image
def save_image(img, path):
    res = cv.imwrite(path, img)
    if not res:
        return False
    return True


# Converts the provided image to pyplot plot with styling
def convert_img_to_plyplot_styled(img, title):
    img_plot = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    plt.imshow(img_plot)
    plt.axis("off")
    plt.title(title)
    gcf = plt.gcf()
    return gcf


# Saves plot to provided path
def save_plt_image(gcf, path):
    gcf.savefig(path, bbox_inches='tight', pad_inches=0)


# Applies gray scale transformation to cv image
def apply_grayscale(img):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            img[y, x] = 0.2989 * img[y, x, 2] + 0.5871 * \
                img[y, x, 1] + 0.1140 * img[y, x, 0]
    return img


def main():
    input_color_image_filename = ""
    output_grayscale_image_filename = ""
    path_input_color_image = ""

# Checking argument validity.
    if len(sys.argv) < 3:
        print("Missing arguments: $./rgb2gray.sh input_color_image_filename output_grayscale_image_filename")
        sys.exit(1)

# Checking if input file exists.
    input_color_image_filename = sys.argv[1]
    output_grayscale_image_filename = sys.argv[2]
    path_input_color_image = pathlib.Path(input_color_image_filename)
    if not path_input_color_image.exists():
        print(input_color_image_filename + " does not exist.")
        sys.exit(1)

# CV image load.
    img = cv.imread(cv.samples.findFile(
        input_color_image_filename), cv.IMREAD_UNCHANGED)
    if img is None:
        print("Could not read " + input_color_image_filename)
        sys.exit(1)

# Appling gray scale transformation.
    gray_scale_img = apply_grayscale(img)

# Saving the image.
    save_image(gray_scale_img, output_grayscale_image_filename)

# Checking if output was successful.
    path_output_image = pathlib.Path(output_grayscale_image_filename)
    if not path_output_image.exists():
        print(output_grayscale_image_filename + " creation failed.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
