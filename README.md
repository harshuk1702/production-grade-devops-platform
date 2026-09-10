# Production-Grade DevOps Platform

A production-oriented DevOps platform demonstrating an end-to-end software delivery and reliability workflow across application development, CI/CD, container security, Kubernetes, progressive delivery, observability, SLOs, centralized logging, distributed tracing, and automated failure recovery.

The project was built incrementally. Each major capability was implemented, tested, validated, documented, and committed to Git, with the final platform deployed and validated on Amazon EKS before the AWS environment was intentionally decommissioned to avoid ongoing infrastructure costs.

---

## Project Goal

Build and validate a production-oriented DevOps platform that automates application delivery from source code through testing, containerization, security scanning, Kubernetes deployment, progressive delivery, observability, reliability monitoring, and automated failure recovery.

The end-to-end engineering flow is:

```text
Code
  ↓
CI
  ↓
Test
  ↓
Build
  ↓
Security Scan
  ↓
Registry
  ↓
Kubernetes
  ↓
Canary
  ↓
Automated Analysis
  ↓
Promotion / Rollback
  ↓
Metrics + Logs + Traces
  ↓
SLOs + Alerting
```

The project intentionally demonstrates not only deployment, but also the operational controls required to determine whether a deployment is healthy, promote it safely, and recover automatically when validation fails.

---

## Project Outcome

The project goal was achieved.

The implementation was deployed and validated on Amazon EKS, including:

- CI/CD through GitHub Actions
- Docker image build and validation
- Trivy container security scanning
- Kubernetes manifest validation
- Amazon ECR integration
- Immutable Git commit-SHA image deployment
- Argo Rollouts progressive canary delivery
- Stable/canary traffic management
- Prometheus-based automated canary analysis
- Automated promotion
- Automated rollback validation
- Application and Kubernetes monitoring
- SLO and error-budget monitoring
- Alertmanager routing
- Discord notifications
- Centralized logging with Grafana Loki and Alloy
- Distributed tracing with OpenTelemetry and Grafana Tempo
- Tempo-to-Loki trace-to-log correlation

The AWS environment was intentionally decommissioned after successful validation to avoid ongoing infrastructure costs. The implementation, Kubernetes configuration, CI/CD workflow, IAM configuration artifacts, validation procedures, and evidence remain preserved in the repository.

---

## Results at a Glance

The following results summarize the measurable outcomes obtained during implementation and remote validation.

| Engineering Area | Before / Baseline | Implemented Result |
|---|---|---|
| Progressive delivery | Conventional deployment model | **3-stage canary: 10% → 50% → 100%** |
| Canary validation | Manual judgement | **Automated Prometheus AnalysisTemplate with ≥95% success-rate threshold** |
| Failure recovery | Manual rollback path | **Automated rollback validated after failed canary analysis** |
| Kubernetes availability | No production-style remote validation | **2/2 replicas Ready and Available during final validation** |
| Application availability SLI | No quantified platform SLI | **1.0 / 100% availability observed during validation query** |
| HTTP error rate | No SLO-grade error measurement | **0% error rate observed during validation** |
| Prometheus rules | No platform-wide rule evaluation | **10 validated rules: 6 alerting + 4 recording rules** |
| Rule evaluation | No centralized evaluation cadence | **30-second evaluation interval** |
| Observability signals | Application-level visibility only | **3 pillars: metrics + logs + traces** |
| Log collection | Pod-local logs | **Kubernetes Pods → Alloy → Loki → Grafana** |
| Distributed tracing | No trace backend | **OpenTelemetry → Tempo → Grafana** |
| Trace/log investigation | Separate signals | **Validated Tempo trace ID ↔ Loki application log correlation** |
| Production deployment workflow | Local-only execution | **GitHub Actions → ECR → EKS → Argo Rollouts** |
| Immutable deployment identity | Mutable image versioning risk | **Git commit SHA used as deployment image tag** |
| Remote cluster | No cloud validation | **Amazon EKS Kubernetes 1.33 validated** |
| Worker capacity | No managed remote nodes | **2 × t3.small managed worker nodes during validation** |
| Node storage | No remote persistent worker footprint | **20 GiB gp3 per worker node during validation** |
| Final production workflow | No measured end-to-end timing | **4m31s validated workflow: 1m23s tests + 3m01s deployment** |
| AWS lifecycle | Running infrastructure would incur ongoing cost | **Validated, then intentionally decommissioned** |

### What Changed from Baseline to Result

The project was deliberately evolved from basic application delivery into a production-oriented operating model:

```text
Basic Application
      |
      v
Automated Tests
      |
      v
Containerized Application
      |
      v
Security Scanning
      |
      v
Kubernetes Deployment
      |
      v
Progressive Canary Delivery
      |
      v
Automated Health Analysis
      |
      +------------------+
      |                  |
     PASS               FAIL
      |                  |
      v                  v
Promotion             Rollback
      |                  |
      +---------+--------+
                |
                v
       Metrics + Logs + Traces
                |
                v
         SLOs + Alerting
```

This progression is important because the project outcome is not simply "an application running on Kubernetes"; it demonstrates controlled delivery, measurable reliability, operational visibility, and automated recovery.

---

## Current Status

The application was deployed and validated on Amazon EKS during Phase 7. The AWS environment was intentionally decommissioned after successful validation to avoid ongoing infrastructure costs. The deployment configuration and validation evidence remain preserved in the repository.

### Validated EKS State Before Decommissioning

```text
Rollout: devops-demo-api
Namespace: default
Replicas: 2
Ready: 2/2
Available: 2
```

The validated Rollout used an immutable Git commit-SHA image and an Argo Rollouts canary strategy with:

```text
maxUnavailable: 0
maxSurge: 1
```

### Completed Platform Capabilities

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
- Amazon ECR image publishing
- Argo Rollouts canary deployment
- Stable and canary Kubernetes Services
- NGINX ingress traffic routing
- 10% → 50% → 100% progressive delivery
- Prometheus-based canary analysis
- Automated promotion and rollback
- Readiness and liveness probes
- CPU and memory resource requests and limits
- Kubernetes security context
- Application Prometheus metrics
- Prometheus scraping
- PrometheusRule alerting
- Alertmanager routing
- Discord alert and recovery notifications
- SLO recording rules
- Availability and error-rate SLIs
- Error-budget calculation
- Burn-rate monitoring
- Loki centralized logging
- Grafana Alloy log collection
- OpenTelemetry instrumentation
- Tempo distributed tracing
- Trace IDs and span IDs in structured logs
- Tempo-to-Loki trace-to-log correlation

### Remaining Enhancements

The project milestone is complete. The remaining enhancements are limited to:

- Production configuration and secrets management
- Loki derived fields for direct log-to-trace navigation

These are future hardening/enhancement items rather than missing validation of the completed project milestone.

---

## Architecture

### Current Architecture

The validated platform implemented the application delivery pipeline together with progressive delivery, metrics, monitoring, alerting, reliability engineering, centralized logging, and distributed tracing.

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
                 Amazon ECR
                           |
                           v
                  Argo Rollouts
                           |
                    +------+------+
                    |             |
                    v             v
              Stable Service   Canary Service
                    |             |
                    +------+------+
                           |
                           v
                    NGINX Ingress
                           |
                           v
                    Progressive Traffic
                           |
                  +--------+--------+
                  |        |        |
                  v        v        v
                10%      50%      100%
               Canary    Canary   Stable
                  |        |        |
                  +--------+--------+
                           |
                           v
                      FastAPI API
                           |
                +----------+----------+
                |          |          |
                v          v          v
             Metrics     Logs      Traces
                |          |          |
                v          v          v
           Prometheus    Alloy   OpenTelemetry
                |          |          |
                |          v          v
                |        Loki      Tempo
                |          |          |
                +----------+----------+
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


Canary Analysis
      |
      v
Prometheus
      |
      v
AnalysisTemplate
      |
      v
Success Rate >= 0.95
      |
      +---- Pass ----> Continue Promotion
      |
      +---- Fail ----> Degraded / Previous Stable Revision


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
The architecture below represents components that were implemented and validated during the project.

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

The target architecture builds on the implemented platform capabilities, including distributed tracing, progressive delivery, centralized observability, SLO-driven operations, automated promotion, and automated rollback. The remote/cloud Kubernetes stage was subsequently implemented and validated on Amazon EKS.

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

Distributed tracing and progressive delivery are now implemented and validated, including controlled canary promotion and automated rollback validation.

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
- Amazon ECR
- Commit-SHA image tagging

### Kubernetes

- Kubernetes
- Argo Rollouts
- Stable and canary Services
- NGINX Ingress traffic routing
- Canary rollout strategy
- Progressive delivery: 10% → 50% → 100%
- Prometheus-based canary analysis
- Automated promotion
- Automated rollback validation
- Readiness probes
- Liveness probes
- Resource requests and limits
- SecurityContext
- ECR image access through AWS IAM

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

### Progressive Delivery

- Argo Rollouts canary deployments
- Stable and canary traffic management
- Prometheus canary validation
- Automated promotion
- Automated rollback validation

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
Login to Amazon ECR
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

Docker images are published to Amazon ECR.

The image repository follows:

```text
592685884777.dkr.ecr.ap-south-1.amazonaws.com/devops-demo-api
```

The CI pipeline publishes:

```text
:ci
:<commit-sha>
```

The Kubernetes Rollout uses an immutable commit-SHA image reference.

Example:

```text
592685884777.dkr.ecr.ap-south-1.amazonaws.com/devops-demo-api:<commit-sha>
```

The currently deployed image should always be verified directly from Kubernetes rather than hard-coded in this README.

This ensures that Kubernetes deployments reference a specific immutable image version rather than a mutable tag such as `latest`.

---

## Kubernetes

The application is deployed to Kubernetes using an Argo Rollout with dedicated stable and canary Services.

### Argo Rollouts

The application is managed by an Argo Rollouts `Rollout` resource with:

```text
2 replicas
```

The rollout uses a canary strategy with progressive traffic weights:

```text
10% Canary
    |
    v
Prometheus Analysis
    |
    v
50% Canary
    |
    v
Prometheus Analysis
    |
    v
100% Promotion
```

The stable and canary Services are:

```text
devops-demo-api-stable
devops-demo-api-canary
```

Traffic routing is provided through the NGINX ingress:

```text
Client
  |
  v
NGINX Ingress
  |
  +------------------+
  |                  |
  v                  v
Stable Service    Canary Service
  |                  |
  +--------+---------+
           |
           v
     FastAPI Pods
```

The canary is validated using the Prometheus AnalysisTemplate:

```text
devops-demo-api-success-rate
```

The production success condition is:

```text
result[0] >= 0.95
```

A failed canary analysis causes the Rollout to enter a degraded state while the previous stable revision remains available.

The current Rollout state has been validated as:

```text
Healthy
Replicas: 2
Available: 2
Stable revision: current healthy revision
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
592685884777.dkr.ecr.ap-south-1.amazonaws.com/devops-demo-api:<commit-sha>
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

## Progressive Delivery

The application uses **Argo Rollouts** to implement progressive canary delivery instead of a traditional Kubernetes Deployment rolling update.

The rollout strategy is:

```text
Current Stable Revision
          |
          v
      Canary 10%
          |
          v
 Prometheus Analysis
          |
          v
       Pause 30s
          |
          v
      Canary 50%
          |
          v
 Prometheus Analysis
          |
          v
       Pause 30s
          |
          v
     Canary 100%
          |
          v
   New Revision Stable
```

Traffic is controlled through dedicated Kubernetes Services and NGINX Ingress routing:

```text
                    NGINX Ingress
                         |
              +----------+----------+
              |                     |
              v                     v
       Stable Service       Canary Service
              |                     |
              v                     v
       Stable Pods            Canary Pods
```

The Rollout automatically evaluates the canary using the Prometheus AnalysisTemplate:

```text
HTTP Success Rate >= 0.95
```

The analysis runs at the 10% and 50% stages. If the success-rate analysis fails, the Rollout enters a degraded state and the previous stable revision remains available.

A successful rollout automatically promotes the canary to 100% and makes the new revision stable.

The Rollout can be inspected using:

```powershell
kubectl get rollout devops-demo-api
kubectl argo rollouts get rollout devops-demo-api
```

A live rollout can be watched using:

```powershell
kubectl argo rollouts get rollout devops-demo-api --watch
```

AnalysisRuns can be inspected using:

```powershell
kubectl get analysisruns
```

The Prometheus AnalysisTemplate is managed as Kubernetes configuration in:

```text
k8s/analysis-template.yaml
```

The production success-rate threshold is:

```text
>= 0.95
```

This provides controlled progressive delivery with automated validation, promotion, and rollback behavior.

## Repository Structure

The repository is organized around the application, CI/CD workflow, Kubernetes configuration, observability configuration, and AWS deployment configuration.

```text
production-grade-devops-platform/
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
├── k8s/
│   ├── alertmanagerconfig.yaml
│   ├── alloy-values.yaml
│   ├── analysis-template.yaml
│   ├── github-actions-rbac.yaml
│   ├── grafana-values.yaml
│   ├── ingress.yaml
│   ├── loki-values.yaml
│   ├── monitoring-values.yaml
│   ├── prometheus-standalone-rules.yaml
│   ├── prometheus-standalone-values.yaml
│   ├── prometheusrule.yaml
│   ├── rollout.yaml
│   ├── service-canary.yaml
│   ├── service-stable.yaml
│   ├── service.yaml
│   └── tempo-values.yaml
│
├── scripts/
│
├── .gitignore
├── eksctl-cluster.yaml
├── github-actions-ecr-policy.json
├── github-actions-eks-policy.json
├── github-actions-trust-policy.json
└── README.md
```

The repository preserves the deployment and validation configuration even though the live AWS environment was intentionally decommissioned after successful validation.

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
- [x] Amazon ECR
- [x] Commit-SHA image tagging

### Phase 4 — Kubernetes

- [x] Argo Rollouts
- [x] Stable and canary Services
- [x] NGINX ingress traffic routing
- [x] Readiness probe
- [x] Liveness probe
- [x] Resource requests and limits
- [x] Kubernetes security context
- [x] Canary rollout strategy
- [ ] Production configuration management

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

## Phase 6 — Progressive Delivery

- [x] Stable deployment
- [x] Canary deployment
- [x] Traffic management
- [x] Canary validation
- [x] Automated promotion
- [x] Automated rollback

Validated flows:

```text
Stable → Canary → Analysis → Promotion

Stable → Canary → Failed Analysis → Rollback
```

## Phase 7 — Cloud / Remote Kubernetes

- [x] Remote Kubernetes cluster with Amazon EKS
- [x] Amazon ECR container registry integration
- [x] Remote deployment through GitHub Actions
- [ ] Production configuration management
- [x] External traffic management
- [x] Production observability
- [x] Remote health, rollout, logging, tracing, and monitoring validation

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

---

## Validation Evidence

The platform was validated locally and on Amazon EKS before the AWS environment was intentionally decommissioned.

Validation covered:

- CI pipeline success
- Docker image build
- Trivy security scanning
- Kubernetes manifest validation
- EKS cluster deployment
- Managed worker node validation
- External application access
- Immutable image verification
- Argo Rollouts canary progression
- Prometheus canary analysis
- Automated promotion
- Failed canary rollback
- Prometheus metrics and recording rules
- Prometheus alerting
- Alertmanager routing
- Discord notifications
- Alert recovery notifications
- SLO and error-budget evaluation
- Loki centralized logging
- Grafana Alloy collection
- Tempo distributed tracing
- Tempo-to-Loki trace correlation

### CI/CD Validation Result

The final validated production workflow completed in approximately:

```text
Total workflow:       4m 31s
Test stage:           1m 23s
Deployment stage:     3m 01s
```

The workflow validated the expected sequence:

```text
GitHub Actions
      |
      v
Tests
      |
      v
Docker Build
      |
      v
Trivy Scan
      |
      v
Kubernetes Manifest Validation
      |
      v
Amazon ECR
      |
      v
Amazon EKS
      |
      v
Argo Rollouts
      |
      v
Health / Rollout Verification
```

The deployment verification checked the expected image, rollout generation, and Healthy rollout state before the production deployment workflow succeeded.

### Kubernetes Validation Result

The validated EKS environment used:

```text
Kubernetes version: 1.33
Managed worker nodes: 2
Instance type: t3.small
Node volume: 20 GiB gp3
Application replicas: 2
```

The final application state before AWS decommissioning was:

```text
Desired replicas:    2
Available replicas:  2
Ready replicas:      2
```

A controlled recovery test also demonstrated that the application could be scaled from:

```text
2 replicas
    ↓
0 replicas
    ↓
0 running application pods
    ↓
scale back to 2
    ↓
2/2 replicas available
```

This validated the Kubernetes recovery path and confirmed that the application returned to the expected healthy state.

### Progressive Delivery Results

The production Rollout used:

```text
10% Canary
   ↓
Prometheus Analysis
   ↓
50% Canary
   ↓
Prometheus Analysis
   ↓
100% Promotion
```

The production success-rate analysis threshold was:

```text
HTTP success rate >= 0.95
```

The successful flow was validated as:

```text
Stable
  ↓
Canary 10%
  ↓
Analysis PASS
  ↓
Canary 50%
  ↓
Analysis PASS
  ↓
Canary 100%
  ↓
New revision becomes Stable
```

A separate failure-path validation intentionally caused the canary analysis to fail.

The observed recovery flow was:

```text
Stable
  ↓
Canary
  ↓
Analysis FAIL
  ↓
Rollout Degraded
  ↓
Failed canary scaled down
  ↓
Previous Stable Revision retained
```

This demonstrated that progressive delivery was not only configured but exercised through both the success and failure paths.

### Prometheus Validation Results

The production Prometheus rules were validated using `promtool`.

Measured rule inventory:

```text
Total rules:          10
Alerting rules:        6
Recording rules:       4
Evaluation interval:  30s
```

The validated Prometheus stack exposed application and Kubernetes signals for:

- Request rate
- HTTP status codes
- HTTP 5xx rate
- Request latency
- Application availability
- CPU utilization
- Memory utilization
- Replica state
- SLOs
- Error budgets
- Burn-rate conditions

The validation query results included:

```text
Availability SLI: 1.0
Error rate:        0
```

These values represent the observed healthy validation period, not a permanent production guarantee.

### Alerting Validation

The alerting chain was validated end-to-end:

```text
Application
    ↓
Prometheus Metrics
    ↓
Prometheus Rule
    ↓
Alertmanager
    ↓
Discord
```

Validated alerting capabilities included:

- High HTTP 5xx rate
- High latency
- Application availability failure
- High CPU
- High memory
- SLO-based violations
- Error-budget burn-rate conditions
- Recovery notifications

The `DevOpsDemoAPIHigh5xxRate` alert was specifically validated as part of the alerting workflow.

### Logging Validation

The centralized logging path was validated as:

```text
Kubernetes Pod
      ↓
Grafana Alloy
      ↓
Grafana Loki
      ↓
Grafana Explore
```

Structured application logs included:

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

This made application requests searchable through Loki while preserving the distributed trace context required for cross-signal investigation.

### Distributed Tracing Validation

The tracing path was validated as:

```text
FastAPI
   ↓
OpenTelemetry
   ↓
OTLP HTTP
   ↓
Grafana Tempo
   ↓
Grafana Trace View
```

The application generated and propagated:

```text
trace_id
span_id
```

A validated Tempo trace ID was:

```text
71a58631de41b0fcb159ab9cc399e3f7
```

The corresponding Loki application log contained the same trace context, demonstrating cross-signal correlation.

### Tempo-to-Loki Correlation Result

The validated investigation workflow was:

```text
Tempo Trace
    ↓
trace_id
    ↓
Loki Query
    ↓
Matching Application Log
```

This allowed the same request to be followed across:

```text
Request
  ↓
Trace
  ↓
Span
  ↓
Structured Log
```

The implementation therefore moved beyond isolated metrics, logs, and traces into practical observability correlation.

---

## Engineering Results: Before → After

The project can be summarized as a sequence of engineering improvements rather than a list of technologies.

### Delivery

**Before**

```text
Application code
    ↓
Manual validation
    ↓
Manual deployment
```

**After**

```text
Git commit
    ↓
GitHub Actions
    ↓
Automated tests
    ↓
Docker build
    ↓
Trivy scan
    ↓
Kubernetes validation
    ↓
Amazon ECR
    ↓
Amazon EKS
```

### Deployment Safety

**Before**

```text
New version
    ↓
Full rollout
```

**After**

```text
New version
    ↓
10% canary
    ↓
Automated analysis
    ↓
50% canary
    ↓
Automated analysis
    ↓
100% promotion
```

### Failure Recovery

**Before**

```text
Deployment failure
    ↓
Operator investigation
    ↓
Manual rollback
```

**After**

```text
Deployment failure
    ↓
Prometheus analysis failure
    ↓
Rollout Degraded
    ↓
Canary removed
    ↓
Previous stable revision retained
```

### Observability

**Before**

```text
Application logs + basic monitoring
```

**After**

```text
Metrics  → Prometheus → Grafana
Logs     → Alloy → Loki → Grafana
Traces   → OpenTelemetry → Tempo → Grafana
                         ↘
                          Loki correlation
```

### Reliability

**Before**

```text
"Application appears healthy"
```

**After**

```text
Availability SLI
      +
Error-rate SLI
      +
Error budget
      +
Burn-rate monitoring
      +
SLO alerting
```

### Operational Result

The final validated platform therefore provides:

```text
Automated Delivery
        +
Container Security
        +
Kubernetes Operations
        +
Progressive Delivery
        +
Automated Failure Recovery
        +
Metrics
        +
Logs
        +
Traces
        +
SLOs
        +
Alerting
```

This is the core production-oriented outcome of the project.

---

## AWS Deployment Lifecycle

The AWS environment was intentionally used as a validation environment rather than left running indefinitely.

### Deployment

```text
GitHub Actions
      ↓
Amazon ECR
      ↓
Amazon EKS
      ↓
Argo Rollouts
      ↓
Prometheus Analysis
      ↓
Promotion / Rollback
      ↓
External Validation
```

### Decommissioning

After successful validation, the AWS resources were intentionally removed to prevent ongoing infrastructure charges.

The decommissioning included:

- Amazon EKS cluster
- Managed worker nodes
- EBS worker volumes
- Load balancer resources
- Public IPv4 allocations
- ECR application repository
- Project-specific GitHub Actions IAM role
- IAM policies associated with the deployment role
- GitHub Actions OIDC provider used by the project

The final repository retains the configuration and evidence required to reproduce the deployment.

### Important Project State

The README intentionally does **not** claim that the application is currently running on AWS.

The accurate project statement is:

> **Deployed and validated on AWS EKS.**

The live environment was subsequently decommissioned for cost control.

---

## Portfolio / Recruiter Summary

This project demonstrates practical experience across:

- Python / FastAPI
- Docker
- GitHub Actions
- Trivy
- Kubernetes
- Amazon EKS
- Amazon ECR
- Argo Rollouts
- NGINX Ingress
- Prometheus
- Grafana
- Alertmanager
- Discord alerting
- SLOs and error budgets
- Grafana Loki
- Grafana Alloy
- OpenTelemetry
- Grafana Tempo
- Distributed tracing
- Trace-to-log correlation
- Kubernetes reliability and recovery
- Progressive delivery
- Automated rollback

The strongest evidence is not the technology list alone; it is the validated operational behaviour:

```text
10% → 50% → 100% canary delivery
          +
≥95% automated success-rate analysis
          +
Successful automated promotion
          +
Validated failed-analysis rollback
          +
2/2 healthy replicas
          +
0 observed HTTP error rate
          +
1.0 availability SLI
          +
10 Prometheus rules
          +
3 observability pillars
          +
4m31s validated production workflow
```

---

## Remaining Enhancements

The completed project milestone does not require another major platform phase.

The remaining enhancements are:

### 1. Production Configuration Management

Introduce a production-grade configuration and secrets-management strategy, such as:

- Kubernetes Secrets with stronger lifecycle controls
- External secret management
- Environment-specific configuration
- Secret rotation
- Configuration validation
- Separation of development, staging, and production configuration

### 2. Loki Derived Fields

Add Loki derived fields so a trace ID in a log entry can be used directly to navigate into Tempo.

Current validated capability:

```text
Tempo
  ↓
trace_id
  ↓
Loki
  ↓
Matching log
```

Future enhancement:

```text
Loki Log Entry
      ↓
Derived trace_id
      ↓
Direct Tempo Navigation
```

These enhancements improve production ergonomics and configuration hygiene but do not change the fact that the main platform milestone was successfully implemented and validated.

---

## Development Approach

The platform was developed in small, verifiable stages.

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

This approach kept each stage reproducible and created a clear Git history of the platform's evolution.

The final implementation was deliberately validated before the AWS environment was decommissioned. This separates **technical validation** from **continuous infrastructure runtime**, allowing the repository to preserve the demonstrated engineering work without incurring unnecessary ongoing AWS costs.

---

## Final Project Status

```text
Phase 1  — Application Foundation          COMPLETE
Phase 2  — Containerization                COMPLETE
Phase 3  — CI/CD                           COMPLETE
Phase 4  — Kubernetes                      COMPLETE
Phase 5  — Observability & Reliability     COMPLETE
Phase 6  — Progressive Delivery            COMPLETE
Phase 7  — AWS / Remote Kubernetes         COMPLETE
```

### Final Outcome

```text
Production-Grade DevOps Platform
             |
             +-- Automated CI/CD
             +-- Container Security
             +-- Kubernetes
             +-- Amazon EKS
             +-- Amazon ECR
             +-- Progressive Canary Delivery
             +-- Automated Analysis
             +-- Automated Rollback
             +-- Prometheus
             +-- Grafana
             +-- Alertmanager
             +-- SLOs / Error Budgets
             +-- Loki / Alloy
             +-- OpenTelemetry / Tempo
             +-- Trace-to-Log Correlation
             +-- Validated Recovery
```

The project demonstrates an end-to-end production-oriented DevOps workflow from source code to deployment, controlled release, observability, reliability measurement, and automated recovery.

The AWS environment was intentionally decommissioned after validation. The repository remains the durable source of truth for the implementation, deployment configuration, CI/CD workflow, and validation evidence.
