1. Installation of postgresql database

    1. First we have to install windows application locally so for that we have to go on this webside:https://www.enterprisedb.com/downloads/postgres-postgresql-downloads download that and install it and set a password which you remeber allways.
    2. Then in teminal firstly setup the fastapi setup and then run that  command :
    >command:

            pip install sqlalchemy
    3. After  that libraray for pydantic-settings helps us to load env variable in fastapi appliaction because env variables we configure for that we use this 
    >command:

            pip install pydantic-settings

2. Connecton with postgresql

    1. open pgadmin windows in left bar open object explorer you seems server just tap on that again you seems a directory  right tap on that and you see properties in ending tap on that and in top, tap connection bar you see some details.
    2. read all details and in .env file of you project folder make a varibale named as db_connection and in that write that 
    >link:

        "postgresql://{username}:{password}@{hostname}:{port}/{maintancedatabase}"
        write that requirement in link which are in brackets{} and write your own details at the place of that and remove brackets.

    3. Open settings.py in Utils folder of our source folder using that we load our db_connection with fastapi using following things.

            1. Write "from pydantic_settings import Basesetting,SettingsConfigDict".

            2. write "from pathlib import path" and on next line write " BASE_Dir = Path(__file__).resolve().parents[2] "

            3. Make a class with name as settings give a parenthesis write "BaseSettings" in parenthesis.

            4. Inside that class create a variable with name model_config and in that variable write "SettingsConfigDict" and in parenthesis write " env_file= BASE_Dir/ ".env",extra="ignore" ".

            5. Also write db_connection:str in that class and outside of class write " final_setting = Settings() ". 

    4. Now next we have to do configuration of db we do using sqlalchemy so for thta open db.py file
and in that we do following things:
            1. Write