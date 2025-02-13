# import matplotlib.pyplot as plt   # (OPTIONAL) Uncomment this if you have installed matplotlib.


def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]


def detect_edges(
    image: list[list[int]], filter: list[list[int]], stride: int
) -> list[list[int]]:
    """
    Detects edges in the input image by convolving the image with the filter.

    Parameter(s):
    - image (2D array): This is the input image that will be processed.
    - filter (2D array): This is the filter that will be used to process the input image.
    - stride (int): Provides the offset for the filter during the convolution process.

    Returns:
    - processed_image (2D array): This is the processed image obtained after performing convolution (will contain edges).
    """
    pass


# (OPTIONAL) This function visualizes the input and output (processed) images side by side using matplotlib.
# def visualize_images_together(image1, image2):
#     fig, axes = plt.subplots(1, 2, figsize=(10, 5))

#     axes[0].imshow(image1, cmap='gray')
#     axes[0].set_title('Original Image')
#     axes[0].axis('off')

#     axes[1].imshow(image2, cmap='gray')
#     axes[1].set_title('Processed Image')
#     axes[1].axis('off')

#     plt.show()


def main(file_name: str) -> list[list[int]]:
    """
    Extracts all input from the input text file.
        - stride
        - image_row, image_col
        - image
        - filter_size
        - vertical_filter
        - horizontal_filter
    Calls detect_edges(...) to perform convolution of image with vertical and horizontal filters.
    Sums the two processed images to obtain the final processed image.
    (Optional) Visualizes the original and processed images side by side using matplotlib.

    Parameter(s):
    - file_name (string): Path to input text file.

    Returns:
    - final_processed_image (2D array): Obtained after adding the two intermediate processed images.
    """
    pass


# Initiates the program by calling main function.
if __name__ == "__main__":
    main("./inputs/test1.txt")
