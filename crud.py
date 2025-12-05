from sqlalchemy.orm import Session
from models import Jugador, Estadistica, Partido
from schemas import JugadorCreate, JugadorUpdate


    def crear_jugador(db: Session, jugadores: JugadorCreate, jugador_id: Optional[int] = None):
            
        jugadores_bd = bd.query(Jugador).filter(Jugador.numero_camiseta == jugador.numero_camiseta).first()
        if jugadores_bd:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Camiseta ya registrada"
            )
            
            jugadores_bd = Jugador(
                nombre_completo=jugadores.nombre_completo,
                numero_camiseta=jugadores.numero_camiseta,
                nacionalidad=jugadores.nacionalidad,
                fecha_nacimiento=jugadores.fecha_nacimiento,
                activo=jugadores.activo,
                altura=jugadores.altura,
                peso=jugadores.peso,
                pie_dominante=jugadores.pie_dominante,
                posicion=jugadores.posicion,
                valor=jugadores.valor,
                año_ingreso=jugadores.año_ingreso,
                estado=jugadores.estado
            )
            db.add(jugadores_bd)
            db.commit()
            db.refresh(jugadores_bd)
            return jugadores_bd
    
    def obtener_todos(db: Session, jugador_id: Optional[int] = None, solo_activos: bool = True):
        query = db.query(Jugador)
        
        if jugador_id is not None:
            query = query.filter(Jugador.jugador_id == jugador_id)
        
        if solo_activos:
            query = query.filter(Jugador.activo == True)
        
        return query.order_by(Jugador.año_ingreso.desc()).all()
    
    def buscar_por_texto(db: Session, texto: str, jugador_id: Optional[int] = None):
        query = db.query(Jugador).filter(Jugador.nombre_completo == texto).first()
        if not query:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Jugador no encontrado"
            )
        return query
    
    def obtener_por_id(db: Session, registro_id:int, jugador_id: Optional[int] = None):
        query = db.query(Jugador).filter(Jugador.id == jugador_id).first()
        
        if jugador_id is not None:
            query = query.filter(Jugador.jugador_id == jugador_id)
        
        return query
    
    def actualizar_registro(db: Session, registro_id: int, jugador_actualizar:JugadorUpdate, usuario_id: Optional[int] = None):
        jugadores = Jugador.obtener_por_id(db, registro_id, jugador_id)
        
        datos_actualizar = jugador_actualizar.dict(exclude_unset=True)
        for campo, valor in datos_actualizar.items():
            setattr(jugadores, campo, valor)
        
        bd.commit()
        bd.refresh(jugadores)
        return jugadores


    def eliminar_registro(db: Session, registro_id: int, jugador_id: Optional[int] = None):
        jugadores = Jugador.obtener_por_id(db, registro_id, jugador_id)
        if jugadores:
            jugadores.activo = False
            db.commit()
            return True
        return False
    
    @staticmethod
    def restaurar_registro(db: Session, registro_id: int, jugador_id: Optional[int] = None):
        jugadores = Jugador.obtener_por_id(db, registro_id, jugador_id)
        if jugadores:
            jugadores.activo = True
            db.commit()
            return True
        return False
    
    @staticmethod
    def eliminar_permanentemente(db: Session, registro_id: int, jugador_id: Optional[int] = None):
        jugadores = Jugador.obtener_por_id(db, registro_id, jugador_id)
        if jugadores:
            db.delete(jugadores)
            db.commit()
            return True
        return False