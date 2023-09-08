import io
import cv2
import numpy as np
from PIL import Image
from utils.normalization import normalization
from data.models.processed_image import ProcessedImage


def process_image(uploaded_image):
    image_content = uploaded_image.read()
    image_bytes = io.BytesIO(image_content)
    image = Image.open(image_bytes)

    image_np = np.array(image)

    sobelEdgesColor_x = cv2.Sobel(image_np, cv2.CV_64F, 1, 0, ksize=5)
    sobelEdgesColor_y = cv2.Sobel(image_np, cv2.CV_64F, 0, 1, ksize=5)

    original_image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    sobelEdgesGray_x = normalization(
        cv2.Sobel(original_image_gray, cv2.CV_64F, 1, 0, ksize=5))
    sobelEdgesGray_y = normalization(
        cv2.Sobel(original_image_gray, cv2.CV_64F, 0, 1, ksize=5))

    verticalColorEdges = ProcessedImage(
        sobelEdgesColor_x, "Sobel Result - Color - Vertical", False)
    horizontalColorEdges = ProcessedImage(
        sobelEdgesColor_y, "Sobel Result - Color - Horizontal", False)
    verticalGrayEdges = ProcessedImage(
        sobelEdgesGray_x, "Sobel Result - Gray - Vertical", True)
    horizontalGrayEdges = ProcessedImage(
        sobelEdgesGray_y, "Sobel Result - Gray - Horizontal", True)

    different_edges = [verticalColorEdges, horizontalColorEdges,
                       verticalGrayEdges, horizontalGrayEdges]

    return different_edges
