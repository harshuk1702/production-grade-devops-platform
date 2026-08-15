from fastapi import FastAPI

app = FastAPI(
    title="DevOps Demo API",
    description=(
        "Application workload for the "
        "Production-Grade Progressive Delivery & "
        "Observability Platform"
    ),
    version="1.0.0",
)


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