1. ## Installation of postgresql database

    1. *First we have to install application locally so for that we have to go on this website: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads download that according to your system and check install guidence for windows on:https://www.enterprisedb.com/docs/supported-open-source/postgresql/installing/windows/ .*

    2. *Then in teminal firstly setup the fastapi system fot that project folder and then run that  command :*
    >*command:*

            pip install SQLALchemy

    3. *After  that libraray for pydantic-settings helps us to load env variable in fastapi appliaction because env variables we configure for that we use this* 
    >*command:*

       pip install pydantic_settings

2. ## Connecton with postgresql

    1. *open pgadmin windows in left bar open object explorer you seems server just tap on that again you seems a directory  right tap on that and you see properties in ending tap on that and in top, tap connection bar you see some details.*

    2. *read all details and in .env file of you project folder make a varibale named as db_connection and in that write that*
    >*link:*

        "postgresql://{username}:{password}@{hostname}:{port}/{maintancedatabase}"
        write that requirement in link which are in brackets{} and write your own details at the place of that and remove brackets.

    3. *Open settings.py in Utils folder of our source folder using that we load our db_connection with fastapi using following things.*

        1. *write  **from pydantic_settings import Basesetting,SettingsConfigDict**.*

        2. *write  **from pathlib import path** and on next line write **BASE_Dir = Path(__file__).resolve().parents[2]***

        3. *Make a class with name as settings give a parenthesis write  **BaseSettings**  in parenthesis.*

        4. *Inside that class create a variable with name model_config and in that variable write    **SettingsConfigDict**  and in parenthesis write **env_file= BASE_Dir/".env",extra="ignore**.*

        5. *Also write **db_connection:str** in that class and outside of class write **final_setting = settings()**.*

    4. *Now next we have to do configuration of db we do using sqlalchemy so for that open db.py file and in that we do following things:*

        1. *Write **from sqlalchemy import create_engine** and on next line write **from sqlalchemy.orm import sessionmaker,declarative_base*** .

        2. *Write that **from {source file name}.utils.settings import  settings**.*

        3.*Create a variable with name base and in that write **declarative_base()** and create another variable with name engine in that write **create_engine(url=db_connection)**.*

        4. *Create another variable with name local_session on next line in that write **sessionmaker(bind=engine)**.*

        5. *Now we have to define a function with name get_db that provides us session when we need.*

        6. *Inside that function create a variable with name session write **local_session()***

        7. *Using try and finally identation write **yield session** in try and in finally write **session.close()***

    5. *Now we have to connect these base and engine with our main.py so for that we do following things in our main.py.*

        1. *Firstly write **from fastapi import FastApi,Depends** and create a variable in that write **FastApi()** and in parenthesis write *title=* that your fastapi application name you want.*

        2. *On top write **from {source_folder}.utils.db import base,engine**.*

        3. *Now write **base.metadata.create_all(engine)**.*

    6. *now we do some things in feautures foder Now open model.py of feuture folder.*

        1. *write **from sqlalchemy import Coloumn,String,Integer,Boolean**.*

        2. *one more important thing we write on next line is **from {source file}.utils.db import base** because that base is responsible to connect our model or our main table to actual data base.*

        3. *Now make a class and give name according to your feauture and in parenthesis write base.*

        4. *In class create a variable with name **__tablename__**  in that write that your data name as you want in double code.*

        5. *In class also write those coloumns for our that table so write all these in that form :{coloumn name}=Coloumn({Integer/String/Boolean}).*
 
    7. *Now we cretae seprate routes so we have to open router.py file and do following things:*

        1. *firstly we have to import Api router from fastapi in that form :**from fastapi import APIRouter**.*
        
        2. *Create a variable with name routes and assign **APIRouter(prefix="/{your feature name}")** .*

        3. *Now open main.py file and we connect that our router with main code so for that first we have to write **from src.{feuture file name}.router import {variable where APIRouter is stored }** and also write **{variable where we stored FastApi()}.include_router({that imported variable from router file})***

    8. *Now open dtos.py where we have to write all requirement for our request body using pydantic so for that*

        1. *write **from pydantic import BaseModel***

        2. *Make a class in parethesis write BaseModel*

        3. *Inside that class write that your all requirement with their datatype and you can set default value that should be told as schema.*
    
    9. *Now we have to connect that schema with our router beacuse that data body should be recieved by our router.*

        1. *In router file import class of request body which is in dtos file and also import get_db from db.py file of Utils folder* 

        2. *Make a post param using that variable of APIRouter and in parenthesis of function that post param write**body:{that imported class from dtos.py file},db=Depends(get_db)***

        3. *Now open controller.py import that schema class body of dtos.py file,also import that class of model.py file ,write **from sqlalchemy.orm import Session** and create a function in parenthesis of that function write**body:{imported schema class},db:Session**,make a variable with name as data another with new_table , in data variable write**body.model_dump()** ,in new_table write **{imported class}({name of that coloumn where you store first thing}=data["{that name by you stored that coloumn thing in schema class of dtos.py}"]) and write those all couloumns which you want in that parenthesis** and now outside of new_task on second line write **db.add(new_task)** , write**db.commit()**and in last write **db.refresh(new_task)***

        4. Finally you have to go on your main.py file and just run that using uvicorn and give your request things.

        5. open pgadmin and click on server,click on database and click on that maintance data name which you give in the ending of path of url,click on schemas and you can see that table name which you give just right click on that it shows view/edit click on that and click all rows rows you see that your given cloumn means it saves your that information which is given using your api.
