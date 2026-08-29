from fastapi import FastAPI
from prometheus_client import Counter, Histogram, make_asgi_app
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


app = FastAPI(
    title="DevOps Demo API",
    description=(
        "Application workload for the "
        "Production-Grade Progressive Delivery & "
        "Observability Platform"
    ),
    version="1.0.0",
)


REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "path", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "path"],
)


class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        import time

        start_time = time.perf_counter()

        path = request.url.path
        method = request.method

        try:
            response = await call_next(request)
            status = str(response.status_code)

            return response

        except Exception:
            status = "500"
            raise

        finally:
            duration = time.perf_counter() - start_time

            REQUEST_COUNT.labels(
                method=method,
                path=path,
                status=status,
            ).inc()

            REQUEST_LATENCY.labels(
                method=method,
                path=path,
            ).observe(duration)


app.add_middleware(MetricsMiddleware)

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.get("/")
def root():
    return {
        "message": "DevOps Demo API",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "devops-demo-api",
        "version": "1.0.0",
    }


@app.get("/api/products")
def get_products():
    return {
        "products": [
            {"id": 1, "name": "Laptop", "price": 1200},
            {"id": 2, "name": "Monitor", "price": 350},
            {"id": 3, "name": "Keyboard", "price": 100},
        ]
    }


@app.get("/api/orders")
def get_orders():
    return {
        "orders": [
            {"id": 1001, "status": "completed"},
            {"id": 1002, "status": "processing"},
            {"id": 1003, "status": "completed"},
        ]
    }


@app.get("/api/test-slow")
async def test_slow():
    import asyncio

    await asyncio.sleep(2)

    return {
        "message": "Intentional slow response for alert testing"
    }


@app.get("/api/test-error")
def test_error():
    raise RuntimeError("Intentional test error for alerting")