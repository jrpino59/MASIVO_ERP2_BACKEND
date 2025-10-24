from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base  # ✅ Importar el mismo Base usado en create_all()

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Float, nullable=False)
