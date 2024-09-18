On this step, we are going to put the model we trained on Docker hub so we can use it on AWS ECS.

step1: Fist, we need to have the trained model

step2: Second, we create the [Model Inference script](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Deploy%20ML%20Models%20on%20AWS%20ECS%20using%20Docker%20and%20FastAPI/app/model/model_inference.py)

step3: we create the [FastAPI App](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Deploy%20ML%20Models%20on%20AWS%20ECS%20using%20Docker%20and%20FastAPI/app/main.py)

step4: we [Dockerize](https://github.com/yvt-ee/MUGC-Language-Detection/blob/main/Deploy%20ML%20Models%20on%20AWS%20ECS%20using%20Docker%20and%20FastAPI/Dockerfile) the above FastAPI App

And we run the docker on your local machine and go to the project’s root dir and then execute the below commands in the terminal

```python
docker build -t <your_docker_hub_username>/language-detection-app .
```

Once the image is built then we can run the container by using below command.


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

