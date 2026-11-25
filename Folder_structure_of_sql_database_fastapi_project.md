IF we are working on big application then we have knowledge about that how to make folder structure for a backened application.

1. Firstly we have to make a folder for that project.
2. In that folder make a file of .env in that we have to store enviroment variables and some other things maybe data urls or other things.
3. We have to make a source folder in that we have to store all our code data.
4. Outside of  that source folder means in root folder of our project we have to create main.py or code.py as you want in that we have to write main code for that app where we have import fastapi uvicorn other packages and do main code or root code for our Api but first we have setup fastapi and completely install that.
5. we have to make file .gitignore using that we push our project important files to github.
6. and in last we have to make a file named requirement.txt in that write all dependencies and packages for our that project.
7. Inside that source folder we create another folders first folder with name as utils that connect with data base and others according to features of our that app.
8. utils folder we have to make that all files which are used in that our other features folder as a supporting we have  create below files:

>__init__.py:

        It represents our tasks as module or a package.

>db.py:

        IN that we configure connection of a data base.

>constant.py:

        Values which are constant means which could'nt want to change are defined in this file.

>helpers.py:

        where we create some helpers functions.

>setting.py:

        Which provides required configuration for connection with data base.

9. Other folders according to feautures of our that project also has files every folder of feautures has same type of files means make all files in our folder for feutures which are given bellow:

>Models.py:

        Which helps in  define to connect tables of data base.

>router.py:

        In that we routes our all params works using our decoraters all endpoints are defined here.

>dtos.py:

        It means data transfer object means in that we define all requirement for request body of that feauture.

>controller.py:

        It adds our that data in our main sqldata base system.
