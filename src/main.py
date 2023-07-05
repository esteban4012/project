from fastapi import FastAPI , HTTPException
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

@app.get("/clients", tags=["clients"])
async def read_clients():
    return data_clients

# post me permite crear clientes

@app.post("/clients",tags=["clients"])
async def create_clients(clients: Cliente):
    client = data_clients["clients"]
    client[clients.id] = clients
    return data_clients

# put me permite editar clientes

@app.put("/clients/{id}", tags=["clients"])
async def edit_clients(id : int , clients : Cliente):
    client = data_clients["clients"]
    if id not in client:
        return HTTPException(status_code=404,detail=f"client with {id=} does not exist")
    
    if len(clients.name.strip()) < 1:
        return HTTPException(status_code=404, detail=" name can not be empty")
    if len(clients.last_name.strip()) < 1:
        return HTTPException(status_code=404, detail=" last_name can not be empty")
    if len(clients.second_surname.strip()) < 1:
        return HTTPException(status_code=404, detail=" second_surname can not be empty")
    if clients.num_id < 1:
        return HTTPException(status_code=404, detail="num_id is mandatory")
    if len(clients.address.strip()) < 1:
        return HTTPException(status_code=404, detail=" address can not be empty")
    if clients.phone_number < 1:
        return HTTPException(status_code=404, detail="phone_number is mandatory")
    if len(clients.email.strip()) < 1:
        return HTTPException(status_code=404, detail=" email can not be empty")
    
    edit = client[id]
    edit.name = clients.name
    edit.last_name = clients.last_name
    edit.second_surname = clients.second_surname
    edit.num_id = clients.num_id
    edit.address = clients.address
    edit.phone_number = clients.phone_number
    edit.email  = clients.email
    return edit
    

# delete me permite eliminar clientes

@app.delete("/clients/{id}", tags=["clients"])
async def delete_client(id : int):
    client = data_clients["clients"]
    if id not in client:
        return HTTPException(status_code=404,detail=f"client with {id=} does not exist")
    client.pop(id)
    return data_clients