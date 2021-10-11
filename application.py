import uvicorn
from fastapi import FastAPI

import route_example
import webhook_example

app = FastAPI()

app.include_router(route_example.router)
app.include_router(webhook_example.router)


if __name__ == '__main__':
    uvicorn.run("application:app", host="127.0.0.1", port=7040, log_level="debug")
