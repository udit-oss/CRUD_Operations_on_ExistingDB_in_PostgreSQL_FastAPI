from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from database import SessionLocal, engine
import models

app = FastAPI()

# Dependency to get DB session
db = SessionLocal()

class PersonBase(BaseModel):
    customer_id: str
    customer_name: str
    segment: str
    age: int
    country: str
    city: str
    state: str
    postal_code: int
    region: str

class PersonOut(PersonBase):
    # customer_id: str

    class Config:
        orm_mode = True

# API endpoint to fetch all persons
# Route to get every person
@app.get('/', response_model=list[PersonOut], status_code=status.HTTP_200_OK)
async def getAll_Persons():
    getAllPersons = db.query(models.Person).all()
    return getAllPersons

@app.get('/getbyID/{customer_id}', response_model=PersonOut, status_code=status.HTTP_200_OK)
async def getBy_ID(customer_id:str):
    getByID = db.query(models.Person).filter(models.Person.customer_id == customer_id).first()
    if getByID is not None:
        return getByID
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")  

# Route to add a new person
@app.post('/add_customer', response_model=PersonOut, status_code=status.HTTP_200_OK)
def addPerson(person:PersonOut):
    newCustomer = models.Person(
        customer_id = person.customer_id,
        customer_name = person.customer_name,
        segment = person.segment,
        age = person.age,
        country = person.country,
        city = person.city,
        state = person.state,
        postal_code = person.postal_code,
        region = person.region
    )
    find_person = db.query(models.Person).filter(models.Person.customer_id == person.customer_id).first()
    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Person with this ID already exists")
    db.add(newCustomer)
    db.commit()
    return newCustomer

# Route to update a customer by ID
@app.put('/update_customer/{customer_id}', response_model=PersonOut, status_code=status.HTTP_202_ACCEPTED)
def updatePerson(customer_id:str, person:PersonOut):
    find_customer  = db.query(models.Person).filter(models.Person.customer_id == customer_id).first()
    if find_customer is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person with this ID does not exists")
    find_customer.customer_id = person.customer_id
    find_customer.customer_name = person.customer_name
    find_customer.segment = person.segment
    find_customer.age = person.age
    find_customer.country = person.country
    find_customer.city = person.city
    find_customer.state = person.state
    find_customer.postal_code = person.postal_code
    find_customer.region = person.region
    db.commit()
    return find_customer
    
# Route to delete a person by ID
@app.delete('/delete_person/{customer_id}', response_model=PersonOut, status_code=200)
def deletePerson(customer_id:str):
    find_person = db.query(models.Person).filter(models.Person.customer_id == customer_id).first()

    if find_person is not None:
        db.delete(find_person)
        db.commit()
        return find_person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person with this id is already deleted or doesn't exist")