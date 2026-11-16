>pydantic:

            Imagine if in request body someone use str at place of int means give a different data type in request then it gives eror but python has built in library which is pydantic ,In pydantic we have to explain exact shape that we expect means we have to describe which field,their data and rule of that field so that pydantic see request from user if it dos'nt follows our rulles then it directly rejects that and give clear explanation which thing is wrong in request so as you know we have request body in json so pydantic convert that in proper python object with validated field then function recieve and clean then gives our result.

FOR example programme check:https://github.com/deep-dharmani/Fast_Api_notes/blob/main/practice_projects/age_to_apply.py 
                                         and 
