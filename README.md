## About Project

[Link to Figma Project](https://www.figma.com/design/bZFeDHTvUClLRDUQ0qix3s/Testify?node-id=0-1&t=7d5QjOapUCQld9nB-1)

### Development Principles
- Scalability
- Unit tests
- Documentation

---
# Deployment Instructions for Kubernetes

## Prerequisites
- Installed [Minikube](https://minikube.sigs.k8s.io/docs/)
- Installed [kubectl](https://kubernetes.io/docs/tasks/tools/)
- Installed [Docker](https://www.docker.com/)
- Git installed

## Steps to Deploy

### 1. Clone the Repository
```sh
git clone https://github.com/OlehLohvyn/Testify.git
cd Testify
```

### 2. Start Minikube
```sh
minikube start
```

### 3. Apply Kubernetes Configurations
Run the following command to deploy all configurations from the `k8s` directory:
```sh
kubectl apply -f k8s/
```

### 4. Verify Deployments
Check if all pods are running correctly:
```sh
kubectl get pods
```

Check if services are running:
```sh
kubectl get services
```

### 5. Access the DRF Application
Find the Minikube service URL:
```sh
minikube service drf-app-service --url
```
Use the provided URL to access the Django REST Framework application.

### 6. (Optional) Debugging
If something goes wrong, check logs:
```sh
kubectl logs -l app=drf-app
```
To describe a pod for detailed info:
```sh
kubectl describe pod <pod-name>
```

### 7. Stop and Cleanup
To stop Minikube:
```sh
minikube stop
```
To delete everything:
```sh
kubectl delete -f k8s/
```

