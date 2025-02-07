# Secrets Management

In this project, sensitive data such as database passwords are stored as Kubernetes secrets to ensure their security. These secrets are essential for proper application deployment and functionality.

## Creating Kubernetes Secrets

### 1. Using the PowerShell Script (Windows)

You can create a Kubernetes secret using the `create-secrets.ps1` PowerShell script. This script takes two arguments:

- `DB_PASSWORD`: The password for the database.
- `SECRET_NAME`: The name of the secret to be created.

#### Usage:

```sh
.\scripts\create-secrets.ps1 -DB_PASSWORD <your-db-password> -SECRET_NAME <your-secret-name>
```

Example:

```sh
.\scripts\create-secrets.ps1 -DB_PASSWORD "your_secure_password" -SECRET_NAME "db-secret"
```

### 2. Using the Bash Script (Linux/macOS)

For Linux/macOS, the `create-secrets.sh` script performs the same task. It requires two arguments:

- `DB_PASSWORD`: The password for the database.
- `SECRET_NAME`: The name of the secret to be created.

#### Usage:

```sh
./scripts/create-secrets.sh <your-db-password> <your-secret-name>
```

Example:

```sh
./scripts/create-secrets.sh "your_secure_password" "db-secret"
```

These scripts will generate the required Kubernetes secrets with the given database password.

## Storing and Managing Secrets in Kubernetes

Kubernetes secrets are stored and managed using the Kubernetes API. The secrets are base64-encoded and can be mounted as environment variables or files inside the application pods.

### Secret Usage in the DRF Application

In the `drf-app` deployment, the secrets are referenced in the following way:

- The `DB_PASSWORD` secret is pulled from Kubernetes and injected as an environment variable in the `drf-app` container.
- The secret is also mounted as a volume to `/etc/secrets` inside the container to ensure that the application can securely access it.

This method ensures that sensitive data, like passwords, are not hard-coded in the application or exposed in the repository.
