# naive_base
Naive Bayes Classifier for CSV Data – Version 1.0

The user selects one CSV file from multiple available files

Right after selection, the system automatically runs an accuracy test on the model

The user selects values for the desired columns

The system returns prediction results with confidence percentages for each value and a final result

## How to Run???
1. Build the Docker image using the Dockerfile:
```bash
docker build -t naive_base:v1 . 
```
2. Run a container from the image:
```bash
docker run -d -p 8001:8001 --name my_naive naive_base:v1
```
# Access
```bash
run run_maneser from the client folder
open the browser at: http://localhost:8001
```
