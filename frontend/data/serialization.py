import aiohttp
import numpy as np

from data.models.processed_image import ProcessedImage


def serialize_image_data(uploaded_image):
    image_data = aiohttp.FormData()
    image_data.add_field('image_file', uploaded_image.read(),
                         filename=uploaded_image.name)
    return image_data


def deserialize_image_data(image_data):
    processed_images = []
    for processed_image in image_data:
        matrix = np.array(processed_image.get('matrix'))
        description = processed_image.get('description')
        is_gray = processed_image.get('isGray')
        processed_image = ProcessedImage(matrix, description, is_gray)
        processed_images.append(processed_image)
    return processed_images
