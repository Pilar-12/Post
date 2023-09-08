#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn Post:app --reload-
#{"id":3,"Name":"Alfredo", "LastName":"Garcia", "Age":30}
#Definimos nuestra entidad: User

class Passenger(BaseModel):
    id: int
    Name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int

#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
passengers_list= []


#***Get
@app.get("/passengersclass/")
async def passengersclass():
    return (passengers_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/passengersclass/


#***Post
@app.post("/passengersclass/")
async def passengersclass(passenger:Passenger):

    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 

    for index, saved_passenger in enumerate(passengers_list):
        if saved_passenger.id == passenger.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el pasajero ya existe"}
    else:
        passengers_list.append(passenger)
        return passenger

    #http://127.0.0.1:8000/passengersclass/