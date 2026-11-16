import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Literal
health_insurance_app=FastAPI()
class insurance_form(BaseModel):
    patient_age:int
    monthly_income:int=Field(le=100000,ge=0)
    gender_income:Literal["male","female","custom"]
    need_insurance:int=Field(le=300000,ge=50000)
@health_insurance_app.post("/")
def form(application:insurance_form):
    if application.gender_income=="female" and application.monthly_income<=25000:
        decision=f"Approved sure we will give you {application.need_insurance}"
    elif application.gender_income=="male" and application.monthly_income<=40000:
        decision=f"Approved we will give {application.need_insurance-15000}"
    elif application.gender_income=="custom" and application.monthly_income<=30000:
        decision=f"Approved we give you {application.need_insurance-5000}"
    elif application.monthly_income<=70000:
        decision=f"Approved we will give {application.need_insurance-25000}"
    else:
        decision="Application rejected you can come at bank if need importantly"
    return {"decision":decision}
if __name__=="__main__":
    uvicorn.run("health_insurance:health_insurance_app",host="127.0.0.1",port=8000)