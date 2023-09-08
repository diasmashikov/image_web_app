import asyncio
from data.api import fetch_and_process_images
from data.serialization import deserialize_image_data, serialize_image_data


def process_uploaded_image(uploaded_image):
    serialized_image_data = serialize_image_data(uploaded_image)
    serialized_processed_image_data = asyncio.run(
        fetch_and_process_images(serialized_image_data))
    processed_images = deserialize_image_data(serialized_processed_image_data)
    return processed_images
