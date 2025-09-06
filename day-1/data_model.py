from pydantic import BaseModel


class NewStudent(BaseModel):
    name: str
    age: int
    course: str


class UpdateStudent(BaseModel):
    name: str | None = None
    age: int | None = None
    course: str | None = None
