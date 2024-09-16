

# The Architecture of AWS development


<img width="716" alt="Screenshot 2024-09-14 at 11 59 46 PM" src="https://github.com/user-attachments/assets/2e1b83d8-974b-479b-ace6-b7102773c457">


To deploy a language detect webpage using AWS, we first need to load the model we trained to AWS, which is why we use docker to push it to docker hub. Since AWS ECS allow us to use the container on AWS. We create a task on AWS point to the image on doker.

![image](https://github.com/user-attachments/assets/c8c6c447-633e-48a6-8203-e08fb2a01a1d)

![image](https://github.com/user-attachments/assets/4373878d-a143-4ce9-abc5-c5837d05356d)

Upon that, we need to use Amplify to deploy the front end 

![image](https://github.com/user-attachments/assets/5329b845-46e8-419f-966d-3ebd89380b4a)


Lambda to triger the function

![image](https://github.com/user-attachments/assets/9dfa5ffc-4c00-486b-b39c-40bf88dc4cb2)

And a database-DynamoDB to store the result.

![image](https://github.com/user-attachments/assets/4db8a820-6f8f-4352-b977-c87110d0cd81)


Besides that, we need S3 to store the images we gonna use on the webpage

![image](https://github.com/user-attachments/assets/32cce454-eef1-46d3-8bd4-9c8326791965)

