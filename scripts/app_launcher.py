import threading
import subprocess


def run_streamlit_app():
    # Replace 'streamlit_app.py' with the name of your Streamlit app script
    subprocess.run(['streamlit', 'run', 'frontend/main.py'])


def run_flask_app():
    # Replace 'flask_app.py' with the name of your Flask app script
    subprocess.run(['python', 'backend/app.py'])


if __name__ == "__main__":
    # Create two threads to run the Streamlit and Flask apps concurrently
    streamlit_thread = threading.Thread(target=run_streamlit_app)
    flask_thread = threading.Thread(target=run_flask_app)

    # Start both threads
    streamlit_thread.start()
    flask_thread.start()

    # Wait for both threads to finish
    streamlit_thread.join()
    flask_thread.join()
