param (
    [string]$DB_PASSWORD,
    [string]$SECRET_NAME
)

# Check if both arguments are provided
if (-not $DB_PASSWORD -or -not $SECRET_NAME) {
    Write-Host "Usage: .\create-secrets.ps1 <DB_PASSWORD> <SECRET_NAME>"
    exit
}

# Create Kubernetes secret
kubectl create secret generic $SECRET_NAME --from-literal=DB_PASSWORD=$DB_PASSWORD

# Check if the secret was created successfully
if ($?) {
    Write-Host "Secret '$SECRET_NAME' created successfully!"
} else {
    Write-Host "Error creating secret!"
}
