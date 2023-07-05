from pydantic import BaseModel

class Articulos(BaseModel):

    id : int
    price : int
    description : str
    id_categoty : int

    
