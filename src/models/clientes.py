
from pydantic import BaseModel, Field
from typing import Optional
import db
from sqlalchemy import Column, Integer, String, Float, DECIMAL

class Cliente(BaseModel):
    id: int = Field(ge=1)
    name : str = Field(min_length=4,max_length=45)
    last_name : str 
    second_surname : Optional[str] 
    num_id : int
    address : str = Field(min_length=4,max_length=45)
    phone_number : int 
    email : str = Field(min_length=10,max_length=45)




class Cliente_entity(db.Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido1 = Column(String(50), nullable=False)
    apellido2 = Column(String(50),nullable=True)
    numero_identificacion = Column(DECIMAL(15,0),nullable=False)
    direccion = Column(String(50),nullable=False)
    telefono = Column(DECIMAL(15,0),nullable=False)
    correo_electronico = Column(String(50),nullable=False)

    def __init__(self, nombre, apellido1, apellido2, numero_identificacion, direccion, telefono, correo_electronico):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.numero_identificacion = numero_identificacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def __repr__(self):
        return f'clientes({self.nombre}, {self.apellido1}, {self.apellido2}, {self.numero_identificacion}, {self.direccion}, {self.telefono}, {self.correo_electronico})'

