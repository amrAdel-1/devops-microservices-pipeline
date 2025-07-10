# DevOps Microservices Pipeline 🚀

This project demonstrates a complete CI/CD pipeline for a microservices-based application using Docker, Kubernetes, and Jenkins.

---

## 📦 Services Included

- **Auth Service**
- **Product Service**
- **Order Service**

Each service has:
- Its own `Dockerfile`
- A standalone `Jenkinsfile`
- `Kubernetes Deployment` and `Service` YAML files

---

## ⚙️ Tech Stack

- **Docker** – Containerized each microservice
- **Jenkins** – CI/CD pipelines to build, push and deploy services
- **Kubernetes** – Deploying and managing services
- **GitHub** – Version control

---

## 🛠️ CI/CD Workflow

1. Each service is built with Docker.
2. Image is pushed to Docker Hub.
3. Kubernetes deployments/services are applied.
4. Pipelines are managed by individual `Jenkinsfile`s per service.

---

## 🧪 How to Test Locally

1. Clone the repo
2. Navigate into each service and build image manually:

```bash
docker build -t <amradel2002>/auth-service:latest auth-service/
docker push <amradel2002>/auth-service:latest
kubectl apply -f auth-service/auth-deployment.yaml
kubectl apply -f auth-service/auth-service.yaml
