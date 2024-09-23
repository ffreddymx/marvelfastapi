from fastapi import FastAPI
from typing import Union
import time
import hashlib
import requests
from models import respuestas



app = FastAPI()

KEY_PUBLICA = "b146cbaabaa231073c59364ea1fe93f8"
KEY_PRIVADA = "ab0446730a01c5e1cf73f185832f0b9aecb9ba41"
MARVEL_API = "https://gateway.marvel.com/v1/public/characters"


ts = str(time.time())
hash_s = ts + KEY_PRIVADA + KEY_PUBLICA    

@app.get("/comics/{name}")
def read_root(name: str):
    ts = str(time.time())
    hash_s = hashlib.md5((ts + KEY_PRIVADA + KEY_PUBLICA).encode()).hexdigest()
    
    url = f"http://gateway.marvel.com/v1/public/comics?title={name}&ts={ts}&apikey={KEY_PUBLICA}&hash={hash_s}"
    response = requests.get(url)
    resultado = respuestas(**response.json())
    return resultado




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


#http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150