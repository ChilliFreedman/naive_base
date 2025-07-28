# naive_base
Naive Bayes Classifier for CSV Data – Version 1.0

The user selects one CSV file from multiple available files

Right after selection, the system automatically runs an accuracy test on the model

The user selects values for the desired columns

The system returns prediction results with confidence percentages for each value and a final result

## How to Run???
1. Build the Docker image using the Dockerfile:
docker build -t classifier_image .

2. Run a container from the image:
docker run -d -p 8000:8000 classifier_image

3. Then you can access the server:
Either run run_maneser from the client folder
Or open the browser at: http://localhost:8000

