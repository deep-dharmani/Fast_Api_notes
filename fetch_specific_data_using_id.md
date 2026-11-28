*When we are making a new endpoint, first of all, focus on to define a controller if already, the model is defined in that If not, then focus on to first of all defining the model, then the controller And when our controller is defined fully and perfectly, then we have to connect controller with routes and finally, we use those routes in main.py.* 

## Make a route to fetch specific data.

1. *In routers.py, make a get param Using route variable and in parentheses give endpoint as /get data/{one_row}.*

2. *make a function with the name `get_one_row`.*

3. *write **{Write the name of that row}:{Write the data_type of the data which is present in that row},db:Session** in the parentheses of that function.* 

4. *Make a variable in that variable with name one_row , write**db.querry({Class that is imported from model.py}).get()***

5. *`from fastapi import HTTPException` at the top.*

6. *Make an `if` indented block and condition as **not one_row** and in that,return HTTPException, give a parenthesis, and in that (parentheses) write **404,detail="Not found"***.

7. *outside of the `if ` indented block return **{"msg":"Fetched successfully","data":one_row}***.

8. *In routers.py, make a get param Using route variable and in parentheses give endpoint as /get data/{one_row}.*

9. *Define a class, in that class (Parenthesis)  write **one_row:{data typeof that info},db=Depends(get_db)***

10. *Inside that function `return` **controller.get_one_row(one_row,db)***.

11. *Now you can see your specific row, Just you have to give end point as **/get data/{that row info}***
