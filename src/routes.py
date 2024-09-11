from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db 
from src import schemas, services

router = APIRouter()

############################################################  ROUTER PRODUCTO ############################################################
@router.post("/producto", response_model=schemas.Producto)
async def create_producto(producto: schemas.ProductoCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await services.crear_producto(db, producto)
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))