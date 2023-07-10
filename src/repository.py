from db import session
from models.clientes import Cliente_entity, Cliente

def fech_clients():
    entities = session.query(Cliente_entity)
    models = []
    for entity in entities:
        models.append(to_client_model(entity))
    return models

def to_client_model(entity : Cliente_entity) -> Cliente:
    return Cliente(id=entity.id, 
                   name=entity.nombre,
                    last_name=entity.apellido1, 
                    second_surname=entity.apellido2, 
                    num_id=entity.numero_identificacion, 
                    address=entity.direccion, 
                    phone_number= entity.telefono, 
                    email=entity.correo_electronico)
