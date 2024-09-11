import os, asyncio
from dotenv import load_dotenv
from fastapi import FastAPI
from database import engine, Base
#from src.models import Producto
from src.routes import router as routers
from sqlalchemy.future import select


#Conecccion con el frontend
'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permitir el origen de tu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los headers
)
'''

load_dotenv()#.env
#DATABASE_URL = os.getenv("DB_URL")
ENV = os.getenv("ENV", "DEV")
ROOT_PATH = os.getenv(f"ROOT_PATH_{ENV.upper()}", "")


app = FastAPI(root_path=ROOT_PATH)
app.include_router(routers)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # Crear todas las tablas

async def main():
    await init_db()

if __name__ == "__main__":
    asyncio.run(main())

