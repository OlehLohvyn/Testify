## About Project

[Link to Figma Project](https://www.figma.com/design/bZFeDHTvUClLRDUQ0qix3s/Testify?node-id=0-1&t=7d5QjOapUCQld9nB-1)

### Development Principles
- Scalability
- Unit tests
- Documentation

---

## How to Run the Project in Kubernetes

1. **Clone the Repository**

   Start by cloning the repository using Git:
   ```bash
   git clone https://your-repository-url.git
   cd your-repository
   ```

2. **Create a Virtual Environment and Install Dependencies**

   Create a virtual environment:
   ```bash
   python -m venv venv
   ```

   Activate it:
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```

   Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build the Docker Image**

   - Build the Docker image for your app:
     ```bash
     docker build -t olehlohvyn2003/my-drf-app:latest .
     ```

4. **Deploy the App and Service in Kubernetes**

   Navigate to the directory with your YAML files:
   ```bash
   cd k8s
   ```

   Apply all the necessary Kubernetes files to deploy the app and the service:
   ```bash
   kubectl apply -f .
   ```

   Make sure all resources have been successfully deployed:
   ```bash
   kubectl get pods
   kubectl get svc
   ```

5. **Check Service Availability**

   To check if your app is running correctly, use the following command to get the service URL:
   ```bash
   minikube service drf-app-service --url
   ```
