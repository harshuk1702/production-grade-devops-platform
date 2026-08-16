$ErrorActionPreference = "Stop"

$SHA = git rev-parse HEAD

Write-Host "Deploying image:"
Write-Host "ghcr.io/harshuk1702/devops-demo-api:$SHA"

kubectl set image deployment/devops-demo-api `
  devops-demo-api=ghcr.io/harshuk1702/devops-demo-api:$SHA

kubectl rollout status deployment/devops-demo-api

kubectl get pods