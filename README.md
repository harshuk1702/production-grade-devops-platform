# Production-Grade DevOps Platform

A hands-on DevOps project focused on building a reliable application delivery platform using containerization, automated testing, CI/CD, Kubernetes, security scanning, progressive delivery, and observability.

The platform is being built incrementally. Each stage is implemented, tested, validated, documented, and committed to Git.

---

## Current Status

The application, containerization, CI/CD, security, Kubernetes, application metrics, Prometheus alerting, and Discord notification foundations are implemented and validated.

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
- Application Prometheus metrics
- Prometheus scraping configuration
- PrometheusRule alerting
- Alertmanager configuration
- Discord alert notifications
- AlertmanagerConfig selection using Kubernetes labels
- AlertmanagerConfig namespace selection
- Persistent Alertmanager configuration through Helm values

### Currently Being Built

- Grafana dashboards
- Kubernetes-level observability
- Advanced alerting and SLO monitoring

### Planned

- Canary deployments
- Traffic management
- Automated promotion and rollback
- Centralized logging
- SLOs and advanced alerting
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
                  +--------+--------+
                  |                 |
                  v                 v
             Deployment        ClusterIP
             2 replicas         Service
                  |
             RollingUpdate
                  |
          +-------+-------+
          |               |
          v               v
    Readiness Probe   Liveness Probe
          |               |
          +-------+-------+
                  |
                  v
             FastAPI API
                  |
                  v
        Prometheus Application Metrics
                  |
                  v
             Prometheus
                  |
                  v
          PrometheusRule
                  |
                  v
             Alertmanager
                  |
                  v
              Discord
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
            Metrics      Logs      Traces
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
- prometheus-client

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

### Observability

- Prometheus
- Alertmanager
- Prometheus Operator
- PrometheusRule
- AlertmanagerConfig
- Application metrics
- Discord alert notifications

### Planned Observability

- Grafana
- Kubernetes metrics
- Centralized logging
- SLOs
- Advanced alerting
- Distributed tracing

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
| `GET /api/test-error` | Intentional 500 error for alert validation |
| `GET /metrics/` | Prometheus application metrics |
| `GET /docs` | Swagger UI |

FastAPI automatically provides OpenAPI documentation through the Swagger interface.

The `/api/test-error` endpoint intentionally raises an exception and returns HTTP 500. It is used to validate application error metrics and the Prometheus alerting pipeline.

---

## Application Metrics

The application exposes Prometheus metrics using the `prometheus-client` library.

Two custom metrics are currently implemented:

```text
http_requests_total
http_request_duration_seconds
```

### Request Counter

The `http_requests_total` counter records HTTP requests using the following labels:

```text
method
path
status
```

Example:

```text
http_requests_total{method="GET",path="/",status="200"}
```

### Request Latency

The `http_request_duration_seconds` histogram records HTTP request latency using:

```text
method
path
```

### Exception Handling

Application exceptions are also recorded as HTTP 500 responses by the metrics middleware.

For example:

```text
http_requests_total{method="GET",path="/api/test-error",status="500"}
```

This allows Prometheus to calculate application error rates and trigger alerts based on HTTP 5xx responses.

### Verify Metrics Locally

The `/metrics` endpoint redirects to `/metrics/`, so use `-L` when testing with `curl`:

```powershell
curl.exe -L http://localhost:8080/metrics/
```

To inspect HTTP request metrics:

```powershell
curl.exe -L http://localhost:8080/metrics/ | Select-String "http_requests_total"
```

Example output includes:

```text
http_requests_total{method="GET",path="/",status="200"}
http_requests_total{method="GET",path="/health",status="200"}
http_requests_total{method="GET",path="/api/test-error",status="500"}
```

---

## Testing

Automated API tests are implemented using Pytest.

Run the tests locally:

```powershell
cd application

.\.venv\Scripts\Activate.ps1

pytest
```

The test suite validates the application's main API behaviour and verifies that the metrics endpoint is available.

Current validation:

```text
4 passed
```

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

Example:

```text
ghcr.io/harshuk1702/devops-demo-api:<commit-sha>
```

This ensures that Kubernetes deployments reference a specific immutable image version rather than a mutable tag such as `latest`.

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
CPU:     100m
Memory:  128Mi
```

and has limits of:

```text
CPU:     500m
Memory:  512Mi
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
READY        2/2
UP-TO-DATE   2
AVAILABLE    2
```

### Verify the Deployed Image

```powershell
kubectl get deployment devops-demo-api -o jsonpath="{.spec.template.spec.containers[0].image}"
```

### Verify Application Endpoints

When the application is exposed locally on port `8080`:

```powershell
curl.exe http://localhost:8080/
```

```powershell
curl.exe http://localhost:8080/health
```

### Verify Metrics

Because FastAPI redirects `/metrics` to `/metrics/`, use:

```powershell
curl.exe -L http://localhost:8080/metrics/
```

To inspect request metrics:

```powershell
curl.exe -L http://localhost:8080/metrics/ | Select-String "http_requests_total"
```

---

## Prometheus Observability

Prometheus is used to collect application metrics from the FastAPI service.

The application exposes Prometheus-compatible metrics through:

```text
/metrics/
```

The metrics include:

```text
http_requests_total
http_request_duration_seconds
```

Prometheus can scrape the Kubernetes Service and collect these application-level metrics.

The observability pipeline is:

```text
FastAPI Application
       |
       v
/metrics/
       |
       v
Kubernetes Service
       |
       v
Prometheus
       |
       v
PrometheusRule
       |
       v
Alertmanager
       |
       v
Discord
```

---

## Prometheus Alerting

A PrometheusRule is used to detect elevated HTTP 5xx error rates from the application.

The alert is:

```text
DevOpsDemoAPIHigh5xxRate
```

The alert is based on the application's Prometheus request counter:

```text
http_requests_total
```

The intentional test endpoint:

```text
/api/test-error
```

returns HTTP 500 and increments the metric:

```text
http_requests_total{method="GET",path="/api/test-error",status="500"}
```

This provides a controlled way to validate the complete alerting pipeline.

---

## Alertmanager

Alertmanager receives alerts generated by Prometheus and routes the application alert to the configured Discord receiver.

The Alertmanager configuration uses an `AlertmanagerConfig` resource:

```text
monitoring/devops-demo-discord
```

The configuration is selected using the label:

```yaml
labels:
  alertmanagerConfig: devops-demo
```

The Alertmanager configuration selector is:

```yaml
alertmanagerConfigSelector:
  matchLabels:
    alertmanagerConfig: devops-demo
```

The namespace selector allows Alertmanager to discover matching `AlertmanagerConfig` resources across namespaces:

```yaml
alertmanagerConfigNamespaceSelector: {}
```

The application alert is matched using:

```text
alertname = DevOpsDemoAPIHigh5xxRate
```

---

## Discord Notifications

Alertmanager sends the application alert to Discord.

The Discord notification includes:

```text
Alert name
Service
Severity
Summary
Description
```

The configured notification title is:

```text
DevOps Demo API Alert
```

Resolved notifications are enabled:

```yaml
sendResolved: true
```

The Discord webhook is stored in a Kubernetes Secret rather than directly in the Git repository.

The AlertmanagerConfig references:

```yaml
apiURL:
  name: discord-webhook
  key: webhook-url
```

This prevents the actual Discord webhook URL from being committed to Git.

---

## Alertmanager Configuration Persistence

The Alertmanager configuration selector is persisted through:

```text
k8s/monitoring-values.yaml
```

The relevant configuration is:

```yaml
alertmanager:
  alertmanagerSpec:
    alertmanagerConfigSelector:
      matchLabels:
        alertmanagerConfig: devops-demo
    alertmanagerConfigNamespaceSelector: {}
```

This ensures that the Alertmanager configuration selection survives a Helm-based monitoring deployment or upgrade.

---

## Alert Validation

The application error endpoint can be used to generate a controlled HTTP 500 response:

```powershell
curl.exe -s -o NUL -w "%{http_code}`n" http://localhost:8080/api/test-error
```

Expected result:

```text
500
```

After generating the error traffic, verify the application metric:

```powershell
curl.exe -L http://localhost:8080/metrics/ | Select-String "http_requests_total"
```

The output should contain a metric similar to:

```text
http_requests_total{method="GET",path="/api/test-error",status="500"}
```

This confirms that:

```text
HTTP Request
    |
    v
FastAPI
    |
    v
HTTP 500
    |
    v
Application Metric
    |
    v
Prometheus
    |
    v
PrometheusRule
    |
    v
Alertmanager
    |
    v
Discord
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

A previous revision can be rolled back using:

```powershell
kubectl rollout undo deployment/devops-demo-api
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
│   ├── alertmanagerconfig.yaml
│   ├── deployment.yaml
│   ├── monitoring-values.yaml
│   ├── prometheusrule.yaml
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

### Phase 5 — Observability

- [x] Application metrics
- [x] Prometheus
- [ ] Grafana
- [ ] Kubernetes metrics
- [ ] Centralized logging
- [x] HTTP 5xx monitoring
- [x] PrometheusRule
- [x] Alertmanager
- [x] Discord notifications
- [ ] Latency monitoring
- [ ] SLOs
- [ ] Advanced alerting

### Phase 6 — Progressive Delivery

- [ ] Stable deployment
- [ ] Canary deployment
- [ ] Traffic management
- [ ] Canary validation
- [ ] Automated promotion
- [ ] Automated rollback

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

The application delivery and initial observability foundation is complete.

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
    +
Application Metrics
    +
Prometheus
    +
PrometheusRule
    +
Alertmanager
    +
Discord Notifications
```

The next major milestone is **advanced observability**, beginning with Grafana dashboards and Kubernetes-level monitoring, followed by SLOs, centralized logging, and more advanced alerting.

---