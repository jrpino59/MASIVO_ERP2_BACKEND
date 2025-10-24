from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.home import router as home_router
from app.routes.clientes.clientes_router import router as clientes_router
from app.routes.productos.productos_router import router as productos_router
from app.routes.ventas.ventas_router import router as ventas_router


app = FastAPI(
    title="MASIVO_ERP2",
    description="ERP desarrollado con FastAPI",
    version="1.0.0"
)

# --- Configuración CORS ---
origins = [
    "http://localhost:5173",   # Frontend Svelte local
    "http://127.0.0.1:5173",   # Alternativa local
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- Fin configuración CORS ---


# --- Rutas del sistema ---
app.include_router(home_router)
app.include_router(clientes_router)
app.include_router(productos_router)
app.include_router(ventas_router)
# --- Fin rutas del sistema ---
