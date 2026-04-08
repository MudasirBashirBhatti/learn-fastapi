from fastapi import APIRouter, Depends,Path
from sqlalchemy.orm import Session
from database import get_db
from services.product_service import ProductService
from repositories.product_repo import ProductRepository
from schemas.product import ProductSchema, ProductCreate

router = APIRouter(prefix="/products", tags=["products"])

# Dependency to provide ProductService to routes
def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    repo = ProductRepository(db)
    return ProductService(repo)

@router.get("/", response_model=list[ProductSchema])
def get_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()

@router.get("/{product_id}", response_model=ProductSchema)
def get_product(product_id: int = Path(...,title="Get product by ID",description="Get product data by its ID",example="P001",min_length=3, max_length=8), service: ProductService = Depends(get_product_service)):
    return service.get_product_or_404(product_id)

@router.post("/", response_model=ProductSchema)
def add_product(data: ProductCreate, service: ProductService = Depends(get_product_service)):
    return service.create_product(data)

@router.put("/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, data: ProductCreate, service: ProductService = Depends(get_product_service)):
    return service.update_product_or_404(product_id, data)

@router.delete("/{product_id}")
def delete_product(product_id: int, service: ProductService = Depends(get_product_service)):
    return service.delete_product_or_404(product_id)