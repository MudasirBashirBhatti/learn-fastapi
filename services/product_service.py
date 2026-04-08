from repositories.product_repo import ProductRepository
from models import Product
from schemas.product import ProductCreate
from fastapi import HTTPException

class ProductService:
    def __init__(self, repo: ProductRepository):
        self.repo = repo

    def get_all_products(self):
        # Simply return all products
        return self.repo.get_all()

    def get_product_or_404(self, product_id: int):
        # Business logic: raise exception if not found
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def create_product(self, data: ProductCreate):
        product = Product(**data.model_dump())
        return self.repo.add(product)

    def update_product_or_404(self, product_id: int, data: ProductCreate):
        if not product_id:
            raise HTTPException(status_code=400, detail="Product ID is required for update")
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        # Update fields dynamically
        for key, value in data.model_dump().items():
            setattr(product, key, value)
        return self.repo.update(product)

    def delete_product_or_404(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        self.repo.delete(product)
        return product
    
    def use_params_request(self,name:str):
        return {"message": f"Hdello, {name}!"}