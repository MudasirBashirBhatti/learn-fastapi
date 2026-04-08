from pydantic import BaseModel,Field
from typing import Annotated

class ProductSchema(BaseModel):
    id:Annotated[int,Field(title="Product ID",description="The unique identifier of the product")]
    name: str = Field(..., title="Product Name", description="The name of the product", examples=["Laptop"])
    price: float = Field(..., title="Product Price", description="The price of the product", examples=[999.99])
    description: str | None

class ProductCreate(BaseModel):
    name: str = Field(..., title="Product Name", description="The name of the product", examples=["Laptop"])
    price: float = Field(..., title="Product Price", description="The price of the product", examples=[999.99]) 
    description: str = Field(..., title="Product Description", description="A brief description of the product", examples=["A high-end gaming laptop with powerful graphics."])