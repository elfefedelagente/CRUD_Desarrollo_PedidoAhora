from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import datetime


class ProductoBase(BaseModel):
    nombre:str
    precio:float
    descripcion: Optional[str] = None

class Producto(ProductoBase):
    id:int
    nombre:str
    precio:float
    descripcion:str
    fecha_creacion: datetime.datetime
    fecha_modificacion: datetime.datetime

    class Config:
        orm_config = True
    
class ProductoCreate(ProductoBase):
    pass



#ProductoOut()
'''
    Incluye todos los atributos que quieres devolver cuando la API responde
class ProductoOut(ProductoBase):
    id: int
    fecha_creacion: datetime
    fecha_modificacion: Optional[datetime] = None
'''
