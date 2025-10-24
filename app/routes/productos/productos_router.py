from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.producto_model import Producto
from app.schemas.producto_schema import ProductoCreate, ProductoOut

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# Conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Obtener todos los productos
@router.get("/", response_model=list[ProductoOut])
def obtener_productos(db: Session = Depends(get_db)):
    productos = db.query(Producto).all()
    return productos

# ✅ Crear un nuevo producto
@router.post("/", response_model=ProductoOut)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = Producto(**producto.dict())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

# ✅ Obtener un producto por ID
@router.get("/{id}", response_model=ProductoOut)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

# ✅ Actualizar un producto existente
@router.put("/{id}", response_model=ProductoOut)
def actualizar_producto(id: int, datos_actualizados: ProductoCreate, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    for campo, valor in datos_actualizados.dict().items():
        setattr(producto, campo, valor)

    db.commit()
    db.refresh(producto)
    return producto

# ✅ Eliminar un producto existente
@router.delete("/{id}")
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    producto = db.query(Producto).filter(Producto.id == id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    db.delete(producto)
    db.commit()
    return {"mensaje": f"Producto con ID {id} eliminado correctamente"}
