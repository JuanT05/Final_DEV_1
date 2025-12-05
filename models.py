class Jugador(base):
    __tablename__ = "jugadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    pais_origen = Column(String)
    anio_nacimiento = Column(Integer)
    pass


class Estadistica():
    pass


class Partido():
    pass


