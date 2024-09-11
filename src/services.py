from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from src import schemas, models
from database import SessionLocal


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

############################################################  CRUD PRODUCTO ############################################################

async def crear_producto(db: AsyncSession, producto:schemas.ProductoCreate) -> schemas.ProductoCreate:
    new_producto = models.Producto(
        nombre=producto.nombre,
        precio=producto.precio,
        descripcion=producto.descripcion
    )
    try:
            db.add(new_producto)
            await db.commit()  # Hacer commit de la transacción
            await db.refresh(new_producto)  # Refrescar la instancia dentro de la misma transacción
    except Exception as e:
            await db.rollback()  # Hacer rollback en caso de error
            raise HTTPException(status_code=400, detail="Error al crear producto") from e
        
        # Retorna el producto creado
    return new_producto

