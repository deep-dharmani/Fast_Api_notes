import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
age_app=FastAPI()
@age_app.get("/")
def age():
    return{"massege":"using age page give age and verify"}
class age_verify(BaseModel):
    age__:int
@age_app.post("/age")
def predict_age(application:age_verify):
    if application.age__>18 and application.age__<=40:
        decision="validate to apply"
    else:
        decision=f"not validate to apply with {application.age__} age"
    return {"decision":decision}
if __name__ == "__main__":
    uvicorn.run("age_to_apply:age_app", host="127.0.0.1", port=8000, reload=True)