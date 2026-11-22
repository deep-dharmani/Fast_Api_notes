import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from products import _products_
product_app=FastAPI()
class products_info(BaseModel):
    id:int
    name:str
    price:int
    count:int
@product_app.get("/all_products")
def my_product():
    return _products_
@product_app.put("/update_produts/{product_id}")
def products_update(product_id:int,products_info:products_info):
    for index,product in enumerate(_products_):
        if product.get("id")==product_id:
            _products_[index]=products_info.model_dump()
            return{"msg":f"Succesfully change..."}
    return{"msg":"product not found"}
@product_app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,product in enumerate(_products_):
        if product.get("id")==product_id:
            deleted=_products_.pop(index)
            return {"msg":"Deleted succesfully","product":deleted}
    return {"msg":"Product not found"}
uvicorn.run("products_supply:product_app",host="127.0.0.1",port=8002)