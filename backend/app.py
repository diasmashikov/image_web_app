import io
from flask import Flask, request, jsonify
from image_processing.sobel import process_image

app = Flask(__name__)


@app.route('/process_image', methods=['POST'])
def process_uploaded_image():
    try:
        uploaded_image_file = request.files['image_file']

        if uploaded_image_file.filename != '':
            processed_images = process_image(uploaded_image_file)
            processed_images_json = [img.convert_to_json()
                                     for img in processed_images]

            return jsonify({'image_data': processed_images_json})

        else:
            return jsonify({'error': 'No file uploaded'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
