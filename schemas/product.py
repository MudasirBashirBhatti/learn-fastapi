from pydantic import BaseModel,Field,field_validator
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

    @field_validator("name")
    @classmethod
    def name_must_be_upper(cls, v):
        if not v.isupper():
            raise ValueError("Name must be in uppercase")
        return v
    
    @field_validator("price")
    @classmethod
    def price_float_positive(cls,v):
        return (round(float(v),2) if v > 0 else ValueError("Price must be a positive number"))