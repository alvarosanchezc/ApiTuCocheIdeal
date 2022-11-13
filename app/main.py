from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Cliente(BaseModel):
    nombre: str
    apellido: str
    pais: str
    ciudad: str
    direccionResidencia: str
    numeroCedula: int
    celular: str
    contrasena: str

clientes = [] #lista para almacenar la información de los clientes

@app.get("/clientes") #para obtener clientes
def get_clientes():
    return clientes
@app.get("/clientes/{numeroCedula}")
def get_cliente(numeroCedula: int):
    for cliente in clientes:
        if cliente["numeroCedula"] == numeroCedula:
            return cliente
    return "No existe el cliente"

@app.post("/clientes") #para registrar clientes
def save_cliente(cliente: Cliente):
#    student.cedula = str(uuid4()) para crear de forma aleatoria el id
    clientes.append(cliente.dict())#para añadir clientes en la lista
    return "Cliente registrado"

@app.put("/clientes/{numeroCedula}")
def update_cliente(updated_cliente: Cliente, numeroCedula:int): #se recibe los datos del cliente y el identificador .
    for cliente in clientes: #por cada estudiante en la lista de estudiante
        if cliente["numeroCedula"] == numeroCedula:
            cliente["nombre"] = updated_cliente.nombre
            cliente["apellido"] = updated_cliente.apellido
            cliente["pais"] =  updated_cliente.pais
            cliente["ciudad"] = updated_cliente.ciudad
            cliente["direccionResidencia"] = updated_cliente.direccionResidencia
            cliente["celular"] = updated_cliente.celular
            cliente["contrasena"] = updated_cliente.contrasena
            return "Cliente modificado"
    return "No existe el Cliente"

@app.delete("/clientes/{numeroCedula}")
def delete_cliente(id: str):
    for cliente in clientes: #buscar cliente en la lista clientes
        if cliente["numeroCedula"] == numeroCedula:
            clientes.remove(cliente) #metodo remove para eliminar el cliente de la lista
            return "Estudiante eliminado"
    return "No existe el estudiante"
