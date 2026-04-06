from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    description: str | None

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str | None