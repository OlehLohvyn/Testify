## About Project

[Link to Figma Project](https://www.figma.com/design/bZFeDHTvUClLRDUQ0qix3s/Testify?node-id=0-1&t=7d5QjOapUCQld9nB-1)

### Development Principles
- Scalability
- Unit tests
- Documentation


# Managing and Monitoring  Minikube Kubernetes Cluster and PostgreSQL Database

### 1. **Start Minikube:**
   - **Command:** `minikube start`
   - **Purpose:** Initializes your local Kubernetes cluster and starts the necessary components like the control plane and kubelet. If the cluster isn't running, this command will launch it. It's essential to run this before you can interact with Kubernetes resources.

### 2. **Check Minikube Status:**
   - **Command:** `minikube status`
   - **Purpose:** This command displays the status of the Minikube cluster. It checks the status of key components like the control plane, kubelet, and apiserver. You can use this to confirm that Minikube is running correctly and that all components are online.

### 3. **List Running Pods:**
   - **Command:** `kubectl get pods`
   - **Purpose:** This command lists all the pods running in your cluster. It shows the pod names, their statuses (whether they're running or not), and other details like restarts and uptime. You can use it to check if your PostgreSQL database (or other services) is running.

### Additional Command to Access Database:
   - **Command:** `kubectl exec -it <pod_name> -- psql -U app_user -d app_db`
   - **Purpose:** This allows you to enter the PostgreSQL pod and interact with the database. Replace `<pod_name>` with the actual name of the pod where your PostgreSQL database is running. The command opens a `psql` session using the `app_user` and the `app_db` database.

These commands help in managing your local Kubernetes cluster with Minikube, monitoring its status, and ensuring that your database is accessible and running properly.