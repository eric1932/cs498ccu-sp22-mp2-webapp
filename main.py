from fastapi import FastAPI
from pydantic import BaseModel

import seed_model


class RequestItem(BaseModel):
    num: int


app = FastAPI()


@app.post("/")
def update_seed_value(item: RequestItem):
    if item.num:
        seed_model.set_seed_value(item.num)
        return {"code": 0}
    else:
        return {"code": -1}


@app.get("/")
def get_seed_value():
    return seed_model.get_seed_value()
