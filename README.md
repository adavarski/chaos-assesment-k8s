[![CICD](https://github.com/adavarski/chaos-assesment-k8s/workflows/CICD/badge.svg)](https://github.com/adavarski/chaos-assesment-k8s/actions)



```
Task:
========

Write a standard web service that serves a straightforward API. The service has to be containerized. It will act as a small microservice displaying greeting text based on a query parameter.

Requirements:
Programming Language & Framework:
Choose a programming language you are comfortable with (Python, Go, NodeJS).
Create a web application using a simple web framework (e.g., for Python, Flask, for Node.js, Express, or built-in net/http for Go).

Web Server Functionality:
The web server should be listening to port 8080.
Create a new API and add: GET /greet endpoint.
This endpoint should perform a GET request and accept a query parameter name.
The server response should be a dictionary JSON as {"message": "Hello !"}.
If the name parameter is missing, the server reply should be “Now everyone can be a hero...:,”.

Dockerization:
Prepare a Dockerfile to dockerize the web server.
Make sure that the docker image is relatively thin and well-optimized.

Testing & Validation:
Open a web browser and ensure the service is available at http://localhost:8080/greet?name=YourName.
Test the service by sending a few requests using different name values.

Bonus:
Create a health check (GET /health) for the service that accepts a request and returns a JSON response regarding the status of the service (e.g., severity level returned as {"status": "ok"}).
Add a CI/CD pipeline script (e.g., GitHub Actions, Jenkins, Gitlab) that builds a Docker image, starts the service, and runs a basic test suite against the running container.

-------------------------
Create Helm chart for app
Deploy app to k8s (k3d)
```
Task steps:

#### 1. Create the Web Service (File: app.py)

Defines two endpoints, /greet and /health.
/greet returns a personalized greeting or a default message if the name parameter is missing.
/health checks the server status, returning {"status": "ok"} for monitoring.

#### 2. Dockerize the Application (File: Dockerfile)

Note: Uses python:3.10-alpine for a smaller image. Installs Flask and sets up the /app directory. Exposes port 8080 and runs app.py.

#### 3. Build and Run the Docker Container

Build the Docker image:

```
docker build -t hello-app .
```
Run the Docker container:

```
docker run -d -p 8080:8080 hello-app
```
#### 4. Test endpoints:

```
$ curl "http://localhost:8080/greet?name=John"
{"message":"Hello John!"}

$ curl "http://localhost:8080/greet"
{"message":"Now everyone can be a hero..."}

$ curl "http://localhost:8080/health"
OK



 docker ps -a
CONTAINER ID   IMAGE       COMMAND            CREATED          STATUS          PORTS                                       NAMES
b560839c5122   hello-app   "python3 app.py"   18 seconds ago   Up 17 seconds   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   practical_faraday



 $ docker exec -it b560839c5122 python -m pytest
=============================================================================================== test session starts ===============================================================================================
platform linux -- Python 3.10.15, pytest-8.3.3, pluggy-1.5.0
rootdir: /app
collected 3 items                                                                                                                                                                                                 

tests/test_health.py .                                                                                                                                                                                      [ 33%]
tests/test_index.py .                                                                                                                                                                                       [ 66%]
tests/test_name.py .                                                                                                                                                                                        [100%]

================================================================================================ 3 passed in 0.02s ================================================================================================

Explanation of Each Test
test_greet_with_name:

Sends a request to /greet with name=John.
Checks if the status code is 200 (OK).
Ensures the response is JSON and matches {"message": "Hello John!"}.

test_greet_without_name:

Sends a request to /greet without the name query parameter.
Checks if the status code is 200 (OK).
Ensures the response is JSON and matches {"message": "Now everyone can be a hero..."}.

test_health:

Sends a request to /health.
Checks if the status code is 200 (OK).
Verifies the response data is exactly "OK" as a byte string.


```



### GitHub Actions: k8s (k3d) & helm deploy

K8s is Kubernetes. K3s is a lightweight K8s distribution. K3d is a wrapper to run K3s in Docker. K3d/K3s are especially good for development and CI purposes, as it takes only 20-30 seconds of time till the cluster is ready (for comparison, Kind/Minikube takes more time till ready)

### GitHub Actions configure

Add GITHUB_USERNAME & DOCKERHUB_TOKEN & GHAT repo variables

GHAT notes:

- Settings -> Developer settings -> Personal access tokens -> Create GHAT
- Repo Actions secrets and variables -> Add GHAT variable with value above PAT
- Repo Settings -> Actions -> Genreal -> Workflow permissions -> Check Read and write permissions & Allow GH Actions to approve PR

GH Actions workflow: Test Python Code -> Build/Push Image ->  Deploy/Test Helm Chart on K8s -> Update Helm Chart

