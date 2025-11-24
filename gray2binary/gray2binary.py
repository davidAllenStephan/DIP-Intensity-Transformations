# Created by David Allen Stephan Marino
# University of Missouri
# 2025-09-10

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


def save_images(imgs, paths):
    i = 0
    for img in imgs:
        cv.imwrite(paths[i], img)
        i = i + 1


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
    gcf.savefig(path)


# Splits full color image to channels then applies thresholding
def apply_binary_thresh_rgb(image, thresh_value_low, thresh_value_high):
    r_chan = image[:, :, 2]
    g_chan = image[:, :, 1]
    b_chan = image[:, :, 0]
    _, red_thresh_binary = cv.threshold(r_chan, thresh_value_low, thresh_value_high, cv.THRESH_BINARY)  # noqa
    _, green_thresh_binary = cv.threshold(g_chan, thresh_value_low, thresh_value_high, cv.THRESH_BINARY)  # noqa
    _, blue_thresh_binary = cv.threshold(b_chan, thresh_value_low, thresh_value_high, cv.THRESH_BINARY)  # noqa
    return red_thresh_binary, green_thresh_binary, blue_thresh_binary  # noqa


# Applies thresholding to gray scale image
def apply_binary_thresh_gray(image, thresh_value_low, thresh_value_high):
    _, thresh_binary = cv.threshold(image, thresh_value_low, thresh_value_high, cv.THRESH_BINARY)  # noqa
    return thresh_binary


def main():
    input_grayscale_image_filename = ""
    output_binary_image_filename = ""
    threshold_value = 0
    rgb_or_gray = 0

# Checking argument validity
    if len(sys.argv) < 4:
        print(
            "Missing arguments: $./gray2binary.sh [input_grayscale_image_filename] [output_binary_image_filename] [threshold_value] [grayscale_image(0) or rgb_image(1) (optional)]")  # noqa
        sys.exit(1)

# Checking if input file exists.
    input_grayscale_image_filename = sys.argv[1]
    output_binary_image_filename = sys.argv[2]
    threshold_value = int(sys.argv[3])
    print(len(sys.argv))
    if len(sys.argv) == 5:
        rgb_or_gray = int(sys.argv[4])
    path_input_grayscale_image = pathlib.Path(input_grayscale_image_filename)
    if not path_input_grayscale_image.exists():
        print(input_grayscale_image_filename + " does not exist.")
        sys.exit(1)

# CV image load.
    img = cv.imread(cv.samples.findFile(
        input_grayscale_image_filename), cv.IMREAD_UNCHANGED)
    if img is None:
        print("Could not read " + input_grayscale_image_filename)
        sys.exit(1)

    if rgb_or_gray == 0:
        # Applying binary thresh
        thresh_img = apply_binary_thresh_gray(img, threshold_value, 255)
        res = save_image(thresh_img, output_binary_image_filename)
        if not res:
            sys.exit(1)
    elif rgb_or_gray == 1:
        # Applying binary thresh on color channels
        red_thresh_img, green_thresh_img, blue_thresh_img = apply_binary_thresh_rgb(img, threshold_value, 255)  # noqa
        color_channel_thresh_imgs = [red_thresh_img, green_thresh_img, blue_thresh_img]  # noqa
        paths = ["red_" + output_binary_image_filename, "green_" + output_binary_image_filename, "blue_" + output_binary_image_filename]  # noqa
        res = save_images(color_channel_thresh_imgs, paths)
        if not res:
            sys.exit(1)

# Checking if output was successful.
    path_output_image = pathlib.Path(output_binary_image_filename)
    if not path_output_image.exists():
        print(output_binary_image_filename + " creation failed.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
