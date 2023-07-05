from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    name : str
    last_name : str
    second_surname : str
    num_id : int
    address : str
    phone_number : int
    email : str