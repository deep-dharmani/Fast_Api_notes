##  Using get method checking all postgre data in our fastapi response body:

1. *First we have to open First, we have to open controllers.py .*

2. *Now make a get_data in controllers.py in parentheses of that function write **db:Session**.*

3. *Now make a variable with the name `data` in that variable write **db.querry{Class that is imported from model.py }.all()**.*

4. *Now, for that class, return the `data` variable.*

5. *Now open router.py and make a decorator param of `get` using the variable of `APIRouter`*

6. *In parentheses for endpoint,You can give the name as /all_data.*

7. *Make a function with the name `all data`, and write**db = Depends(get_db)**,Now return `controllers.getdata`and write db in parenthesis.*

8. *Now you can get data in your API model, by using the endpoint as `/getdata`. *