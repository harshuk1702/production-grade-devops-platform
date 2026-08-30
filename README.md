# Production-Grade DevOps Platform

A hands-on DevOps project focused on building a reliable application delivery platform using containerization, automated testing, CI/CD, Kubernetes, security scanning, progressive delivery, and observability.

The platform is being built incrementally. Each stage is implemented, tested, validated, documented, and committed to Git.

---

## Current Status

The application delivery platform, containerization, CI/CD, security, Kubernetes deployment, application metrics, Prometheus monitoring, Grafana dashboards, Kubernetes-level observability, Prometheus alerting, Alertmanager routing, and Discord notifications have been implemented and validated.

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

### Implemented Observability

- Grafana dashboards
- Kubernetes-level observability
- kube-state-metrics
- node-exporter
- Application request metrics
- Application latency metrics
- HTTP 5xx error monitoring
- Application availability monitoring
- Application latency alerting
- CPU monitoring and alerting
- Memory monitoring and alerting
- PrometheusRule alerting
- Alertmanager routing
- Discord alert notifications
- Alert recovery notifications

### Currently Being Built

- Service-level objectives (SLOs)
- SLO-based alerting
- Advanced alerting and reliability monitoring

### Planned

- Canary deployments
- Traffic management
- Automated promotion and rollback
- Centralized logging
- Distributed tracing
- Remote/cloud Kubernetes deployment

---

## Architecture

### Current Architecture

The current platform implements the complete application delivery and initial observability pipeline.

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI
    |
    +----------------------+----------------------+
    |                      |                      |
    v                      v                      v
Pytest Tests          Docker Build       Kubernetes Validation
                           |
                           v
                   Trivy Security Scan
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
               Deployment      Service
               2 replicas     ClusterIP
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
          +---------+---------+
          |                   |
          v                   v
   Application Metrics   Application Traffic
          |
          v
      Prometheus
          |
    +-----+----------------------+
    |                            |
    v                            v
PrometheusRule              Grafana
    |
    v
Alertmanager
    |
    v
  Discord
```

The current architecture represents components that have been implemented and validated.

---

## Observability Architecture

The observability layer collects application-level and Kubernetes-level telemetry and provides visualization and alerting.

```text
                    Kubernetes Cluster
                           |
             +-------------+-------------+
             |                           |
             v                           v
       FastAPI Application        Kubernetes Resources
             |                           |
             |                           +-------------------+
             |                           |                   |
             v                           v                   v
      /metrics/ endpoint         kube-state-metrics    node-exporter
             |                           |                   |
             +-------------+-------------+-------------------+
                           |
                           v
                      Prometheus
                           |
                +----------+----------+
                |                     |
                v                     v
             Grafana             PrometheusRule
          Dashboards                  |
                |                     v
                |                Alertmanager
                |                     |
                |                     v
                |                  Discord
                |
                v
        Metrics Visualization
```

### Application Observability

The FastAPI application exposes Prometheus-compatible metrics for:

- Request volume
- HTTP status codes
- HTTP 5xx responses
- Request latency
- Endpoint-level behaviour

The primary application metrics are:

```text
http_requests_total
http_request_duration_seconds
```

### Kubernetes Observability

Kubernetes-level metrics are collected through:

```text
kube-state-metrics
node-exporter
```

These provide visibility into Kubernetes resources and node-level infrastructure metrics.

The observability flow is:

```text
Kubernetes
    |
    +----------------------+
    |                      |
    v                      v
kube-state-metrics    node-exporter
    |                      |
    +----------+-----------+
               |
               v
           Prometheus
               |
               v
            Grafana
```

### Alerting Architecture

Application and Kubernetes metrics are evaluated by Prometheus alerting rules.

```text
Application / Kubernetes Metrics
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

The current alerting layer covers:

- High HTTP 5xx error rate
- High p95 request latency
- Application availability
- High CPU usage
- High memory usage

Alert recovery notifications are enabled through Alertmanager.

---

## Target Architecture

The target architecture represents the planned final state of the platform, including progressive delivery, centralized logging, SLOs, advanced alerting, and automated rollback.

```text
Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions CI/CD
    |
    +----------------------+----------------------+
    |                      |                      |
    v                      v                      v
Automated Tests       Docker Build       Kubernetes Validation
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
             Stable                 Canary
                |                     |
                +----------+----------+
                           |
                           v
                  Traffic Management
                           |
                           v
                  Application Platform
                           |
            +--------------+--------------+
            |              |              |
            v              v              v
         Metrics          Logs          Traces
            |              |              |
            v              v              v
       Prometheus     Log Platform    Trace Platform
            |
            v
          Grafana
            |
            v
       SLOs / Alerting
            |
            v
    Automated Promotion
            |
            v
     Automated Rollback
```

Components are marked as implemented only after they have been deployed and validated.

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
- Commit-SHA image tagging

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
- Grafana
- Alertmanager
- Prometheus Operator
- PrometheusRule
- AlertmanagerConfig
- kube-state-metrics
- node-exporter
- Application metrics
- Kubernetes metrics
- HTTP 5xx monitoring
- Latency monitoring
- CPU monitoring
- Memory monitoring
- Application availability monitoring
- Discord alert notifications
- Alert recovery notifications

### Planned Observability

- Centralized logging
- Service-level objectives (SLOs)
- Advanced SLO-based alerting
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

This metric allows Prometheus to calculate request latency percentiles such as p95 latency.

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

### Port Forwarding

The Kubernetes Service can be exposed locally using:

```powershell
kubectl port-forward svc/devops-demo-api 8080:8000
```

If port `8080` is already being used by another process, use another local port:

```powershell
kubectl port-forward svc/devops-demo-api 8081:8000
```

Then access the application through:

```powershell
curl.exe http://localhost:8081/
```

The local port is independent of the Kubernetes Service port. The format is:

```text
<local-port>:<service-port>
```

---

## Prometheus Observability

Prometheus is used to collect application and Kubernetes metrics.

The FastAPI application exposes Prometheus-compatible metrics through:

```text
/metrics/
```

The application metrics include:

```text
http_requests_total
http_request_duration_seconds
```

Kubernetes-level metrics are provided through:

```text
kube-state-metrics
node-exporter
```

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
       +------------------+
       |                  |
       v                  v
    Grafana         PrometheusRule
                          |
                          v
                     Alertmanager
                          |
                          v
                       Discord
```

Prometheus provides the metrics backend for both Grafana dashboards and alert evaluation.

---

## Grafana

Grafana provides visualization for the platform's application and Kubernetes observability data.

Prometheus is configured as the metrics data source.

The dashboards provide visibility into areas such as:

- Application request traffic
- HTTP response status
- HTTP 5xx errors
- Request latency
- Kubernetes resource state
- Pod-level information
- Node-level metrics
- Application health

The Grafana architecture is:

```text
Application Metrics
        |
        v
    Prometheus
        |
        v
      Grafana
        |
        +-----------------------+
        |                       |
        v                       v
Application Dashboards   Kubernetes Dashboards
```

Grafana is used for visualization and operational investigation, while Prometheus and Alertmanager handle metric evaluation and alert delivery.

---

## Kubernetes-Level Observability

Kubernetes observability is provided through `kube-state-metrics` and `node-exporter`.

### kube-state-metrics

`kube-state-metrics` exposes metrics representing the state of Kubernetes objects.

These metrics provide visibility into resources such as:

- Deployments
- Pods
- Replica counts
- Available replicas
- Desired replicas
- Kubernetes workload state

These metrics are used by Prometheus for Kubernetes-level monitoring and alerting.

### node-exporter

`node-exporter` exposes node-level infrastructure metrics.

These metrics provide visibility into areas such as:

- CPU
- Memory
- Filesystem
- Node resources
- Host-level activity

The Kubernetes observability pipeline is:

```text
Kubernetes Cluster
       |
       +-------------------------+
       |                         |
       v                         v
kube-state-metrics          node-exporter
       |                         |
       +------------+------------+
                    |
                    v
                Prometheus
                    |
                    v
                 Grafana
```

---

## Prometheus Alerting

A PrometheusRule is used to detect application and infrastructure conditions that require attention.

The current application alerts are:

```text
DevOpsDemoAPIHigh5xxRate
DevOpsDemoAPIHighLatency
DevOpsDemoAPIDown
DevOpsDemoAPIHighCPU
DevOpsDemoAPIHighMemory
```

### High 5xx Error Rate

The `DevOpsDemoAPIHigh5xxRate` alert detects when more than 5% of application requests return HTTP 5xx responses during the last five minutes.

The expression is based on:

```text
http_requests_total
```

The alert condition is:

```text
5xx error rate > 5%
```

for:

```text
1 minute
```

### High Latency

The `DevOpsDemoAPIHighLatency` alert monitors p95 request latency.

The alert triggers when:

```text
p95 request latency > 1 second
```

for:

```text
2 minutes
```

The calculation uses:

```text
http_request_duration_seconds_bucket
```

### Application Availability

The `DevOpsDemoAPIDown` alert compares available Kubernetes replicas with the desired replica count.

The alert detects:

```text
available replicas < desired replicas
```

for:

```text
1 minute
```

### High CPU

The `DevOpsDemoAPIHighCPU` alert detects when a pod uses more than 80% of its requested CPU.

The condition must remain true for:

```text
5 minutes
```

### High Memory

The `DevOpsDemoAPIHighMemory` alert detects when a pod uses more than 80% of its configured memory limit.

The condition must remain true for:

```text
5 minutes
```

---

## Alertmanager

Alertmanager receives alerts generated by Prometheus and routes the application alerts to the configured Discord receiver.

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

The application alerts are routed using the service label:

```text
service = devops-demo-api
```

The current Alertmanager route groups alerts by:

```text
alertname
service
```

The configured grouping behaviour includes:

```text
groupWait: 5s
groupInterval: 10s
repeatInterval: 1h
```

---

## Discord Notifications

Alertmanager sends application alerts to Discord.

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

This allows Discord to receive both firing and resolved alert notifications.

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

The application error endpoint can be used to generate a controlled HTTP 500 response.

```powershell
curl.exe -s -o NUL -w "%{http_code}`n" http://localhost:8080/api/test-error
```

Expected result:

```text
500
```

Multiple requests can be generated to increase the 5xx error rate:

```powershell
1..20 | ForEach-Object {
    curl.exe -s -o NUL http://localhost:8080/api/test-error
}
```

### Verify Application Metrics

```powershell
curl.exe -L http://localhost:8080/metrics/ | Select-String "http_requests_total"
```

The output should contain a metric similar to:

```text
http_requests_total{method="GET",path="/api/test-error",status="500"}
```

### Verify the Prometheus Error Rate

The current 5xx error percentage can be queried directly from Prometheus:

```powershell
$params = @{
    query = 'sum(increase(http_requests_total{service="devops-demo-api",status=~"5.."}[5m])) / sum(increase(http_requests_total{service="devops-demo-api"}[5m])) * 100'
}

$result = Invoke-RestMethod `
    "http://localhost:9090/api/v1/query" `
    -Method Get `
    -Body $params

$result.data.result
```

The result can be used to verify that the error rate has exceeded the configured 5% threshold.

### Verify Alert State

Check the Prometheus alert:

```powershell
Invoke-RestMethod "http://localhost:9090/api/v1/alerts" |
    Select-Object -ExpandProperty data |
    Select-Object -ExpandProperty alerts |
    Where-Object {
        $_.labels.alertname -eq "DevOpsDemoAPIHigh5xxRate"
    } |
    Format-List
```

The alert transitions through:

```text
pending
    |
    v
firing
```

After the error condition clears and the alert's evaluation period passes, it transitions back to:

```text
inactive
```

Because Alertmanager is configured with:

```yaml
sendResolved: true
```

a resolved notification can also be delivered to Discord.

### Complete Alerting Flow

The complete validation path is:

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
    |
    v
Resolved Notification
```

This validates the complete application-to-notification observability pipeline.

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
- [x] Grafana
- [x] Kubernetes metrics
- [x] kube-state-metrics
- [x] node-exporter
- [ ] Centralized logging
- [x] HTTP 5xx monitoring
- [x] PrometheusRule
- [x] Alertmanager
- [x] Discord notifications
- [x] Alert recovery notifications
- [x] Latency monitoring
- [ ] SLOs
- [ ] Advanced SLO-based alerting
- [ ] Distributed tracing

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
10. Validate monitoring and alerting where applicable

This approach keeps each stage reproducible and provides a clear Git history of the platform's evolution.

---

## Current Milestone

The application delivery platform and initial observability foundation are complete.

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
Kubernetes Metrics
    +
Prometheus
    +
Grafana
    +
PrometheusRule
    +
Alertmanager
    +
Discord Notifications
    +
Alert Recovery
```

The platform has now progressed beyond basic application monitoring into a broader observability foundation covering:

```text
Application
    |
    +----------------------+
    |                      |
    v                      v
Application Metrics   Kubernetes Metrics
    |                      |
    +----------+-----------+
               |
               v
           Prometheus
               |
        +------+------+
        |             |
        v             v
     Grafana      Alerting
                     |
                     v
                Alertmanager
                     |
                     v
                  Discord
```

The next major milestone is **advanced observability and reliability engineering**, beginning with service-level objectives (SLOs), SLO-based alerting, centralized logging, and distributed tracing.

After the observability layer is further matured, the project will progress toward **progressive delivery**, including canary deployments, traffic management, automated promotion, and automated rollback.

---