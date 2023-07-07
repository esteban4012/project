from pydantic import BaseModel, Field

class Category(BaseModel):
    
    id : int = Field(ge=1)
    description : str = Field(min_length=4,max_length=20)