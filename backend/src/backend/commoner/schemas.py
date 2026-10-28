from datetime import date
from enum import Enum
from pydantic import BaseModel, Field

# 
class Status(str, Enum):
    ACTIVO = "activo"
    INACTIVO = "inactivo"
    FALLECIDO = "fallecido"
    SUSPENDIDO = "suspendido"


class Commoner(BaseModel):
    dni: str = Field(pattern=r"^\d{8}$")
    name: str = Field(min_length=1, max_length=50)
    last_name: str = Field(min_length=1, max_length=100)
    date_of_birth: date
    phone_number: str = Field(pattern=r"^\d{9}$")
    status: Status