# Production-Grade DevOps Platform

A hands-on DevOps project focused on building a reliable application delivery platform using containerization, automated testing, CI/CD, Kubernetes, security scanning, observability, reliability engineering, centralized logging, distributed tracing, and progressive delivery.

The platform is being built incrementally. Each stage is implemented, tested, validated, documented, and committed to Git.

---

## Current Status

The application delivery platform, containerization, CI/CD, security, Kubernetes deployment, application metrics, Prometheus monitoring, Grafana dashboards, Kubernetes-level observability, Prometheus alerting, Alertmanager routing, Discord notifications, SLO-based reliability monitoring, centralized logging, and distributed tracing have been implemented and validated.

The current Kubernetes deployment is healthy with:

```text
Deployment: devops-demo-api
Namespace: default
Replicas: 2
Ready: 2/2
Available: 2
```

The deployment uses an immutable commit-SHA container image and a `RollingUpdate` strategy with:

```text
maxUnavailable: 0
maxSurge: 1
```

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
- SLO recording rules
- Availability and error-rate SLIs
- Error-budget calculation
- Error-budget burn-rate alerting
- SLO violation alerting
- Loki centralized logging
- Grafana Alloy log collection
- Grafana Loki datasource
- Kubernetes pod log collection and visualization
- OpenTelemetry instrumentation
- OpenTelemetry OTLP trace export
- Tempo distributed tracing backend
- Grafana Tempo datasource
- Trace visualization in Grafana
- Trace IDs in structured application logs
- Span IDs in structured application logs
- Trace-aware Kubernetes application logging
- Trace validation through Kubernetes traffic
- Trace validation through Grafana Tempo
- Trace ID validation through Loki queries
- Tempo-to-Loki trace-to-logs configuration

### Implemented Observability

- Grafana dashboards
- Kubernetes-level observability
- kube-state-metrics
- node-exporter
- Application request metrics
- Application latency metrics
- HTTP 5xx error monitoring
- Application availability monitoring
- Application latency monitoring
- Application latency alerting
- CPU monitoring and alerting
- Memory monitoring and alerting
- PrometheusRule alerting
- Alertmanager routing
- Discord alert notifications
- Alert recovery notifications
- Service-level objectives (SLOs)
- Availability SLI
- Error-rate SLI
- Error-budget calculation
- Error-budget burn-rate monitoring
- SLO violation alerting
- Centralized Kubernetes pod logging
- Loki log storage
- Grafana Alloy log collection
- Grafana Explore log querying
- OpenTelemetry instrumentation
- Distributed tracing
- Tempo trace storage and querying
- Grafana trace visualization
- Trace ID and span ID application logging
- Trace-to-log correlation from Tempo to Loki

### Implemented Reliability Engineering

- Service-level objectives (SLOs)
- Availability SLI
- Error-rate SLI
- SLO recording rules
- Error-budget calculation
- Error-budget burn-rate alerting
- SLO violation alerting
- SLO validation through Prometheus queries
- Reliability monitoring based on application request metrics

### Implemented Centralized Logging

- Grafana Loki
- Grafana Alloy
- Kubernetes pod log discovery
- Kubernetes pod log relabeling
- Centralized log ingestion
- Grafana Loki datasource
- Grafana Explore log querying
- Structured JSON application logs
- Trace ID logging
- Span ID logging
- End-to-end log validation from Kubernetes pod to Grafana

The validated logging flow is:

```text
Kubernetes Pod
      |
      v
Grafana Alloy
      |
      v
Grafana Loki
      |
      v
Grafana Explore
```

### Implemented Distributed Tracing

- OpenTelemetry SDK and instrumentation
- FastAPI OpenTelemetry instrumentation
- OTLP HTTP trace export
- Tempo trace backend
- Tempo OTLP ingestion
- Grafana Tempo datasource
- Grafana trace exploration
- Trace ID generation and propagation
- Span ID generation and propagation
- Trace IDs included in structured application logs
- Trace IDs queryable in Loki
- Trace visualization validated through Grafana
- Tempo-to-Loki trace-to-logs configuration

The validated tracing flow is:

```text
FastAPI Application
        |
        v
OpenTelemetry Instrumentation
        |
        v
OTLP HTTP Export
        |
        v
Grafana Tempo
        |
        v
Grafana
```

The trace and log correlation flow is:

```text
FastAPI Request
      |
      +----------------------+
      |                      |
      v                      v
OpenTelemetry           Structured Log
      |                      |
      v                      v
    Tempo                  Alloy
      |                      |
      |                      v
      |                    Loki
      |                      |
      +----------+-----------+
                 |
                 v
              Grafana
```

The application logs contain the active OpenTelemetry trace context:

```text
trace_id
span_id
```

A validated trace can therefore be used to locate the corresponding application log entry in Loki.

### Planned

- Bidirectional Loki-to-Tempo trace navigation using Loki derived fields
- Canary deployments
- Traffic management
- Automated promotion
- Automated rollback
- Remote/cloud Kubernetes deployment
- Production-scale configuration management

---

## Architecture

### Current Architecture

The current platform implements the application delivery pipeline together with metrics, monitoring, alerting, reliability engineering, centralized logging, and distributed tracing.

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
               2 replicas      ClusterIP
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
          |         |         |
          v         v         v
      Metrics     Logs      Traces
          |         |         |
          v         v         v
     Prometheus   Alloy     OpenTelemetry
          |         |         |
          |         v         v
          |       Loki      Tempo
          |         |         |
          +---------+---------+
                    |
                    v
                 Grafana
                    |
             +------+------+
             |             |
             v             v
        PrometheusRule   Explore
             |
             v
        Alertmanager
             |
             v
           Discord


Kubernetes Pod Logs
        |
        v
 Grafana Alloy
        |
        v
   Grafana Loki
        |
        v
Grafana Explore


FastAPI Traces
        |
        v
OpenTelemetry
        |
        v
      Tempo
        |
        v
Grafana Trace View
```

The current architecture represents components that have been implemented and validated.

---

## Observability Architecture

The observability layer collects application-level metrics, Kubernetes-level metrics, Kubernetes pod logs, and distributed traces.

```text
                         Kubernetes Cluster
                                |
                +---------------+---------------+
                |               |               |
                v               v               v
        FastAPI Application  Kubernetes     Application
                |            Resources        Traces
                |               |               |
        +-------+-------+   +---+---+           v
        |               |   |       |     OpenTelemetry
        v               v   v       v           |
   /metrics/        Application   kube-state-   v
                    Logs          metrics     Tempo
        |               |           |           |
        |               v           v           |
        |          Grafana Alloy  node-exporter |
        |               |           |           |
        |               v           |           |
        |              Loki         |           |
        |               |           |           |
        +---------------+-----------+-----------+
                                |
                                v
                            Prometheus
                                |
                    +-----------+-----------+
                    |                       |
                    v                       v
                 Grafana              PrometheusRule
                    |                       |
                    |                       v
                    |                  Alertmanager
                    |                       |
                    |                       v
                    |                    Discord
                    |
             +------+------+
             |             |
             v             v
       Grafana Explore  Tempo Trace View
```

The platform therefore separates metrics, logs, and traces while providing a common visualization and investigation layer through Grafana.

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

These metrics provide the foundation for:

- Application dashboards
- HTTP 5xx monitoring
- Latency monitoring
- Availability measurement
- Error-rate measurement
- SLO calculations
- Error-budget calculations
- SLO-based alerting

The application also emits structured JSON logs containing:

```text
timestamp
level
service
message
trace_id
span_id
method
path
status
duration_seconds
```

OpenTelemetry instrumentation creates traces for incoming FastAPI requests.

The tracing data is exported using OTLP HTTP to Tempo.

### Distributed Tracing

Distributed tracing is implemented using OpenTelemetry instrumentation and Grafana Tempo.

The tracing pipeline is:

```text
FastAPI Application
        |
        v
OpenTelemetry Instrumentation
        |
        v
OTLP HTTP Exporter
        |
        v
Tempo
        |
        v
Grafana
```

The Kubernetes application is configured to export traces to:

```text
http://tempo.tempo.svc.cluster.local:4318/v1/traces
```

The application uses:

```text
OTEL_SERVICE_NAME=devops-demo-api
```

The tracing implementation is based on:

```text
opentelemetry-distro
opentelemetry-exporter-otlp
opentelemetry-instrumentation-fastapi
```

The application logs the active trace context so that a request can be correlated with its trace:

```text
trace_id
span_id
```

A validated application request produced a trace such as:

```text
trace_id: e94c23b30fc541e950b8bbfb7f19fa96
span_id: ab535222f32c5aaa
```

The trace was subsequently located in Grafana Tempo and the same trace ID was verified in Loki.

### Trace-to-Log Correlation

Grafana is configured with Tempo as a tracing datasource and Loki as the logging datasource.

Tempo is configured to use Loki for trace-to-log navigation through:

```yaml
jsonData:
  tracesToLogsV2:
    datasourceUid: loki
    spanStartTimeShift: "-2s"
    spanEndTimeShift: "2s"
    filterByTraceID: true
    filterBySpanID: false
```

The correlation flow is:

```text
Tempo Trace
     |
     v
Trace ID
     |
     v
Loki
     |
     v
Structured Application Log
```

The application log contains the same trace ID generated by OpenTelemetry.

A direct Loki query can therefore locate the log associated with a trace:

```text
{namespace="default"} |= "<trace-id>"
```

For example:

```text
trace_id="a00ae9f335695a5950430f79687a5a43"
```

was successfully matched to the corresponding `/api/test-slow` application log in Loki.

The current implementation validates Tempo-to-Loki correlation. Full bidirectional navigation from arbitrary Loki log entries back into Tempo using Loki derived fields remains a planned enhancement.

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

### Centralized Logging

Kubernetes pod logs are collected by Grafana Alloy and forwarded to Grafana Loki.

The logging pipeline is:

```text
Kubernetes Pods
      |
      v
Kubernetes Pod Discovery
      |
      v
Grafana Alloy
      |
      v
Grafana Loki
      |
      v
Grafana
      |
      v
Grafana Explore
```

Grafana Alloy uses Kubernetes service discovery to discover pod log targets and applies Kubernetes metadata such as:

```text
namespace
pod
container
app
```

The collected logs are forwarded to:

```text
http://loki.loki.svc.cluster.local:3100/loki/api/v1/push
```

This is an internal Kubernetes service endpoint and is not exposed externally.

A Loki query can be used in Grafana Explore to inspect pod logs:

```text
{pod="devops-demo-api-<pod-id>"}
```

The centralized logging pipeline was validated using a temporary Kubernetes test pod. A known test log entry was emitted, ingested by Alloy, stored by Loki, and successfully queried from Grafana Explore.

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
- SLO violations
- Error-budget burn rate

Alert recovery notifications are enabled through Alertmanager.

---

## Service-Level Objectives

The platform includes SLO-based reliability monitoring built on the existing Prometheus metrics.

The SLO pipeline is:

```text
Application Metrics
        |
        v
Prometheus
        |
        v
Availability / Error-Rate SLI
        |
        v
SLO Recording Rules
        |
        v
Error Budget
        |
        v
Burn-Rate Evaluation
        |
        v
SLO Alert
        |
        v
Alertmanager
        |
        v
Discord
```

### Availability SLI

Application availability is measured using successful request behaviour from the application metrics.

The availability SLI provides a measurable representation of the percentage of requests that successfully complete.

### Error-Rate SLI

The error-rate SLI measures the proportion of HTTP 5xx responses relative to total application requests.

The primary metric is:

```text
http_requests_total
```

The error-rate calculation can be represented conceptually as:

```text
5xx requests / total requests
```

### Error Budget

The error budget represents the amount of unreliability permitted by the configured SLO target.

Conceptually:

```text
Error Budget = 1 - SLO Target
```

The error budget can then be used to evaluate whether the service is consuming reliability capacity too quickly.

### Burn-Rate Monitoring

Burn-rate monitoring evaluates how quickly the application is consuming its available error budget.

The platform uses Prometheus recording rules and alerting rules to identify excessive error-budget consumption.

This provides an operational signal beyond simple threshold-based monitoring.

### SLO Validation

SLO behaviour is validated directly through Prometheus queries and controlled application traffic.

The reliability monitoring flow is:

```text
Controlled Application Traffic
          |
          v
    Application Metrics
          |
          v
       Prometheus
          |
          v
      SLO Rules
          |
          +----------------+
          |                |
          v                v
     Error Budget      Burn Rate
                           |
                           v
                      SLO Alert
```

---

## Target Architecture

The target architecture represents the planned final state of the platform, including distributed tracing, progressive delivery, centralized observability, SLO-driven operations, and automated rollback.

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
             Stable                Canary
                |                     |
                +----------+----------+
                           |
                           v
                  Traffic Management
                           |
                           v
                  Application Platform
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          Metrics        Logs         Traces
             |             |             |
             v             v             v
        Prometheus       Loki          Tempo
             |             |             |
             +-------------+-------------+
                           |
                           v
                        Grafana
                           |
                    +------+------+
                    |             |
                    v             v
                  SLOs        Alerting
                    |             |
                    +------+------+
                           |
                           v
                  Automated Promotion
                           |
                           v
                   Automated Rollback
```

Components are marked as implemented only after they have been deployed and validated.

Distributed tracing is now implemented and validated. Progressive delivery remains a future milestone.

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
- OpenTelemetry

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
- p95 latency monitoring
- CPU monitoring
- Memory monitoring
- Application availability monitoring
- Service-level objectives
- Error-budget monitoring
- Burn-rate monitoring
- SLO-based alerting
- Discord alert notifications
- Alert recovery notifications
- Grafana Loki
- Grafana Alloy
- Centralized Kubernetes pod logging
- Grafana Explore
- OpenTelemetry
- OTLP
- Grafana Tempo
- Distributed tracing
- Trace IDs
- Span IDs
- Trace visualization
- Trace-to-log correlation

### Planned Observability

- Bidirectional Loki-to-Tempo trace navigation
- Loki derived fields for trace navigation

### Planned Progressive Delivery

- Canary deployments
- Traffic management
- Canary validation
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
| `GET /api/test-slow` | Intentional slow response for latency and tracing validation |
| `GET /metrics/` | Prometheus application metrics |
| `GET /docs` | Swagger UI |

FastAPI automatically provides OpenAPI documentation through the Swagger interface.

The `/api/test-error` endpoint intentionally raises an exception and returns HTTP 500. It is used to validate application error metrics and the Prometheus alerting pipeline.

The `/api/test-slow` endpoint intentionally introduces a slow response and is used to validate latency monitoring and distributed tracing.

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

## Distributed Tracing

Distributed tracing is implemented using OpenTelemetry and Grafana Tempo.

### OpenTelemetry Instrumentation

The application uses:

```text
opentelemetry-distro
opentelemetry-exporter-otlp
opentelemetry-instrumentation-fastapi
```

FastAPI requests are instrumented using OpenTelemetry.

The application is configured with:

```text
OTEL_SERVICE_NAME=devops-demo-api
```

The Kubernetes deployment exports traces using OTLP HTTP to:

```text
http://tempo.tempo.svc.cluster.local:4318/v1/traces
```

### Tracing Architecture

```text
HTTP Request
     |
     v
FastAPI
     |
     v
OpenTelemetry Instrumentation
     |
     +-------------------+
     |                   |
     v                   v
Trace Context       Structured Log
     |                   |
     v                   v
OTLP HTTP             Alloy
     |                   |
     v                   v
   Tempo                Loki
     |                   |
     +---------+---------+
               |
               v
            Grafana
```

### Trace Context in Application Logs

The application structured logging formatter extracts the active OpenTelemetry span context.

Each completed HTTP request can therefore contain:

```text
trace_id
span_id
```

alongside:

```text
method
path
status
duration_seconds
```

Example:

```json
{
  "timestamp": "2026-09-02T20:31:36",
  "level": "INFO",
  "service": "devops-demo-api",
  "message": "HTTP request completed",
  "trace_id": "e94c23b30fc541e950b8bbfb7f19fa96",
  "span_id": "ab535222f32c5aaa",
  "method": "GET",
  "path": "/api/test-slow",
  "status": "200",
  "duration_seconds": 2.0015
}
```

### Tempo

Tempo runs in the `tempo` namespace.

The Tempo service exposes:

```text
3200  HTTP API
4317  OTLP gRPC
4318  OTLP HTTP
```

The Kubernetes service endpoint is:

```text
tempo.tempo.svc.cluster.local
```

The application sends OTLP HTTP traces to:

```text
http://tempo.tempo.svc.cluster.local:4318/v1/traces
```

### Grafana Tempo Datasource

Grafana is configured declaratively with the Tempo datasource through:

```text
k8s/monitoring-values.yaml
```

The configured datasource is:

```yaml
- name: Tempo
  type: tempo
  uid: tempo
  url: http://tempo.tempo.svc.cluster.local:3200
  access: proxy
  isDefault: false
  jsonData:
    tracesToLogsV2:
      datasourceUid: loki
      spanStartTimeShift: "-2s"
      spanEndTimeShift: "2s"
      filterByTraceID: true
      filterBySpanID: false
```

This allows Grafana to use Loki when investigating logs associated with Tempo traces.

### Trace Validation

A controlled request was generated against:

```text
/api/test-slow
```

The endpoint returned:

```text
{"message":"Intentional slow response for alert testing"}
```

The corresponding Kubernetes application log contained:

```text
trace_id: e94c23b30fc541e950b8bbfb7f19fa96
span_id: ab535222f32c5aaa
path: /api/test-slow
status: 200
duration_seconds: 2.0015
```

The trace was subsequently imported and visualized through Grafana Tempo.

### Loki Trace ID Validation

The same trace context is present in Loki.

A Loki query can locate the log using the trace ID:

```text
{namespace="default"} |= "<trace-id>"
```

A validated example returned the corresponding structured application log:

```text
trace_id: a00ae9f335695a5950430f79687a5a43
span_id: c62464ff12c612c6
path: /api/test-slow
status: 200
duration_seconds: 2.0009
```

This proves that the trace identifier generated by OpenTelemetry is available in both the tracing backend and centralized application logs.

### Trace-to-Log Correlation

The current correlation direction is:

```text
Tempo Trace
     |
     v
Trace ID
     |
     v
Loki Query
     |
     v
Structured Application Log
```

Grafana Tempo is configured to use Loki for trace-to-log navigation.

The current configuration uses:

```text
spanStartTimeShift: -2s
spanEndTimeShift: +2s
filterByTraceID: true
```

Full Loki derived-field configuration for direct log-to-trace navigation has not yet been added to the current platform configuration and therefore remains a planned enhancement.

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

The currently deployed image should always be verified directly from Kubernetes rather than hard-coded in this README.

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

The current deployment state has been validated as:

```text
READY        2/2
UP-TO-DATE   2
AVAILABLE    2
```

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
READY        2/2
UP-TO-DATE   2
AVAILABLE    2
```

### Verify the Deployed Image

```powershell
kubectl get deployment devops-demo-api -o jsonpath="{.spec.template.spec.containers[0].image}"
```

Expected format:

```text
ghcr.io/harshuk1702/devops-demo-api:<commit-sha>
```

### Verify Deployment Replica Metrics

Prometheus exposes Kubernetes deployment metrics through kube-state-metrics.

Query available replicas:

```powershell
(Invoke-RestMethod "http://localhost:9090/api/v1/query?query=kube_deployment_status_replicas_available{namespace%3D%22default%22%2Cdeployment%3D%22devops-demo-api%22}").data.result |
    Format-List
```

Query desired replicas:

```powershell
(Invoke-RestMethod "http://localhost:9090/api/v1/query?query=kube_deployment_spec_replicas{namespace%3D%22default%22%2Cdeployment%3D%22devops-demo-api%22}").data.result |
    Format-List
```

The validated healthy state is:

```text
Available replicas: 2
Desired replicas:   2
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

The local port is independent of the Kubernetes Service port.

The format is:

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
    Grafana          PrometheusRule
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

Loki is configured as the centralized logging data source.

Tempo is configured as the distributed tracing data source.

The dashboards and Explore views provide visibility into areas such as:

- Application request traffic
- HTTP response status
- HTTP 5xx errors
- Request latency
- Kubernetes resource state
- Pod-level information
- Node-level metrics
- Application health
- Distributed traces
- Trace IDs
- Application logs

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


Kubernetes Pod Logs
        |
        v
    Grafana Alloy
        |
        v
      Loki
        |
        v
      Grafana
        |
        v
   Grafana Explore


Application Traces
        |
        v
  OpenTelemetry
        |
        v
      Tempo
        |
        v
      Grafana
        |
        v
   Trace Explorer
```

Grafana is used for visualization and operational investigation, while Prometheus and Alertmanager handle metric evaluation and alert delivery.

Grafana Explore provides interactive querying of Loki logs.

Example LogQL query:

```text
{pod="devops-demo-api-<pod-id>"}
```

Tempo Explore provides interactive trace investigation.

Trace IDs can also be used to correlate trace data with structured application logs stored in Loki.

---

## Loki Centralized Logging

Grafana Loki provides centralized log storage for Kubernetes pod logs.

Grafana Alloy runs as a Kubernetes DaemonSet and collects logs from pods across the cluster.

The logging architecture is:

```text
Kubernetes Pods
      |
      v
Kubernetes Discovery
      |
      v
Grafana Alloy
      |
      v
Grafana Loki
      |
      v
Grafana Loki Datasource
      |
      v
Grafana Explore
```

### Grafana Alloy

The Alloy configuration is stored in:

```text
k8s/alloy-values.yaml
```

The configuration:

- Discovers Kubernetes pods
- Discovers pod log targets
- Relabels Kubernetes metadata
- Collects pod logs
- Forwards logs to Loki

Relevant labels include:

```text
namespace
pod
container
app
```

Alloy runs as a DaemonSet so that log collection is distributed across Kubernetes nodes.

### Loki

Loki runs in the `loki` namespace.

The Kubernetes service is:

```text
loki.loki.svc.cluster.local:3100
```

Alloy forwards logs to:

```text
http://loki.loki.svc.cluster.local:3100/loki/api/v1/push
```

### Grafana Loki Datasource

The Loki datasource is configured declaratively through:

```text
k8s/monitoring-values.yaml
```

The configured datasource is:

```yaml
grafana:
  additionalDataSources:
    - name: Loki
      type: loki
      uid: loki
      url: http://loki.loki.svc.cluster.local:3100
      access: proxy
      isDefault: false
```

This allows Grafana to query Loki through the Kubernetes service.

### Verify Logs in Grafana

Open Grafana and navigate to:

```text
Explore
```

Select:

```text
Loki
```

A basic query is:

```text
{pod="devops-demo-api-<pod-id>"}
```

Kubernetes metadata can also be used to narrow the query.

Example:

```text
{namespace="default"}
```

Trace IDs can be searched directly in Loki:

```text
{namespace="default"} |= "<trace-id>"
```

The centralized logging pipeline was validated end-to-end:

```text
Kubernetes Pod
      |
      v
Grafana Alloy
      |
      v
Grafana Loki
      |
      v
Grafana Explore
      |
      v
Visible Pod Logs
```

---

## Tempo Distributed Tracing

Grafana Tempo provides the distributed tracing backend for the application.

Tempo runs in the `tempo` namespace.

### Tempo Configuration

The Tempo Helm values are stored in:

```text
k8s/tempo-values.yaml
```

The current configuration is:

```yaml
tempo:
  reportingEnabled: false

persistence:
  enabled: false

traces:
  otlp:
    grpc:
      enabled: true
    http:
      enabled: true
```

### Tempo Service

The Tempo Kubernetes service exposes:

```text
3200  HTTP API
4317  OTLP gRPC
4318  OTLP HTTP
```

The internal service endpoint is:

```text
tempo.tempo.svc.cluster.local
```

### Trace Ingestion

The application exports OTLP HTTP traces to:

```text
http://tempo.tempo.svc.cluster.local:4318/v1/traces
```

The validated flow is:

```text
devops-demo-api
      |
      v
OpenTelemetry
      |
      v
OTLP HTTP
      |
      v
Tempo
```

### Grafana Tempo Datasource

Grafana uses the Tempo datasource:

```yaml
- name: Tempo
  type: tempo
  uid: tempo
  url: http://tempo.tempo.svc.cluster.local:3200
  access: proxy
  isDefault: false
  jsonData:
    tracesToLogsV2:
      datasourceUid: loki
      spanStartTimeShift: "-2s"
      spanEndTimeShift: "2s"
      filterByTraceID: true
      filterBySpanID: false
```

### Trace Visualization

A validated application trace was imported into Grafana Tempo and successfully visualized.

The trace included the application service:

```text
devops-demo-api
```

The `/api/test-slow` endpoint was used as a controlled trace-generation endpoint.

The request duration was approximately:

```text
2 seconds
```

The trace ID was also present in the corresponding Loki log entry.

### Trace and Log Correlation

The application generates trace IDs through OpenTelemetry.

The same trace IDs are written to structured application logs.

Therefore:

```text
HTTP Request
     |
     +-----------------------+
     |                       |
     v                       v
   Tempo                   Loki
     |                       |
     |                       |
     +----------+------------+
                |
                v
             Grafana
```

This establishes a common trace identifier across the tracing and logging systems.

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

For the `devops-demo-api` deployment, the following metrics have been verified through Prometheus:

```text
kube_deployment_status_replicas_available
kube_deployment_spec_replicas
```

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

The current application alerts include:

```text
DevOpsDemoAPIHigh5xxRate
DevOpsDemoAPIHighLatency
DevOpsDemoAPIDown
DevOpsDemoAPIHighCPU
DevOpsDemoAPIHighMemory
```

SLO-based rules additionally evaluate reliability and error-budget conditions.

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

This alert was validated by generating controlled HTTP 500 traffic through:

```text
/api/test-error
```

The alert transitioned into a firing state and generated a Discord notification.

After the error traffic stopped and the evaluation window cleared, the alert resolved and a recovery notification was received.

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

The `/api/test-slow` endpoint is also available for controlled latency and tracing validation.

### Application Availability

The `DevOpsDemoAPIDown` alert compares available Kubernetes replicas with the desired replica count.

The intended alert condition is:

```text
available replicas < desired replicas
```

for:

```text
1 minute
```

The underlying Kubernetes metrics are:

```text
kube_deployment_status_replicas_available
kube_deployment_spec_replicas
```

The deployment has been manually scaled to zero and restored to two replicas during validation.

The healthy state was successfully restored:

```text
Desired replicas:   2
Available replicas: 2
```

The Prometheus replica metrics were also verified.

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

### SLO-Based Alerting

The platform also evaluates SLO reliability conditions using Prometheus recording and alerting rules.

The SLO alerting flow is:

```text
Application Requests
        |
        v
http_requests_total
        |
        v
Availability / Error-Rate SLI
        |
        v
SLO Recording Rules
        |
        v
Error Budget
        |
        v
Burn Rate
        |
        v
SLO Violation Alert
        |
        v
Alertmanager
        |
        v
Discord
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

The current namespace selector is restricted to the `monitoring` namespace:

```yaml
alertmanagerConfigNamespaceSelector:
  matchNames:
    - monitoring
```

This matches the current project configuration and allows Alertmanager to discover the intended `AlertmanagerConfig` resource in the `monitoring` namespace.

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

The actual webhook value is intentionally not documented or committed to Git.

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
    alertmanagerConfigNamespaceSelector:
      matchNames:
        - monitoring
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

### Verify Application Availability Metrics

The availability alert can be investigated directly through Prometheus.

Query available replicas:

```powershell
(Invoke-RestMethod "http://localhost:9090/api/v1/query?query=kube_deployment_status_replicas_available{namespace%3D%22default%22%2Cdeployment%3D%22devops-demo-api%22}").data.result |
    Format-List
```

Query desired replicas:

```powershell
(Invoke-RestMethod "http://localhost:9090/api/v1/query?query=kube_deployment_spec_replicas{namespace%3D%22default%22%2Cdeployment%3D%22devops-demo-api%22}").data.result |
    Format-List
```

The healthy state should show:

```text
Available replicas: 2
Desired replicas: 2
```

To inspect whether the availability alert is currently active:

```powershell
Invoke-RestMethod "http://localhost:9090/api/v1/alerts" |
    Select-Object -ExpandProperty data |
    Select-Object -ExpandProperty alerts |
    Where-Object {
        $_.labels.alertname -eq "DevOpsDemoAPIDown"
    } |
    Format-List
```

An empty result means that the alert is not currently present in the Prometheus active-alert response.

### Verify SLO Rules

SLO recording rules can be inspected directly through the Prometheus expression interface or API.

The reliability validation should verify:

```text
Availability SLI
Error-Rate SLI
SLO Target
Error Budget
Burn Rate
SLO Alert State
```

The exact recording-rule names should be verified from the current `k8s/prometheusrule.yaml` rather than hard-coded into operational documentation.

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

## Logging Validation

The centralized logging pipeline can be validated independently from metric alerting.

The expected architecture is:

```text
Kubernetes Pod
      |
      v
Grafana Alloy
      |
      v
Grafana Loki
      |
      v
Grafana Explore
```

### Verify Loki

Check the Loki pod:

```powershell
kubectl get pods -n loki
```

Check the Loki service:

```powershell
kubectl get svc -n loki
```

### Verify Grafana Alloy

Check the Alloy DaemonSet:

```powershell
kubectl get daemonset -n logging
```

Check Alloy pods:

```powershell
kubectl get pods -n logging
```

### Verify Logs in Grafana

Open Grafana and select:

```text
Explore
```

Choose the Loki datasource and run:

```text
{pod="devops-demo-api-<pod-id>"}
```

The query should return log entries generated by the Kubernetes pod.

The end-to-end logging pipeline has been validated using a controlled test log:

```text
Kubernetes Pod
      |
      v
Alloy
      |
      v
Loki
      |
      v
Grafana Explore
      |
      v
Test Log Successfully Visible
```

### Verify Trace IDs in Loki

A trace ID can be searched directly in Loki:

```text
{namespace="default"} |= "<trace-id>"
```

This allows a trace discovered in Tempo to be correlated with its structured application log.

---

## Tracing Validation

Distributed tracing can be validated independently from metric alerting and centralized logging.

### Generate a Trace

The `/api/test-slow` endpoint can be used to generate a controlled trace:

```powershell
kubectl run curl-test --rm -i --restart=Never `
  --image=curlimages/curl `
  -- curl -s http://devops-demo-api.default.svc.cluster.local:8000/api/test-slow
```

Expected response:

```text
{"message":"Intentional slow response for alert testing"}
```

### Verify the Trace-Aware Application Log

```powershell
kubectl logs deployment/devops-demo-api --since=10m | Select-String "test-slow"
```

The application log should contain:

```text
trace_id
span_id
path
status
duration_seconds
```

Example:

```json
{
  "trace_id": "e94c23b30fc541e950b8bbfb7f19fa96",
  "span_id": "ab535222f32c5aaa",
  "path": "/api/test-slow",
  "status": "200",
  "duration_seconds": 2.0015
}
```

### Verify Loki Trace Correlation

A trace ID can be queried directly through Loki:

```powershell
kubectl run loki-query --rm -i --restart=Never `
  --image=curlimages/curl `
  -- curl -s "http://loki.loki.svc.cluster.local:3100/loki/api/v1/query_range?query=%7Bnamespace%3D%22default%22%7D%7C%3D%22<trace-id>%22&limit=20"
```

The query should return the corresponding structured application log.

### Verify Trace in Grafana

Open Grafana and navigate to:

```text
Explore
```

Select:

```text
Tempo
```

A validated trace can be opened using its trace ID.

The trace should display the instrumented FastAPI request and associated span information.

The validated tracing pipeline is:

```text
Kubernetes Request
       |
       v
FastAPI
       |
       v
OpenTelemetry
       |
       +----------------------+
       |                      |
       v                      v
     Tempo                Structured Log
       |                      |
       v                      v
    Grafana                 Alloy
                              |
                              v
                             Loki
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

The current deployment strategy is:

```text
RollingUpdate

maxUnavailable: 0

maxSurge: 1
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
│   ├── alloy-values.yaml
│   ├── deployment.yaml
│   ├── monitoring-values.yaml
│   ├── prometheusrule.yaml
│   ├── service.yaml
│   └── tempo-values.yaml
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

### Phase 5 — Observability and Reliability

- [x] Application metrics
- [x] Prometheus
- [x] Grafana
- [x] Kubernetes metrics
- [x] kube-state-metrics
- [x] node-exporter
- [x] HTTP 5xx monitoring
- [x] PrometheusRule
- [x] Alertmanager
- [x] Discord notifications
- [x] Alert recovery notifications
- [x] Latency monitoring
- [x] CPU monitoring
- [x] Memory monitoring
- [x] Application availability monitoring
- [x] Service-level objectives (SLOs)
- [x] Availability SLI
- [x] Error-rate SLI
- [x] Error-budget calculation
- [x] SLO-based alerting
- [x] Burn-rate monitoring
- [x] Advanced reliability monitoring
- [x] Centralized logging
- [x] Grafana Loki
- [x] Grafana Alloy
- [x] Grafana log visualization
- [x] OpenTelemetry
- [x] Distributed tracing
- [x] Grafana Tempo
- [x] Trace IDs in structured application logs
- [x] Span IDs in structured application logs
- [x] Grafana trace visualization
- [x] Tempo-to-Loki trace-to-log correlation
- [ ] Loki derived fields for direct log-to-trace navigation

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
11. Validate logging and tracing where applicable

This approach keeps each stage reproducible and provides a clear Git history of the platform's evolution.

---

## Current Milestone

The application delivery platform, Kubernetes deployment, monitoring, alerting, reliability engineering, centralized logging, and distributed tracing foundation are complete.

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

    +

Service-Level Objectives

    +

Availability / Error-Rate SLIs

    +

Error Budgets

    +

Burn-Rate Monitoring

    +

SLO-Based Alerting

    +

Grafana Loki

    +

Grafana Alloy

    +

Centralized Kubernetes Logging

    +

OpenTelemetry

    +

Distributed Tracing

    +

Grafana Tempo

    +

Trace IDs

    +

Span IDs

    +

Trace Visualization

    +

Trace-to-Log Correlation
```

The current Kubernetes deployment has also been validated after controlled scaling:

```text
Deployment: devops-demo-api

Initial state:

2/2 replicas available

Controlled test:

scaled to 0 replicas

Observed:

0/0 replicas

No application pods

Recovery:

scaled back to 2 replicas

Final state:

2/2 replicas available

2/2 pods running
```

Prometheus successfully exposes the Kubernetes deployment state through:

```text
kube_deployment_status_replicas_available

kube_deployment_spec_replicas
```

The final healthy state is:

```text
Available replicas: 2

Desired replicas: 2
```

The platform has progressed beyond basic application monitoring into a broader observability and reliability foundation covering:

```text
Application
    |
    +----------------------+----------------------+----------------------+
    |                      |                      |
    v                      v                      v
Application Metrics   Kubernetes Metrics    Kubernetes Logs
    |                      |                      |
    |                      |                      v
    |                      |                 Grafana Alloy
    |                      |                      |
    |                      |                      v
    |                      |                     Loki
    |                      |                      |
    |                      |                      |
    |                      |                      v
    |                      |               Grafana Explore
    |                      |
    +----------+-----------+
               |
               v
           Prometheus
               |
         +-----+-----+
         |           |
         v           v
      Grafana     Alerting
         |           |
         |           v
         |      Alertmanager
         |           |
         |           v
         |        Discord
         |
         +----------------------+
                                |
                                v
                       Application Traces
                                |
                                v
                         OpenTelemetry
                                |
                                v
                              Tempo
                                |
                                v
                         Grafana Traces
```

The project has now established a complete baseline for:

```text
Metrics

    +

Dashboards

    +

Alerting

    +

Notifications

    +

SLOs

    +

Error Budgets

    +

Reliability Monitoring

    +

Centralized Logging

    +

Distributed Tracing

    +

Trace-to-Log Correlation
```

The platform has therefore progressed from basic monitoring into a three-pillar observability model:

```text
              Observability
                    |
        +-----------+-----------+
        |           |           |
        v           v           v
     Metrics      Logs       Traces
        |           |           |
        v           v           v
   Prometheus     Loki       Tempo
        |           |           |
        +-----------+-----------+
                    |
                    v
                 Grafana
```

The next major milestone is **progressive delivery and canary deployment**.

---

## Next Task

The next implementation task starts with:

```text
PHASE 6 — PROGRESSIVE DELIVERY

        |

        v

STABLE DEPLOYMENT

        |

        v

CANARY DEPLOYMENT

        |

        v

TRAFFIC MANAGEMENT

        |

        v

CANARY VALIDATION

        |

        v

AUTOMATED PROMOTION

        |

        v

AUTOMATED ROLLBACK
```

The distributed tracing milestone has been completed.

The current observability foundation includes:

```text
Metrics
    |
    v
Prometheus
    |
    v
Grafana

Logs
    |
    v
Grafana Alloy
    |
    v
Loki
    |
    v
Grafana

Traces
    |
    v
OpenTelemetry
    |
    v
Tempo
    |
    v
Grafana
```

The tracing implementation provides:

- OpenTelemetry instrumentation for the FastAPI application
- OTLP trace export
- Tempo trace storage
- Grafana trace visualization
- Trace IDs in structured application logs
- Span IDs in structured application logs
- Trace ID queries in Loki
- Tempo-to-Loki trace-to-log correlation

The remaining observability enhancement is bidirectional navigation from Loki logs directly back to Tempo using Loki derived fields.

The next major implementation task is:

**Implement progressive delivery with a stable deployment and canary deployment strategy.**

The progressive delivery implementation should build on the existing Kubernetes, monitoring, alerting, SLO, logging, and tracing foundation rather than replacing the current platform.

The planned progressive delivery flow is:

```text
Existing Kubernetes Deployment
        |
        v
Stable Version
        |
        +----------------+
        |                |
        v                v
     Stable           Canary
        |                |
        +-------+--------+
                |
                v
       Traffic Management
                |
                v
        Canary Validation
                |
        +-------+-------+
        |               |
        v               v
      Healthy        Unhealthy
        |               |
        v               v
Automated Promotion  Automated Rollback
```

Canary validation should use the existing observability foundation:

```text
Canary
  |
  +------------------+------------------+
  |                  |                  |
  v                  v                  v
Metrics             Logs              Traces
  |                  |                  |
  v                  v                  v
Prometheus           Loki              Tempo
  |                  |                  |
  +------------------+------------------+
                     |
                     v
                  Grafana
                     |
                     v
              Canary Decision
```

This keeps the project progression logical:

```text
Application

    ↓

Containerization

    ↓

CI/CD

    ↓

Kubernetes

    ↓

Metrics

    ↓

Monitoring

    ↓

Alerting

    ↓

SLOs / Reliability Engineering

    ↓

Centralized Logging

    ↓

Distributed Tracing

    ↓

Trace-to-Log Correlation

    ↓

Advanced Observability

    ↓

Progressive Delivery

    ↓

Canary Deployment

    ↓

Traffic Management

    ↓

Automated Promotion

    ↓

Automated Rollback
```

The platform is intentionally implemented in validated stages so that each capability is operational before the next architectural layer is introduced.

---