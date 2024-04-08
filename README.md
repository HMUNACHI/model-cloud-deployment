# Model Deployment Demonstration for Beginners

This repository demonstrates how to build a machine learning model into an API and deploy it on various cloud services. The project uses a Hugging Face opinion mining model, Flask for API creation, and Docker for containerization.

## Project Structure

- `Dockerfile`: Contains instructions for building the Docker image.
- `app.py`: Contains Flask APIs that interacts with the machine learning model.
- `model.py`: Contains the Hugging Face model.
- `requirements.txt`: Contains the necessary Python dependencies.

## Local Deployment

1. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Build the Docker image:
    ```bash
    docker build -t model-api .
    ```

3. Run the Docker container:
    ```bash
    docker run -p 5000:5000 model-api
    ```

4. The API should now be accessible at `http://localhost:5000`.

## API Usage

The API endpoint is `/feedback` and it accepts POST requests. The request body should be a JSON object with a `text` field containing the text to analyze.

### Python Requests

You can use the `requests` library in Python to send a POST request:

```python
import requests
import json

url = "http://localhost:5000/feedback"
data = {"text": "Your text here"}
response = requests.post(url, data=json.dumps(data))

print(response.json())
```

Alternatively, you can use cURL to send a POST request from the command line:

```python
curl -X POST -H "Content-Type: application/json" -d '{"text":"Your text here"}' http://localhost:5000/feedback
```


## Deployment on Google Cloud Run

1. Build the Docker image and push it to Google Container Registry (GCR):
    ```bash
    gcloud builds submit --tag gcr.io/PROJECT-ID/model-api
    ```

2. Deploy the image to Cloud Run:
    ```bash
    gcloud run deploy --image gcr.io/PROJECT-ID/model-api --platform managed
    ```

## Deployment on AWS Elastic Beanstalk

1. Create a Docker run configuration file named `Dockerrun.aws.json`.

2. Initialize your Elastic Beanstalk environment:
    ```bash
    eb init -p docker your-app-name
    ```

3. Create an environment and deploy your application:
    ```bash
    eb create your-env-name
    ```

## Deployment on Azure App Service

1. Create a Docker image and push it to Docker Hub or Azure Container Registry (ACR).

2. Create a new App Service on Azure portal.

3. In the Deployment Center, choose Docker Container for the source and select the Docker image you pushed.

4. Click on Run API and your API should be live.

Please refer to the official documentation of each cloud service for more detailed instructions and troubleshooting. Each service has ways to attach domains.

## Implementing API Keys into the Endpoint

To secure your API, you can implement API key authentication. This involves modifying your Flask application to require an API key with each request.

Here's a simple example of how you can do this:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/feedback', methods=['POST'])
def feedback():
    api_key = request.headers.get('X-API-KEY')
    if not api_key or api_key != 'YOUR_API_KEY':
        return jsonify({'message': 'Invalid API Key'}), 403

    # Your existing code here...

if __name__ == '__main__':
    app.run(debug=True)
```

Again, each cloud service has functionalities for managing API keys.