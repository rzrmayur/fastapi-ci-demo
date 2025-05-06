"""
main.py - FastAPI Tutorial Example

This file demonstrates the basics of FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+.
FastAPI is based on standard Python type hints, making code easy to write, read, and maintain.

Key FastAPI Features:
- Automatic interactive API docs (Swagger UI and ReDoc)
- Data validation and serialization using Pydantic
- Dependency injection system
- Asynchronous support

To run this app:
1. Install FastAPI and Uvicorn (ASGI server):
   pip install fastapi uvicorn
2. Start the server:
   uvicorn main:app --reload
3. Open your browser at:
   http://127.0.0.1:8000/docs  (Swagger UI)
   http://127.0.0.1:8000/redoc (ReDoc)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create the FastAPI app instance
app = FastAPI(
    title="FastAPI Tutorial API",
    description="A beginner-friendly FastAPI example with comments and explanations.",
    version="1.0.0"
)

# Pydantic model for request/response validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Root endpoint
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint returns a welcome message.
    """
    return {"message": "Welcome to FastAPI! Visit /docs for the interactive API documentation."}

# Path parameter example
@app.get("/items/{item_id}", tags=["Items"])
def read_item(item_id: int, q: str = None):
    """
    Get an item by its ID.
    - item_id: path parameter (int)
    - q: optional query parameter (str)
    """
    result = {"item_id": item_id}
    if q:
        result["q"] = q
    return result

# Request body example (POST)
@app.post("/items/", response_model=Item, tags=["Items"])
def create_item(item: Item):
    """
    Create an item with name, price, and is_offer fields.
    Request body is validated using the Item model.
    """
    return item

# Error handling example
@app.get("/error", tags=["Error Handling"])
def get_error():
    """
    Demonstrates raising an HTTPException for error handling.
    """
    raise HTTPException(status_code=418, detail="I'm a teapot (example error)")

# Health check endpoint
@app.get("/health", tags=["Utility"])
def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "ok"}

# Version endpoint
@app.get("/version", tags=["Utility"])
def version():
    """
    Returns the API version.
    """
    return {"version": app.version}
