from pydantic import BaseModel
from typing import List


class series(BaseModel):
    resourceURI: str
    name: str
    

class comics(BaseModel): 
    id: int
    title: str
    series:series


class comicdata(BaseModel):
    results: List[comics]

class respuestas(BaseModel):
    data: comicdata