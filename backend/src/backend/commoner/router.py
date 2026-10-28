from fastapi import APIRouter
from .schemas import Commoner

router = APIRouter(prefix="/commoners", tags=["commoners"])

@router.get("/")
def get_all_commoners():
    return {
        "message" : "here will be all commoners list"
    }


@router.post("/")
def create_commoner(commoner: Commoner):
    return {
        "message": "Datos válidos",
        "data": commoner.model_dump()
    }

