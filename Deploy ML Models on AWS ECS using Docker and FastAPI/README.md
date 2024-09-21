# Deploying a Trained Machine Learning Model as an Interactive Web Application

After training the ML model using Jupyter Notebook or another tool, we build an interactive website to showcase the value of our work. 

In this guide, we will focus on app development rather than model training, and will walk you through the process of deploying the trained model as a web application using FastAPI and Docker, and finally hosting it on AWS ECS.

### Step1: Obtain the Trained Model

First, ensure that you have the trained machine learning model saved in a format that can be easily loaded (such as .pkl or .h5). This model will be used for inference in your application.

### Step2: Create the Model Inference Script
To perform model inference, create a Python script that loads the trained model and runs predictions. You can reference an example from [this script.](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Deploy%20ML%20Models%20on%20AWS%20ECS%20using%20Docker%20and%20FastAPI/app/model/model_inference.py)

### Step3: Build the FastAPI Application
Next, develop a FastAPI application to serve your model. This app will expose an API endpoint for users to send data and receive predictions. You can refer to this example[FastAPI App.](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Deploy%20ML%20Models%20on%20AWS%20ECS%20using%20Docker%20and%20FastAPI/app/main.py)

### Step 4: Dockerize the FastAPI Application
Once your FastAPI app is ready, you'll need to containerize it using Docker. This allows the app to run consistently in any environment. Here's the following [Dockerize example](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Deploy%20ML%20Models%20on%20AWS%20ECS%20using%20Docker%20and%20FastAPI/Dockerfile) 

To build the Docker image, navigate to your project’s root directory and run:

```python
docker build -t <your_docker_hub_username>/language-detection-app .
```

Once the image is built, you can run the container with:

```python
docker run -p 80:80 <your_docker_hub_username>/language-detection-app
```

step5: Push the above Docker image to the Docker Hub

login to your docker
```python
docker login
```

push the image
```python
docker push <your_docker_hub_username>/language-detection-app
```


step5: Deploying Docker Hub image on AWS ECS

Creating the ECS Cluster

![1*d5P2NPGrpAGJNGu1RfLH6g](https://github.com/user-attachments/assets/b0b7383b-2faf-45ae-b49e-0a5c272e31f2)

In “Image URI” give your docker image path and container port should be 80.

![1*DiWpE8dQVFVhYULHfcLb3A](https://github.com/user-attachments/assets/918de2f8-8375-48a1-8400-8ecff7bf31d6)

Now, create a new task definition

![1*x85pK7nPVgatEokqDhck0w](https://github.com/user-attachments/assets/f8e1f924-fca9-4f0a-adec-1a775eb3a109)

run the above task definition as a new task in the cluster

![1*uHHAzxqTHAbIfsDlMLvy2A](https://github.com/user-attachments/assets/9721ba4f-1882-41f4-a55d-58026fad9f9c)

