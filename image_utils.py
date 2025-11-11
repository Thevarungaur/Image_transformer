import cv2
import numpy as np
from PIL import Image

def read_and_preprocess_image(image_file, width=400):
    """Read an image, convert it to grayscale, and resize while keeping aspect ratio."""
    pil_img = Image.open(image_file)
    rgb_array = np.array(pil_img)
    grayscale_img = cv2.cvtColor(rgb_array, cv2.COLOR_RGB2GRAY)

    # Maintain aspect ratio during resizing
    height, width_original = grayscale_img.shape
    aspect = width_original / height
    adjusted_height = int(width / aspect)
    resized_img = cv2.resize(grayscale_img, (width, adjusted_height))

    return resized_img


def rotate_image(image, angle):
    """Rotate the image about its center point."""
    rows, cols = image.shape
    rotation_center = (cols // 2, rows // 2)
    rotation_matrix = cv2.getRotationMatrix2D(rotation_center, angle, 1.0)
    rotated_img = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    return rotated_img


def scale_image(image, scale_factor):
    """Scale the image by the specified factor."""
    if scale_factor <= 0:
        raise ValueError("Scaling factor must be greater than zero.")
    # Get original size
    original_height, original_width = image.shape[:2]
    # Compute new size
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    # Ensure at least 1 pixel in each dimension
    new_width = max(new_width, 1)
    new_height = max(new_height, 1)
    scaled_img = cv2.resize(image,
                            (new_width, new_height),
                            interpolation=cv2.INTER_LINEAR)
    return scaled_img


def translate_image(image, tx, ty):
    """Shift (translate) the image along X and Y directions."""
    rows, cols = image.shape
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    shifted_img = cv2.warpAffine(image, translation_matrix, (cols, rows))
    return shifted_img
