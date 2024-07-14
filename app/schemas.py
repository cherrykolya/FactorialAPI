from pydantic import BaseModel


class FactorialResponse(BaseModel):
    value: str
