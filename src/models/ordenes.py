from pydantic import BaseModel

class Ordenes(BaseModel):

    id : int
    fecha : str
    id_cliente : int