from fastapi import FastAPI
from routes import agent_analyze

app = FastAPI()


app.include_router(agent_analyze.router)






