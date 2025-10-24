from fastapi import APIRouter

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.get("/")
def obtener_clientes():
    return {"mensaje": "Módulo Clientes operativo"}
