import json
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import models
from database import SessionLocal, engine
#note:normally you'd want to use migrations
models.Base.metadata.create_all(bind=engine)

from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import register_tortoise
app = FastAPI()
db=[]
templates = Jinja2Templates(directory="templates")


class Date(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    #id = fields.IntField(pk=True)
    cargo_type=fields.CharField(max_length=200,unique=True)
    rate=fields.IntField()
    freight_amount=fields.IntField()
Date_Pydantic = pydantic_model_creator(Date,name='Date')



class Tariff(BaseModel):
    cargo_type: str
    rate: float
    freight_amount: float


with open('tariff.json', 'r') as f:
    data = json.load(f)['Date']
    tariff_list = [Tariff(**item) for item in data]


# print(Date)
@app.get("/date/")
def get_date():
    return {"Date": data}


@app.get("/cargo/", response_class=HTMLResponse)
def get_cargo(request: Request):
    cargo_types = [tariff.cargo_type for tariff in tariff_list]
    return templates.TemplateResponse("cargo_item.html", {"request": request, "cargo_types": cargo_types})


@app.post("/calculate")
def calculate_cost_of_insurance(request: Request, cargo: str = Form()):
    # Find the cargo rate and freight amount for the selected cargo
    selected_tariff = next((tariff for tariff in tariff_list if tariff.cargo_type == cargo), None)
    if selected_tariff is None:
        return {"message": "Invalid cargo type"}

        # Calculate the insurance cost
    insurance_cost = selected_tariff.rate * selected_tariff.freight_amount

    return {"insurance_cost": insurance_cost}

register_tortoise(
    app,
    db_url='sqlite://app.db',
    modules={'models':['main']},
    generate_schemas=True,
    add_exception_handlers=True


)