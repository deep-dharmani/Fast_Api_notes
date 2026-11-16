import uvicorn
from fastapi import FastAPI
stuedent_app=FastAPI()
stuedents={
    1111:{"name":"Deep","class":"11th", "behaviour":"mannerfull"},
    1112:{"name":"Praveer","class":"11th","behaviour":"not mannerable"},
    1113:{"name":"Aziz","class":"11th","behaviour":"not mannerable"}
}
@stuedent_app.get("/info/{stuedent_id}")
def stuendts_info(stuedent_id:int):
    if stuedent_id not in stuedents:
        return{"eror":f"{stuedent_id} is invalid id"}
    else:
        return {"Name":stuedents[stuedent_id]["name"],
                "Class":stuedents[stuedent_id]["class"],
                "Behaviour":stuedents[stuedent_id]["behaviour"]}
@stuedent_app.get("/stuedents")
def stuedents_(class_:str="11th",behaviour:str="mannerfull"):
    quary=[]
    for c in stuedents.values(): 
        if c["class"]==class_ and c["behaviour"]==behaviour:
            quary.append(c["name"])
    return quary
if __name__=="__main__":
    uvicorn.run("stuedent_info:stuedent_app",host="127.0.0.1",port=8000,reload=True)