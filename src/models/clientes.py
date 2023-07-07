from pydantic import BaseModel, Field
from typing import Optional

class Cliente(BaseModel):
    id: int = Field(ge=1)
    name : str = Field(min_length=4,max_length=15)
    last_name : str = Field(min_length=4,max_length=15)
    second_surname : Optional[str] = Field(min_length=4,max_length=15)
    num_id : int
    address : str = Field(min_length=4,max_length=15)
    phone_number : int 
    email : str = Field(min_length=10,max_length=30)