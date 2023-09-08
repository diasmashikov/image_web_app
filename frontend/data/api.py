import streamlit as st
import aiohttp

url = 'http://127.0.0.1:5000/'


async def fetch_and_process_images(image_data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url + "process_image", data=image_data) as response:
            if response.status == 200:
                response_data = await response.json()
                return response_data.get('image_data', [1, 2, 3])
            else:
                st.error(f'Error: {response.status}')
                return []
