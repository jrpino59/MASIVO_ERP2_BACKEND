from app.db.database import Base, engine
from app.models.producto_model import Producto  # ← necesario para que SQLAlchemy registre la tabla

def crear_tablas():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    crear_tablas()
