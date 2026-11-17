>HTTP Exception:

Using http exception we can easily handels erors in fastapi, so for that we have to just when we are import FastAPI comma HTTPException and in that decorater function we have to raise before return just have to write raise HTTPException and inside parenthesis write statuscode=that status code of eror comma detail=that line which we want to give at place of eror.

If it gives eror which are unexcepted means we are unaware from that eror then we have to use try and except but in except block we have to raise HTTPException at the place of Exception. 

-Conclusion:

    - So we can do  three things in fastapi for eror handling first one is pydantic second is HTTPException and third is Try and Except. 
 