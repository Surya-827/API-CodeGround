from typing import Union
from fastapi import FastAPI

#Below Command to Run Specific Sever Module
#uvicorn your_module_name:app --reload

app = FastAPI()

@app.get("/Hello-world")
def Hello():
    data = {
        "message": "hello world",
        "details": {
            "author": {
                "name": "Tushar",
                "email": "tushar@example.com"
            },
            "tags": ["fastapi", "python", "web"]

        }
    }
    return data

@app.get("/surya-info")
def surya():
    data = {
        "message" : "User Info",
        "details" : {
            "author" : {
                "name" : "Surya Kiran"
            },
            "contact" : {
            "email" : "surya@gmail.com",
            "phone" : "+9189338949"
            },
            "tags" : ["fastapi","python","web"]
        }
    }

    return data



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
