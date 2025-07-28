# Naive Bayes CSV Classification System – Version 0.2

1. Training Service
Receives a CSV file from the user

Loads the file into a DataFrame

Trains a Naive Bayes model

Runs a test and returns the model's accuracy

Sends the trained model to the second service

2. Classification Service
Receives the trained model from the first service

Lets the user select values for specific columns

Uses the model to classify the input

Returns prediction results and confidence scores

# Create a Docker network so both services can communicate:
```bash
docker network create naive_net
```
# Build the images (each from its subfolder):
```bash
docker build -t model_image -f model_server/Dockerfile . 
docker build -t classifier_image -f classifier_server/Dockerfile . 
```
# Run the containers on the same network:
```bash
docker run -d --name model_container --network naive_net -p 8001:8001 model_image
docker run -d --name classifier_container --network naive_net -p 8002:8002 classifier_image
```


# Access
```bash
run client.run_maneser
Training API available at: http://localhost:8001
Classification API available at: http://localhost:8002
```