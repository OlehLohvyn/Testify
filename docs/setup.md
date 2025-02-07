# Setup Environment for Testify

## Prerequisites
- Installed [Minikube](https://minikube.sigs.k8s.io/docs/)
- Installed [kubectl](https://kubernetes.io/docs/tasks/tools/)
- Installed [Docker](https://www.docker.com/)
- Git installed

## Steps to Setup

### 1. Clone the Repository
```sh
git clone https://github.com/OlehLohvyn/Testify.git
cd Testify
```

### 2. Create Kubernetes Secrets
Before deploying the application, you need to create the necessary secrets for the PostgreSQL database. These secrets will store sensitive data such as the database password.

To create the secrets, you can use the following scripts:

- **For Windows (PowerShell):**

  ```sh
  .\scripts\create-secrets.ps1 -DB_PASSWORD <your-db-password> -SECRET_NAME <your-secret-name>
  ```

  - Replace `<your-db-password>` with the desired database password.
  - Replace `<your-secret-name>` with a name for the secret.

  Example:
  ```sh
  .\scripts\create-secrets.ps1 -DB_PASSWORD "your_secure_password" -SECRET_NAME "db-secret"
  ```

- **For Linux/macOS (Bash):**

  ```sh
  ./scripts/create-secrets.sh <your-db-password> <your-secret-name>
  ```

  - Replace `<your-db-password>` with the desired database password.
  - Replace `<your-secret-name>` with a name for the secret.

  Example:
  ```sh
  ./scripts/create-secrets.sh "your_secure_password" "db-secret"
  ```

These scripts will generate the required secrets in Kubernetes for your database.

### 3. Start Minikube
```sh
minikube start
```

### 4. Apply Kubernetes Configurations
Run the following command to deploy all configurations from the `k8s` directory:
```sh
kubectl apply -f k8s/
```

### 5. Verify Deployments
Check if all pods are running correctly:
```sh
kubectl get pods
```

Check if services are running:
```sh
kubectl get services
```

### 6. Access the DRF Application
Find the Minikube service URL:
```sh
minikube service drf-app-service --url
```
Use the provided URL to access the Django REST Framework application.

Once the application is deployed, run the following command to apply Django migrations:

```sh
kubectl exec -it <pod_name> -- python testify/manage.py migrate
```

This will set up the necessary database tables.
