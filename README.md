### GitHub Actions k8s demo: k3d & helm playground

This is a demo of how K3d can be used as part of a GitHub Actions Workflow for testing Helm charts.

[![CICD](https://github.com/adavarski/chaos-assesment-k8s/workflows/CICD/badge.svg)](https://github.com/adavarski/chaos-assesment-k8s/actions)

K8s is Kubernetes. K3s is a lightweight K8s distribution. K3d is a wrapper to run K3s in Docker. K3d/K3s are especially good for development and CI purposes, as it takes only 20-30 seconds of time till the cluster is ready (for comparison, Kind/Minikube takes more time till ready)

### GitHub Actions configure
- Settings -> Developer settings -> Personal access tokens -> Create GHAT
- Repo Actions secrets and variables -> Add GHAT variable with value above PAT
- Repo Settings -> Actions -> Genreal -> Workflow permissions -> Check Read and write permissions & Allow GH Actions to approve PR

GH Actions workflow: Test Python Code -> Build/Push Image ->  Deploy/Test Helm Chart on K8s -> Update Helm Chart (Image Tag -> for example: ArgoCD to use it: `infra repo:helm charts` and do CD -> Ref: https://github.com/adavarski/ArgoCD-GitOps-playground && https://github.com/adavarski/homelab

#### 1. Create the Web Service (File: app.py)

Defines two endpoints, /greet and /health.
/greet returns a personalized greeting or a default message if the name parameter is missing.
/health checks the server status, returning {"status": "ok"} for monitoring.

#### 2. Dockerize the Application (File: Dockerfile)

Note: Uses python:3.9-slim for a smaller image. Installs Flask and sets up the /app directory. Exposes port 8080 and runs app.py.

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

Use curl for testing:
```
$ curl "http://localhost:8080/greet?name=adavarski"
{"message":"Hello adavarski!"}

$ curl "http://localhost:8080/greet"
{"message":"Now everyone can be a hero..."}

$ curl "http://localhost:8080/health"
{"status":"ok"}
```

