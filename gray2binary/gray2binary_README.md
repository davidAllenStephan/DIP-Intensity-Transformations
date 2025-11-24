
# rgb2gray usage guide

The program ./gray2binary converts an input image to binary at a user defined threshold value and saves to disk. The program can be used by either executing the python file or using the bash file.

Threshold value is user defined and not limited by the program. The high cap threshold is defined in the program at 255. The program by default will create a binary of the inputed gray image. However if the user wishes to split the color channels and segment those (requiring an rgb image) an optional 4th paramter can be included in the execution to account for this.

The output of this program if in grayscale_image mode will result in one image output of the resulting binary image. However, when segmenting the color channels 3 images will be created each prepended with their respective color channel. Ex. red_output_image, green_output_image, blue_output_image.

```$ python3 gray2binary.py [input_grayscale_image_filename] [output_binary_image_filename] [threshold_value] [grayscale_image(0) or rgb_image(1) (optional)]```

```$ ./rgb2gray [input_grayscale_image_filename] [output_binary_image_filename] [threshold_value] [grayscale_image (0) or rgb_image(1) (optional)]```

Usage of the bash file requires execution rights on the file. To enable this execute this command in the directory where the file is stored.

```$ chmod +x gray2binary.sh```
