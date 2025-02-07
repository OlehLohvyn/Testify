#!/bin/bash

# Check if both arguments are provided
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <DB_PASSWORD> <SECRET_NAME>"
  exit 1
fi

# Set values from arguments
DB_PASSWORD=$1
SECRET_NAME=$2

# Create Kubernetes secret
kubectl create secret generic $SECRET_NAME --from-literal=DB_PASSWORD=$DB_PASSWORD

# Check if the secret was created successfully
if [ $? -eq 0 ]; then
  echo "Secret '$SECRET_NAME' created successfully!"
else
  echo "Error creating secret!"
fi
