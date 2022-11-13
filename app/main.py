from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Student(BaseModel):
    id: str
    name: str
    lastname: str

students = [] #lista para almacenar la información de los estudiantes

@app.get("/estudiantes") #para obtener estudiantes
def get_students():
    return students
@app.get("/estudiantes/{id}")
def get_student(id: str):
    for student in students:
        if student["id"] == id:
            return student
    return "No existe el estudiante"

@app.post("/estudiantes") #para registrar estudiantes
def save_student(student: Student):
    student.id = str(uuid4()) #para crear de forma aleatoria el id
    students.append(student.dict())#para añadir estudiantes en la lista
    return "Estudiante registrado"

@app.put("/estudiantes/{id}")
def update_student(updated_student: Student, id:str): #se recibe los datos del estudiante y el identificador .
    for student in students: #por cada estudiante en la lista de estudiante
        if student["id"] == id:
            student["name"] = updated_student.name
            student["lastname"] = updated_student.lastname
            return "Estudiante modificado"
    return "No existe el estudiante"

@app.delete("/estudiantes/{id}")
def delete_student(id: str):
    for student in students: #buscar estudiante en la lista estudiante
        if student["id"] == id:
            students.remove(student) #metodo remove para eliminar el estudiante de la lista
            return "Estudiante eliminado"
    return "No existe el estudiante"

