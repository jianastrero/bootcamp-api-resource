from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB, Query

app = FastAPI()
db = TinyDB('./db.json')

peopleTable = db.table("people")


class Person(BaseModel):
    name: str
    age: int
    streetAddress: str
    barangay: str
    city: str
    province: str
    country: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate-people")
async def generate_people():
    peopleTable.truncate()

    people = [
        {'id': 1, 'name': 'John', 'age': 25, 'streetAddress': 'Halimuyak St.', 'barangay': 'Brgy. 1',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 2, 'name': 'Jane', 'age': 22, 'streetAddress': 'Bulaklak St.', 'barangay': 'Brgy. 2',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 3, 'name': 'Jenny', 'age': 23, 'streetAddress': 'Rosas St.', 'barangay': 'Brgy. 3',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 4, 'name': 'Jomar', 'age': 24, 'streetAddress': 'Sampaguita St.', 'barangay': 'Brgy. 4',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 5, 'name': 'Jasper', 'age': 26, 'streetAddress': 'Dama de Noche St.', 'barangay': 'Brgy. 5',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 6, 'name': 'Alice', 'age': 30, 'streetAddress': 'Mabini St.', 'barangay': 'Brgy. 6',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 7, 'name': 'Bob', 'age': 28, 'streetAddress': 'Rizal St.', 'barangay': 'Brgy. 7',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 8, 'name': 'Charlie', 'age': 32, 'streetAddress': 'Bonifacio St.', 'barangay': 'Brgy. 8',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 9, 'name': 'Diana', 'age': 27, 'streetAddress': 'Luna St.', 'barangay': 'Brgy. 9',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 10, 'name': 'Eve', 'age': 29, 'streetAddress': 'Quezon St.', 'barangay': 'Brgy. 10',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 11, 'name': 'Frank', 'age': 31, 'streetAddress': 'Aguinaldo St.', 'barangay': 'Brgy. 11',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 12, 'name': 'Grace', 'age': 33, 'streetAddress': 'Del Pilar St.', 'barangay': 'Brgy. 12',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 13, 'name': 'Hank', 'age': 34, 'streetAddress': 'Laurel St.', 'barangay': 'Brgy. 13',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 14, 'name': 'Ivy', 'age': 26, 'streetAddress': 'Osmeña St.', 'barangay': 'Brgy. 14',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 15, 'name': 'Jack', 'age': 35, 'streetAddress': 'Roxas St.', 'barangay': 'Brgy. 15',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 16, 'name': 'Karen', 'age': 36, 'streetAddress': 'Kalayaan St.', 'barangay': 'Brgy. 16',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 17, 'name': 'Leo', 'age': 37, 'streetAddress': 'Katipunan St.', 'barangay': 'Brgy. 17',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 18, 'name': 'Mona', 'age': 38, 'streetAddress': 'Magsaysay St.', 'barangay': 'Brgy. 18',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 19, 'name': 'Nina', 'age': 39, 'streetAddress': 'Ninoy St.', 'barangay': 'Brgy. 19',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 20, 'name': 'Oscar', 'age': 40, 'streetAddress': 'Ortigas St.', 'barangay': 'Brgy. 20',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 21, 'name': 'Paul', 'age': 41, 'streetAddress': 'Paterno St.', 'barangay': 'Brgy. 21',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 22, 'name': 'Quincy', 'age': 42, 'streetAddress': 'Quirino St.', 'barangay': 'Brgy. 22',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 23, 'name': 'Rachel', 'age': 43, 'streetAddress': 'Ramos St.', 'barangay': 'Brgy. 23',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'},
        {'id': 24, 'name': 'Steve', 'age': 44, 'streetAddress': 'Santos St.', 'barangay': 'Brgy. 24',
         'city': 'City of Manila', 'province': 'Metro Manila', 'country': 'Philippines'}
    ]

    for person in people:
        peopleTable.insert(person)

    return {"message": "People generated"}

@app.get("/people")
async def get_people():
    return peopleTable.all()

@app.get("/people/{person_id}")
async def get_person(person_id: int):
    Person = Query()
    person = peopleTable.get(Person.id == person_id)
    return person

@app.post("/people/add")
async def add_person(person: Person):
    person = {
        'id': peopleTable.all()[-1]['id'] + 1,
        'name': person.name,
        'age': person.age,
        'streetAddress': person.streetAddress,
        'barangay': person.barangay,
        'city': person.city,
        'province': person.province,
        'country': person.country
    }

    peopleTable.insert(person)
    return {"message": "Person added", "data": person}

@app.post("/people/update/{person_id}")
async def update_person(person_id: int, person: Person):
    Person = Query()
    peopleTable.update({
        'name': person.name,
        'age': person.age,
        'streetAddress': person.streetAddress,
        'barangay': person.barangay,
        'city': person.city,
        'province': person.province,
        'country': person.country
    }, Person.id == person_id)

    person = peopleTable.get(Person.id == person_id)
    return {"message": "Person updated", "data": person}

@app.post("/people/delete/{person_id}")
async def delete_person(person_id: int):
    Person = Query()
    person = peopleTable.get(Person.id == person_id)
    peopleTable.remove(Person.id == person_id)
    return {"message": "Person deleted", "data": person}
