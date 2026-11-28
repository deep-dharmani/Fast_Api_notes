## update table 

1. *First open `routers.py` make a post param using the variable of APIRouter and give endpoint as `update_table`.*

2. *Define a function with name `update_table` in the parenthesis of that write `body:{That imported class from dtos},{speciallity for all rows}:{type of that speciallity},db:Depends({imported function from db.py})`*

3. *Open controller.py and define a function with name as `update_stuedent` in the parenthesis of that write `body:{imported class from model.py},{speciallity for all rows}:{type of that speciallity},db:Session`*

4. *Inside that, make a variable with name `one_row` in that variable write`db.query({Imported class from model.py}).filter({Imported class from model.py}.{Specialty for all rows}:{type of that specialty}).first()`*

5. *Make an if condition and write command as `not one_row`and inside that identified condition, write `return HTTPException(404, detail="not found")`.*

6. *Outside of that idented block condition of if, write `one_row.{row name}=body.{row name}` and write in that form for all rows, line by line.*

7. *Write `db.add(one_row)` on the next line and on another line, write `db.commit()` also write on another line: `db.refresh(one_row)`.*

8. *And finally, return a dictionary with key `message` and value `f"updated successfully {one_row}"`.*

9. *Now you can use that by using the endpoint as `/update_table`*.

10. Hello, how are you?