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
        product = Product(**data.dict())
        return self.repo.add(product)

    def update_product_or_404(self, product_id: int, data: ProductCreate):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        # Update fields dynamically
        for key, value in data.dict().items():
            setattr(product, key, value)
        return self.repo.update(product)

    def delete_product_or_404(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        self.repo.delete(product)
        return product