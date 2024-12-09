from pydantic import BaseModel
class SandwichBase(BaseModel):
    name: str
    ingredients: str
    price: float
class SandwichCreate(SandwichBase):
    pass
class Sandwich(SandwichBase):
    id: int
    class Config:
        from_attributes = True
