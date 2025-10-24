from fastapi import APIRouter

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)

@router.get("/")
def obtener_ventas():
    return {"mensaje": "Módulo Ventas operativo"}
