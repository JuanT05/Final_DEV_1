from pydantic import BaseModel
from typing import Optional, List


# ===========================
#        JUGADOR
# ===========================

class JugadorBase(BaseModel):
    nombre_completo: str
    numero_camiseta: int
    nacionalidad: str
    fecha_nacimiento: str
    activo: Optional[bool] = True

    altura: int
    peso: int
    pie_dominante: str
    posicion: str
    valor: int
    año_ingreso: int
    estado: str


class JugadorCreate(JugadorBase):
    pass


class JugadorUpdate(BaseModel):
    nombre_completo: Optional[str] = None
    numero_camiseta: Optional[int] = None
    nacionalidad: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    activo: Optional[bool] = None

    altura: Optional[int] = None
    peso: Optional[int] = None
    pie_dominante: Optional[str] = None
    posicion: Optional[str] = None
    valor: Optional[int] = None
    año_ingreso: Optional[int] = None
    estado: Optional[str] = None


class JugadorRead(JugadorBase):
    id: int
    estadistica: List["EstadisticaRead"] = []
    partido: List["PartidoRead"] = []

    class Config:
        orm_mode = True


# ===========================
#       ESTADISTICA
# ===========================

class EstadisticaBase(BaseModel):
    tiempo_cancha: int
    numero_goles: int
    faltas: int
    targetas_resividas: str


class EstadisticaCreate(EstadisticaBase):
    jugador_id: int


class EstadisticaUpdate(BaseModel):
    tiempo_cancha: Optional[int] = None
    numero_goles: Optional[int] = None
    faltas: Optional[int] = None
    targetas_resividas: Optional[str] = None


class EstadisticaRead(EstadisticaBase):
    id: int
    jugador_id: Optional[int]

    class Config:
        orm_mode = True


# ===========================
#         PARTIDO
# ===========================

class PartidoBase(BaseModel):
    goles_equipo_sigFC: str
    goles_equipo_rival: str
    penales: bool
    npenales_gol_sigFc: bool
    npenales_gol_rival: bool
    resultado_partido: str


class PartidoCreate(PartidoBase):
    jugador_id: int


class PartidoUpdate(BaseModel):
    goles_equipo_sigFC: Optional[str] = None
    goles_equipo_rival: Optional[str] = None
    penales: Optional[bool] = None
    npenales_gol_sigFc: Optional[bool] = None
    npenales_gol_rival: Optional[bool] = None
    resultado_partido: Optional[str] = None


class PartidoRead(PartidoBase):
    id: int
    jugador_id: Optional[int]

    class Config:
        orm_mode = True


# ===========================
#   Resolver referencias
# ===========================

JugadorRead.update_forward_refs()
