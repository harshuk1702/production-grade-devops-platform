import json
import logging
import os
import sys

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
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


resource = Resource.create(
    {
        "service.name": os.getenv(
            "OTEL_SERVICE_NAME",
            "devops-demo-api",
        ),
    }
)

tracer_provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint=os.getenv(
        "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT",
        "http://localhost:4318/v1/traces",
    )
)

tracer_provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

trace.set_tracer_provider(tracer_provider)

FastAPIInstrumentor.instrument_app(app)


class TraceContextFormatter(logging.Formatter):
    def format(self, record):
        span = trace.get_current_span()
        span_context = span.get_span_context()

        trace_id = (
            format(span_context.trace_id, "032x")
            if span_context.is_valid
            else None
        )

        span_id = (
            format(span_context.span_id, "016x")
            if span_context.is_valid
            else None
        )

        log_record = {
            "timestamp": self.formatTime(
                record,
                "%Y-%m-%dT%H:%M:%S",
            ),
            "level": record.levelname,
            "service": os.getenv(
                "OTEL_SERVICE_NAME",
                "devops-demo-api",
            ),
            "message": record.getMessage(),
            "trace_id": trace_id,
            "span_id": span_id,
        }

        for field in (
            "method",
            "path",
            "status",
            "duration_seconds",
        ):
            if hasattr(record, field):
                log_record[field] = getattr(record, field)

        return json.dumps(log_record)


logger = logging.getLogger("devops-demo-api")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(TraceContextFormatter())

logger.handlers.clear()
logger.addHandler(handler)
logger.propagate = False


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

            logger.info(
                "HTTP request completed",
                extra={
                    "method": method,
                    "path": path,
                    "status": status,
                    "duration_seconds": round(duration, 4),
                },
            )

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