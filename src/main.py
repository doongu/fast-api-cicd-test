from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check_handler():
    return {"ping": "pong"}


todo_data = {
    1: {
        "id": 1,
        "contents": "실전",
        "is_done": True,
    },
    2: {
        "id": 2,
        "contents": "실전",
        "is_done": True,
    },
    3: {
        "id": 3,
        "contents": "실전",
        "is_done": True,
    },
 }

@app.get("/todos")
def get_todos_handler():
    return list(todo_data.values())

