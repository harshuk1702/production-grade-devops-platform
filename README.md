# Production-Grade DevOps Platform

A hands-on DevOps project focused on building a reliable application delivery platform using containerization, automated testing, CI/CD, Kubernetes, progressive delivery, and observability.

The platform is being built incrementally. Each stage is implemented, tested, measured, documented, and committed to Git.

## Current Status

The application and container foundation are complete.

- FastAPI application
- Automated API tests
- Docker containerization
- Docker health check
- Non-root container execution
- GitHub repository and version control

The CI/CD, Kubernetes, progressive delivery, and observability components are the next stages of implementation.

---

## Architecture

### Current Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
FastAPI Application
    |
    v
Docker Container
    |
    +---- Port 8000
    |
    +---- Health Check
    |
    +---- Non-root user
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
    +------------------+
    |                  |
    v                  v
Automated Tests    Docker Build
                       |
                       v
               Container Registry
                       |
                       v
                   Kubernetes
                       |
              +--------+--------+
              |                 |
              v                 v
           Stable            Canary
              |                 |
              +--------+--------+
                       |
                       v
               Traffic Management
                       |
                       v
                 Observability
                /      |       \
               /       |        \
          Metrics      Logs    Dashboards
               |
               v
        SLO / Health Checks
               |
               v
        Automated Rollback
```

The target architecture represents the planned final state of the platform. Components will be marked as implemented only after they have been deployed and validated.

---

## Technology Stack

### Application

- Python
- FastAPI
- Uvicorn
- Pytest

### Containerization

- Docker
- Python 3.13 slim
- Docker health checks
- Non-root container execution

### Planned Platform Components

- GitHub Actions
- Container Registry
- Kubernetes
- Helm
- Prometheus
- Grafana
- Progressive delivery / Canary deployments
- Automated rollback

---

## Application

The current FastAPI application exposes the following endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /` | Application root |
| `GET /health` | Application health check |
| `GET /api/products` | Product data |
| `GET /api/orders` | Order data |
| `GET /docs` | Swagger UI |

The API provides automatically generated OpenAPI documentation through the FastAPI Swagger interface.

---

## Testing

Automated API tests are implemented using Pytest.

Run the tests:

```powershell
cd application
.\.venv\Scripts\Activate.ps1
pytest
```

Current validation result:

```text
4 passed
```

The test suite currently validates the application's main API behaviour.

---

## Docker

The application is packaged as a Docker image.

### Build the Image

```powershell
docker build -t devops-demo-api:1.2.0 ./application
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

Current validation:

```text
Container status: healthy
```

The container also runs as a non-root user.

### Verify the Container User

```powershell
docker exec devops-demo-api whoami
```

Result:

```text
appuser
```

### Container Image

The current Docker image was measured locally at approximately:

```text
56.88 MB
```

The value is based on the locally built Docker image.

---

## Repository Structure

```text
production-grade-devops-platform/
|
+-- application/
|   |
|   +-- app/
|   |   +-- __init__.py
|   |   +-- main.py
|   |
|   +-- tests/
|   |   +-- __init__.py
|   |   +-- test_api.py
|   |
|   +-- Dockerfile
|   +-- pytest.ini
|   +-- requirements.txt
|
+-- docs/
|
+-- .gitignore
+-- README.md
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

### Phase 3 — CI/CD

- [ ] GitHub Actions
- [ ] Automated test pipeline
- [ ] Docker image build in CI
- [ ] Image security scanning
- [ ] Container registry

### Phase 4 — Kubernetes

- [ ] Kubernetes Deployment
- [ ] Kubernetes Service
- [ ] Readiness probe
- [ ] Liveness probe
- [ ] ConfigMap / Secrets
- [ ] Resource requests and limits

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
- [ ] Centralised logging
- [ ] Latency and error-rate monitoring
- [ ] SLOs

---

## Development Approach

The platform is developed in small, verifiable stages.

For each major change:

1. Implement the change
2. Run automated tests
3. Validate the deployment behaviour
4. Measure relevant results
5. Update the documentation
6. Commit the change to Git
7. Push the change to GitHub

The README and architecture documentation are updated as the implementation evolves.