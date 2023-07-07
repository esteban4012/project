from pydantic import BaseModel,Field

class Ordenes(BaseModel):

    id : int = Field(ge=1)
    fecha : str = Field(default="dd/mm/year", min_length=5,max_length=20)
    id_cliente : int = Field(ge=1)