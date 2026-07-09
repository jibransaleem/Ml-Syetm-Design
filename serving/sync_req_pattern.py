from fastapi import FastAPI
import time


# --------------- dumy serverv  :: having too end point exponse one has no latency  , one has 5 sec latency------------------
app = FastAPI()


@app.post("/pred/{value}")
def time_pred(value: int):
    time.sleep(5)
    return {"result": value + 1}


@app.post("/preds/{value}")
def pred(value: int):
    return {"result": value + 1}


@app.get("/")
def home():
    return {"message": "api"}


# ----------------------- user perspective : request serving ----------------------------------
import requests


# example user wants to take loan from bank so there fore make a sync call to server so can block him for response , untill he can wait: 2 cases

# case :1  => all good but if server crashes all things will slowly crash 

def make_request1():
    try:
        out = requests.post("http://localhost:8000/preds/10")
        print(out.status_code)
        print(out.json())
    except requests.Timeout:
        print("Request took too much time to execute")

# case :2 => hanldes the server crash by using timeout so request fallbacks and nothing would happen
def make_request2():
    try:
        out = requests.post("http://localhost:8000/preds/10" , timeout=3)
        print(out.status_code)
        print(out.json())
    except requests.Timeout:
        print("Request took too much time to execute")

make_request1()

make_request2()