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

@app.post('/products/add')
def add_product(product:Product):
    return {"message":f"Product {product.name} added successfully!"}

@app.put('/products/{product_id}')
def update_product(product_id:int,product:Product):
    for i,p in enumerate(products):
        if p.id == product_id:
            products[i]=product
            return {"message":f"Product {product_id} updated successfully!"}
    return {"message":f"Product {product_id} not found!"}

@app.get('/products/{product_id}')
def get_product(product_id:int):
    for p in products:
        if p.id == product_id:
            return p
    return {"message":f"Product {product_id} not found!"}

@app.delete('/products/{product_id}')
def delete_product(product_id:int):
    for i,p in enumerate(products):
        if p.id == product_id:
            products.pop(i)
            return {"message":f"Product {product_id} deleted successfully!"}
    return {"message":f"Product {product_id} not found!"}