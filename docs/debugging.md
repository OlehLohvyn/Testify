# Debugging

If something goes wrong, check logs:
```sh
kubectl logs -l app=drf-app
```

To describe a pod for detailed info:
```sh
kubectl describe pod <pod-name>
```