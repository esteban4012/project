from fastapi import FastAPI
from models.clientes import Cliente
app = FastAPI()

# CRUD para la clase Clientes
# get me permite leer la tabla de los clientes
# en este caso utilizaremos como un diccionario como base de datos


data_clients = {
    "clients" : {
        1 : Cliente(id= 1, name= "esteban", last_name= "agudelo", second_surname= "hurtado", num_id= 12345678, address= "diagonal 65", phone_number= 3246785643, email= "esteban@gmail.com")
    }
}

@app.get("/clientes", tags=["clientes"])
async def read_clients():
    return data_clients
