import streamlit as st
import numpy as np

from logic.image_processing import process_uploaded_image

from ui.images_grid import images_grid


def main():
    st.title("Image Processing with Sobel Edge Detection for AMIIE Research and Educational Laboratory by Dias Mashikov")
    uploaded_image = st.file_uploader(
        "Choose an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        st.write("Original Image")
        st.image(uploaded_image, caption='Original Uploaded Image',
                 use_column_width=True)

        if st.button("Process"):
            with st.spinner(text="Image is processing..."):
                processed_images = process_uploaded_image(uploaded_image)
                st.success("Image processing is done!")
            images_grid(processed_images)


if __name__ == "__main__":
    main()
