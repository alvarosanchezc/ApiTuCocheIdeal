from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Student(BaseModel):
    nombre: str
    apellido: str
    pais: str
    ciudad: str
    direccionResidencia: str
    numeroCedula: int
    celular: str
    contrasena: str

students = [] #lista para almacenar la información de los estudiantes

@app.get("/estudiantes") #para obtener estudiantes
def get_students():
    return students
@app.get("/estudiantes/{numeroCedula}")
def get_student(numeroCedula: int):
    for student in students:
        if student["numeroCedula"] == numeroCedula:
            return student
    return "No existe el cliente"

@app.post("/estudiantes") #para registrar estudiantes
def save_student(student: Student):
#    student.cedula = str(uuid4()) para crear de forma aleatoria el id
    students.append(student.dict())#para añadir estudiantes en la lista
    return "Cliente registrado"

@app.put("/estudiantes/{numeroCedula}")
def update_student(updated_student: Student, numeroCedula:int): #se recibe los datos del estudiante y el identificador .
    for student in students: #por cada estudiante en la lista de estudiante
        if student["numeroCedula"] == numeroCedula:
            student["nombre"] = updated_student.nombre
            student["apellido"] = updated_student.apellido
            student["pais"] =  updated_student.pais
            student["ciudad"] = updated_student.ciudad
            student["direccionResidencia"] = updated_student.direccionResidencia
            student["celular"] = updated_student.celular
            student["contrasena"] = updated_student.contrasena
            return "Cliente modificado"
    return "No existe el Cliente"

@app.delete("/estudiantes/{numeroCedula}")
def delete_student(id: str):
    for student in students: #buscar estudiante en la lista estudiante
        if student["numeroCedula"] == numeroCedula:
            students.remove(student) #metodo remove para eliminar el estudiante de la lista
            return "Estudiante eliminado"
    return "No existe el estudiante"
