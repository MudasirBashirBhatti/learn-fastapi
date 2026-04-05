from fastapi import FastAPI
from models.product import Product
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


products = [
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop."),
    Product(id=2, name="Smartphone", price=499.99, description="A sleek smartphone with a great camera."),
]

@app.get("/products")
def get_all_products():
    return products


