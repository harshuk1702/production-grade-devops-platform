# Production-Grade DevOps Platform

A hands-on DevOps project focused on building a reliable application delivery platform using containerization, automated testing, CI/CD, Kubernetes, security scanning, progressive delivery, and observability.

The platform is being built incrementally. Each stage is implemented, tested, validated, documented, and committed to Git.

---

## Current Status

The application, containerization, CI/CD, security, and Kubernetes foundations are implemented and validated.

### Implemented

- FastAPI application
- Automated API tests with Pytest
- Docker containerization
- Docker health check
- Non-root container execution
- Container security hardening
- GitHub Actions CI
- Docker image build in CI
- Trivy container vulnerability scanning
- Kubernetes manifest validation
- GitHub Container Registry publishing
- Kubernetes Deployment
- Kubernetes Service
- RollingUpdate deployment strategy
- Readiness probe
- Liveness probe
- CPU and memory resource requests and limits
- Kubernetes container security context

### Currently Being Built

- Application metrics
- Prometheus
- Grafana
- Kubernetes observability

### Planned

- Canary deployments
- Traffic management
- Automated promotion and rollback
- Centralized logging
- SLOs and alerting
- Remote/cloud Kubernetes deployment

---

## Architecture

### Current Architecture

```text
Developer
    |
    v
Git Repository
    |
    v
GitHub Actions
    |
    +----------------------+
    |                      |
    v                      v
Pytest Tests          Docker Build
                           |
                           v
                    Trivy Security Scan
                           |
                           v
                  Kubernetes Validation
                           |
                           v
                 GitHub Container Registry
                           |
                           v
                     Kubernetes
                           |
                    +------+------+
                    |             |
                    v             v
              Deployment      ClusterIP
              2 replicas       Service
                    |
              RollingUpdate
                    |
          +---------+---------+
          |                   |
          v                   v
    Readiness Probe      Liveness Probe
          |                   |
          +---------+---------+
                    |
                    v
              FastAPI API
```

### Target Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI/CD
    |
    +--------------------+
    |                    |
    v                    v
Automated Tests      Docker Build
                         |
                         v
                  Security Scanning
                         |
                         v
                 Container Registry
                         |
                         v
                    Kubernetes
                         |
              +----------+----------+
              |                     |
              v                     v
           Stable                Canary
              |                     |
              +----------+----------+
                         |
                         v
                 Traffic Management
                         |
                         v
                   Observability
                 /       |        \
                /        |         \
           Metrics      Logs     Traces
              |
              v
       Prometheus / Grafana
              |
              v
       SLOs / Alerting
              |
              v
      Automated Rollback
```

The target architecture represents the planned final state of the platform. Components are marked as implemented only after they have been deployed and validated.

---

## Technology Stack

### Application

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- HTTPX

### Containerization

- Docker
- Python 3.13 slim base image
- Docker health checks
- Non-root execution
- Linux package updates
- Container security hardening

### CI/CD

- GitHub Actions
- Automated testing
- Docker image builds
- Trivy vulnerability scanning
- Kubernetes manifest validation
- GitHub Container Registry

### Kubernetes

- Kubernetes
- Deployment
- Service
- RollingUpdate strategy
- Readiness probes
- Liveness probes
- Resource requests and limits
- SecurityContext
- GHCR imagePullSecret

### Planned Observability

- Prometheus
- Grafana
- Application metrics
- Kubernetes metrics
- Centralized logging
- SLOs and alerting

### Planned Progressive Delivery

- Canary deployments
- Traffic management
- Automated promotion
- Automated rollback

---

## Application

The FastAPI application exposes the following endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /` | Application root |
| `GET /health` | Application health check |
| `GET /api/products` | Product data |
| `GET /api/orders` | Order data |
| `GET /docs` | Swagger UI |

FastAPI automatically provides OpenAPI documentation through the Swagger interface.

---

## Testing

Automated API tests are implemented using Pytest.

Run the tests locally:

```powershell
cd application
.\.venv\Scripts\Activate.ps1
pytest
```

Current validation:

```text
4 passed
```

The test suite validates the application's main API behaviour.

---

## Docker

The application is packaged as a Docker image.

### Build the Image

```powershell
docker build -t devops-demo-api:1.2.0 ./application
```

For CI-style testing:

```powershell
docker build -t devops-demo-api:ci ./application
```

### Run the Container

```powershell
docker run -d --name devops-demo-api -p 8000:8000 devops-demo-api:1.2.0
```

### Check the Container

```powershell
docker ps
```

The Docker image includes a health check against:

```text
/health
```

The container runs as a non-root user with UID `10001`.

### Verify Container User

```powershell
docker exec devops-demo-api whoami
```

Expected result:

```text
appuser
```

---

## Container Security

The container image is hardened to reduce the attack surface.

The Dockerfile:

- Uses the slim Python base image
- Updates installed OS packages
- Installs application dependencies
- Creates a dedicated non-root user
- Runs the application as UID `10001`
- Avoids root execution at runtime
- Provides a container health check

Kubernetes additionally enforces:

```text
runAsUser: 10001
runAsGroup: 10001
runAsNonRoot: true
allowPrivilegeEscalation: false
capabilities:
  drop:
    - ALL
```

---

## CI Pipeline

GitHub Actions runs automatically on:

- Pushes to `main`
- Pull requests targeting `main`

The CI workflow performs the following stages:

```text
Checkout
   |
   v
Setup Python 3.13
   |
   v
Install Dependencies
   |
   v
Run Pytest
   |
   v
Build Docker Image
   |
   v
Trivy Vulnerability Scan
   |
   v
Validate Kubernetes Manifests
   |
   v
Login to GHCR
   |
   v
Tag Docker Image
   |
   v
Push Docker Images
```

### CI Validation

The pipeline validates:

- Application tests
- Docker image build
- Container vulnerabilities
- Kubernetes manifests
- Container registry publishing

The vulnerability scanner is configured to fail the pipeline when unresolved `HIGH` or `CRITICAL` vulnerabilities are detected.

```yaml
severity: CRITICAL,HIGH
ignore-unfixed: true
exit-code: "1"
```

---

## Container Registry

Docker images are published to GitHub Container Registry.

The image repository follows:

```text
ghcr.io/<github-owner>/devops-demo-api
```

The CI pipeline publishes:

```text
:ci
:<commit-sha>
```

The Kubernetes Deployment uses an immutable commit-SHA image reference.

---

## Kubernetes

The application is deployed to Kubernetes using a Deployment and Service.

### Deployment

The Deployment runs:

```text
2 replicas
```

The deployment strategy is:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 0
    maxSurge: 1
```

This ensures that Kubernetes maintains application availability during a rolling update.

### Service

The application is exposed internally through a Kubernetes `ClusterIP` Service.

```text
Service
  |
  v
devops-demo-api:8000
  |
  v
Application Pods
```

### Resource Management

Each container requests:

```text
CPU:    100m
Memory: 128Mi
```

and has limits of:

```text
CPU:    500m
Memory: 512Mi
```

### Readiness Probe

The readiness probe checks:

```text
GET /
```

A pod must become ready before Kubernetes sends it traffic.

### Liveness Probe

The liveness probe also checks:

```text
GET /
```

If the application becomes unhealthy, Kubernetes can restart the container.

---

## Kubernetes Validation

Check the cluster:

```powershell
kubectl get nodes
```

Check application pods:

```powershell
kubectl get pods -l app=devops-demo-api
```

Check the Deployment:

```powershell
kubectl get deployment devops-demo-api
```

Check the Service:

```powershell
kubectl get service devops-demo-api
```

Check Deployment details:

```powershell
kubectl describe deployment devops-demo-api
```

Check rollout status:

```powershell
kubectl rollout status deployment/devops-demo-api
```

Expected deployment state:

```text
READY       2/2
UP-TO-DATE  2
AVAILABLE   2
```

---

## Rolling Updates

The Kubernetes Deployment uses a rolling update strategy.

The update process is:

```text
Existing Version
      |
      v
Create New Pod
      |
      v
Readiness Probe
      |
      v
New Pod Becomes Ready
      |
      v
Terminate Old Pod
      |
      v
Repeat
      |
      v
New Version Fully Deployed
```

The rollout can be inspected using:

```powershell
kubectl rollout status deployment/devops-demo-api
```

Deployment history:

```powershell
kubectl rollout history deployment/devops-demo-api
```

---

## Repository Structure

```text
production-grade-devops-platform/
|
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── application/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_api.py
│   │
│   ├── Dockerfile
│   ├── pytest.ini
│   └── requirements.txt
│
├── docs/
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── scripts/
│   └── deploy.ps1
│
├── .gitignore
└── README.md
```

---

## Implementation Roadmap

### Phase 1 — Application Foundation

- [x] FastAPI application
- [x] Health endpoint
- [x] API endpoints
- [x] Automated tests

### Phase 2 — Containerization

- [x] Dockerfile
- [x] Docker image
- [x] Docker health check
- [x] Non-root container user
- [x] Container validation
- [x] Container security hardening

### Phase 3 — CI/CD

- [x] GitHub Actions
- [x] Automated test pipeline
- [x] Docker image build in CI
- [x] Container vulnerability scanning
- [x] Kubernetes manifest validation
- [x] GitHub Container Registry
- [x] Commit-SHA image tagging

### Phase 4 — Kubernetes

- [x] Kubernetes Deployment
- [x] Kubernetes Service
- [x] Readiness probe
- [x] Liveness probe
- [x] Resource requests and limits
- [x] Kubernetes security context
- [x] RollingUpdate strategy
- [ ] ConfigMap / application Secrets

### Phase 5 — Progressive Delivery

- [ ] Stable deployment
- [ ] Canary deployment
- [ ] Traffic management
- [ ] Canary validation
- [ ] Automated promotion
- [ ] Automated rollback

### Phase 6 — Observability

- [ ] Application metrics
- [ ] Prometheus
- [ ] Grafana
- [ ] Kubernetes metrics
- [ ] Centralized logging
- [ ] Latency monitoring
- [ ] Error-rate monitoring
- [ ] SLOs
- [ ] Alerting

### Phase 7 — Cloud / Remote Kubernetes

- [ ] Remote Kubernetes cluster
- [ ] Cloud container registry integration
- [ ] Remote deployment
- [ ] Production configuration management
- [ ] External traffic management
- [ ] Production observability

---

## Development Approach

The platform is developed in small, verifiable stages.

For each major change:

1. Implement the change
2. Run automated tests
3. Build and validate the container
4. Validate Kubernetes behaviour
5. Measure relevant results
6. Update the documentation
7. Commit the change to Git
8. Push the change to GitHub
9. Verify GitHub Actions

This approach keeps each stage reproducible and provides a clear Git history of the platform's evolution.

---

## Current Milestone

The application delivery foundation is complete.

The platform currently demonstrates:

```text
Application
    +
Testing
    +
Containerization
    +
Container Security
    +
CI/CD
    +
Vulnerability Scanning
    +
Container Registry
    +
Kubernetes
    +
Rolling Updates
    +
Health Checks
```

The next major milestone is **observability**, beginning with application metrics and Prometheus, followed by Grafana dashboards and Kubernetes-level monitoring.