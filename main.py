from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wiki_logic
from mylib.logic import phrase as wiki_phrase

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Wikipedia API. call/search_wiki"}

@app.get("/search/{value}")
async def search(value:str):
    """Page to Search Wikipedia"""
    result = search_wiki(value)
    return {"result":result}

@app.get("/wiki/{name}")
async def wiki(name:str):
    """Retrieve Wikipedia Page"""
    result = wiki_logic(value)
    return {"result"}

@app.get("/phrase/{name}")
async def phrase(name:str):
    result = wiki_phrase(name)
    return {"result":result}
if __name__ == "__main__":
    uvicorn.run(app,port=8080,host='0.0.0.0')
# result = wiki()
# print(result)
