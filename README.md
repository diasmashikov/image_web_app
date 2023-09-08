# Image Processing Web Application (Edge Detection) by Dias Mashikov

## Overview
This repository contains the implementation of an Image Processing Web Application that performs edge detection on jpg/png images using the Sobel algorithm from OpenCV. The application is built with simplicity and ease of deployment in mind, making it a great choice for small-scale image processing tasks.

## How to run the application
Follow these instructions:

1. In the root of the application, call this command in your terminal **python scripts/app_setup.py**
2. After the setup is done, launch the fullstack application using **python scripts/app_launcher.py**

## Demo
![alt text](https://github.com/diasmashikov/images_hosting/blob/main/sobel_web_1.png)

![alt text](https://github.com/diasmashikov/images_hosting/blob/main/sobel_web_2.png)

![alt text](https://github.com/diasmashikov/images_hosting/blob/main/sobel_web_3.png)

![alt text](https://github.com/diasmashikov/images_hosting/blob/main/sobel_web_4.png)

## Technologies Used
- **Frontend**: Streamlit, a Python frontend framework for rapid web UI development.
- **Backend**: Flask, a Python backend framework for creating HTTP routes to process images.
- **Hosting and Deployment**: Heroku, a cloud hosting platform for hassle-free and reliable deployment.

## Motivation for Tech Stack
The choice of technologies was driven by the project's requirements and the need for simplicity in development and deployment. Here's why we selected these tools:

- **Streamlit and Flask**: These frameworks were chosen for their simplicity in building small web applications. Python's familiarity also played a significant role in their selection, making development more straightforward.

- **Heroku**: Heroku was chosen for hosting and deployment due to its ease of use and automated server maintenance. It allows us to deploy the application quickly without worrying about server management, making it an ideal choice for rapid development.

## Scalability Considerations
If the application were designed to be scalable to handle larger loads and more complex tasks, several improvements could be made:

1. **Frontend Enhancement**: Transition from Streamlit to a more robust frontend library like ReactJS for more extensive control over the user interface, enabling better scalability and customization.

2. **Backend Microservices**: Continue using Flask for the backend but consider adopting a microservices architecture to distribute processing tasks efficiently and handle higher loads.

3. **Dockerization**: Dockerize the application to ensure consistent environments, portability, and easier scaling. This allows for better isolation of components and simplified CI/CD pipelines.

4. **Kubernetes Orchestration**: Utilize Kubernetes to manage multiple Docker containers, ensuring efficient resource allocation, scaling, and load balancing as the application grows.

5. **Software Testing Standards**: Implement comprehensive testing practices, including unit testing for frontend and backend business logic and UI testing for the frontend. This ensures robust and reliable functionality as the application evolves.

6. **Architectural Patterns**: Consider adopting better architectural patterns like Model-View-ViewModel (MVVM) or Model-View-Controller (MVC) for the frontend to maintain code organization and scalability.
