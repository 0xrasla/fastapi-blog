from pydantic import BaseModel


class Blog(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        orm_mode = True


class BlogCreate(BaseModel):
    title: str
    body: str
