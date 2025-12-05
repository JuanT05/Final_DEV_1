from pydantic import BaseModel, Field, validator
from typing import Optional

# ==========================
# 📘 Esquemas para Jugador
# ==========================
class JugadorBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre completo del jugador")
    pais: str = Field(..., min_length=2, max_length=50, description="País de origen del jugador")


class JugadorCreate(JugadorBase):
    pass


class JugadorResponse(JugadorBase):
    id: int

    class Config:
        orm_mode = True
