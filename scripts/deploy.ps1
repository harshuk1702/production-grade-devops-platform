$ErrorActionPreference = "Stop"

$Deployment = "devops-demo-api"
$Container = "devops-demo-api"
$ImageRepository = "ghcr.io/harshuk1702/devops-demo-api"
$Namespace = "default"

$SHA = git rev-parse HEAD
$Image = "${ImageRepository}:${SHA}"

Write-Host ""
Write-Host "Checking container image availability..."
Write-Host "Image: $Image"

docker manifest inspect $Image *> $null

if ($LASTEXITCODE -ne 0) {
    throw "Container image is not available in GHCR: $Image"
}

Write-Host "Container image is available."

Write-Host "========================================"
Write-Host "Production Deployment"
Write-Host "========================================"
Write-Host "Deployment : $Deployment"
Write-Host "Namespace  : $Namespace"
Write-Host "Image      : $Image"
Write-Host ""

Write-Host "Checking Kubernetes connectivity..."
kubectl cluster-info

if ($LASTEXITCODE -ne 0) {
    throw "Kubernetes cluster is not reachable."
}

Write-Host ""
Write-Host "Updating deployment image..."

kubectl set image deployment/$Deployment `
    $Container=$Image `
    -n $Namespace

if ($LASTEXITCODE -ne 0) {
    throw "Failed to update deployment image."
}

Write-Host ""
Write-Host "Waiting for rollout..."

kubectl rollout status deployment/$Deployment `
    -n $Namespace `
    --timeout=180s

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Rollout failed. Starting automatic rollback..."

    kubectl rollout undo deployment/$Deployment `
        -n $Namespace

    if ($LASTEXITCODE -ne 0) {
        throw "Rollout failed and automatic rollback also failed."
    }

    kubectl rollout status deployment/$Deployment `
        -n $Namespace `
        --timeout=180s

    if ($LASTEXITCODE -ne 0) {
        throw "Rollback completed but the previous version did not become healthy."
    }

    Write-Host ""
    Write-Host "Rollback completed successfully."
    exit 1
}

Write-Host ""
Write-Host "Rollout completed successfully."

Write-Host ""
Write-Host "Verifying deployment..."

kubectl get deployment $Deployment -n $Namespace

if ($LASTEXITCODE -ne 0) {
    throw "Deployment verification failed."
}

Write-Host ""
Write-Host "Verifying pods..."

kubectl get pods `
    -n $Namespace `
    -l app=$Deployment `
    -o wide

if ($LASTEXITCODE -ne 0) {
    throw "Pod verification failed."
}

Write-Host ""
Write-Host "Verifying running container images..."

$RunningImages = kubectl get pods `
    -n $Namespace `
    -l app=$Deployment `
    -o jsonpath="{range .items[*]}{.spec.containers[0].image}{'\n'}{end}"

if ($LASTEXITCODE -ne 0) {
    throw "Running image verification command failed."
}

Write-Host $RunningImages

$ExpectedImage = $Image

foreach ($RunningImage in $RunningImages) {
    if ($RunningImage -ne $ExpectedImage) {
        throw "Image verification failed. Expected: $ExpectedImage but found: $RunningImage"
    }
}

Write-Host "All running pods are using the expected image."

Write-Host ""
Write-Host "========================================"
Write-Host "Deployment completed successfully."
Write-Host "========================================"