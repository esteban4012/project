from pydantic import BaseModel,Field

class Articulos(BaseModel):

    id : int = Field(ge=1)
    price : int
    description : str = Field(min_length=4,max_length=20)
    id_category : int

    
