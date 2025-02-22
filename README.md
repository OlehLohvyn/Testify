# Testify Project Documentation


## Project Overview

This project is a Django REST Framework (DRF) application with PostgreSQL, deployed using Kubernetes and Minikube. It follows principles of scalability, unit tests, and documentation.

## Setup and Deployment

For detailed instructions on how to set up and deploy the project, refer to the [Setup and Deployment guide](docs/setup.md).

## Secrets Management

For managing database passwords securely, we use Kubernetes secrets. For detailed instructions on how to create secrets, refer to the [Secrets Management guide](docs/secrets_management.md).

## Debugging and Troubleshooting

For debugging and troubleshooting tips, refer to the [Debugging and Troubleshooting guide](docs/debugging.md).

##  API Documentation

This project leverages Swagger (using the [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) package) to automatically generate API documentation. This allows developers to quickly review available endpoints, parameters, and responses, and even test API calls directly from the browser.

### Accessing Swagger Documentation in Kubernetes

Since the project is running inside a Kubernetes cluster, the Swagger UI is not available on `localhost`. Instead, you need to expose the service and retrieve the correct URL.

To get the accessible URL for Swagger, run:
```powershell
minikube service drf-app-service --url
```
This will return an output similar to:
```
http://127.0.0.1:54836
```
Use this dynamically assigned URL to access Swagger documentation:

- **Swagger UI:** `http://<your-minikube-url>/swagger/`  
  An interactive interface for browsing endpoints and testing API requests.

- **ReDoc:** `http://<your-minikube-url>/redoc/`  
  An alternative documentation layout with a different design.

- **Swagger JSON:** `http://<your-minikube-url>/swagger.json`  
  The raw JSON file containing the full API specification.

⚠️ **Note:** This URL will change each time you restart minikube. If needed, consider configuring an **Ingress** or **NodePort** to expose a stable API endpoint.






Additional Customization
You can further customize the documentation by modifying the openapi.Info object or by adding additional routes as needed. For more details, please refer to the [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) documentation.