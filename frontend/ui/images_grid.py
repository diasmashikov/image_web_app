import streamlit as st


def images_grid(images):
    numColumns = 2
    for i in range(0, len(images), numColumns):
        image_row = images[i:i + numColumns]
        col = st.columns(len(image_row))

        for j, img in enumerate(image_row):
            with col[j]:
                display_image(img)


def display_image(image):
    caption = image.description
    channels = "BGR" if not image.isGray else "RGB"
    st.image(image.matrix, caption=caption, clamp=True, channels=channels)
