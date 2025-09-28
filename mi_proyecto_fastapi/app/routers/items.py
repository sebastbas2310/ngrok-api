# mi_proyecto_fastapi/app/main.py
from fastapi import FastAPI
from mi_proyecto_fastapi.app.routers import items  # <-- aquí importas tus rutas

app = FastAPI()
app.include_router(items.router)  # registras tus endpoints
