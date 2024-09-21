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

```


### Step 5: Push the Docker Image to Docker Hub

Before deploying to AWS, you need to push your Docker image to Docker Hub.

Log in to your Docker account:

```python
docker login
```

Then push the image to Docker Hub:
```python
docker push <your_docker_hub_username>/language-detection-app
```

### Step 6: Deploy the Docker Image on AWS ECS

Now, let’s deploy the Dockerized FastAPI app on AWS Elastic Container Service (ECS).



1. Create an ECS Cluster
In the AWS ECS console, create a new cluster.
![1*d5P2NPGrpAGJNGu1RfLH6g](https://github.com/user-attachments/assets/b0b7383b-2faf-45ae-b49e-0a5c272e31f2)



2. Create a New Task Definition
Now, create a new task definition for the app in ECS. Set it to use the Docker image from your Docker Hub.


![1*x85pK7nPVgatEokqDhck0w](https://github.com/user-attachments/assets/f8e1f924-fca9-4f0a-adec-1a775eb3a109)

In the container settings, provide the "Image URI" with your Docker Hub image path, and set the container port to 80.

![1*DiWpE8dQVFVhYULHfcLb3A](https://github.com/user-attachments/assets/918de2f8-8375-48a1-8400-8ecff7bf31d6)


3. Run the Task in the ECS Cluster
Finally, launch the task in your ECS cluster.


![1*uHHAzxqTHAbIfsDlMLvy2A](https://github.com/user-attachments/assets/9721ba4f-1882-41f4-a55d-58026fad9f9c)



Once your task is running, the application will be live and accessible via the public URL associated with the ECS task.

<img width="838" alt="image" src="https://github.com/user-attachments/assets/86d0474f-86b6-4e98-9359-c3a563ce272a">

You can trigger the ECS task automatically using AWS Lambda. This setup can be helpful in scenarios where you want the container to be invoked based on certain events or schedules.

This Lambda function can be configured to start the ECS task using the public identifier. We will talke more about AWS develop [here](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Application%20Building/README.md).

![WeChatb26e02af92c8ada953e6ed81b22ae8bf](https://github.com/user-attachments/assets/6be24220-f06e-4a42-a03e-291e75b6e687)

By following these steps, you’ll successfully deploy your machine learning model as a web application using FastAPI and Docker, hosted on AWS ECS. In upcoming sections, we’ll explore further enhancements like automating the task triggering using AWS Lambda.
