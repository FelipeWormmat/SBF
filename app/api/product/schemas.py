from pydantic import BaseModel

class ProductMethodSchema(BaseModel):
    name: str
    enabled: bool

class ShowProductMethodSchema(ProductMethodSchema):
    id: int
    class Config:
        orm_mode = True