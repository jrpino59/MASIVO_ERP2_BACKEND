from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"mensaje": "¡Bienvenido a MASIVO_ERP2 - API modular!"}
