from sqlalchemy.orm import Session
from models import Jugador, Estadistica, Partido
from schemas

 @staticmethod
    def crear_jugador(db: Session, nombre_completo: str, numero_camiseta: int, nacionalidad: str, 
                                    nacionalidad: str, fecha_nacimiento: str, activo: bool, altura: int, 
                                    peso: int, pie_dominante: str, posicion: str, valor: int, año_ingreso: int, 
                                    estado: str, jugador_id: Optional[int] = None):
        jugadores = Jugador(
            nombre_completo=nombre_completo,
            numero_camiseta=numero_camiseta,
            nacionalidad=nacionalidad,
            fecha_nacimiento=fecha_nacimiento,
            activo=activo,
            altura=altura,
            peso=peso,
            pie_dominante=pie_dominante,
            posicion=posicion,
            valor=valor,
            año_ingreso=año_ingreso,
            estado=estado
        )
        db.add(jugadores)
        db.commit()
        db.refresh(jugadores)
        return jugadores
    
    @staticmethod
    def obtener_todos(db: Session, jugador_id: Optional[int] = None, solo_activos: bool = True):
        query = db.query(Jugador)
        
        if jugador_id is not None:
            query = query.filter(Jugador.jugador_id == jugador_id)
        
        if solo_activos:
            query = query.filter(Jugador.activo == True)
        
        return query.order_by(Jugador.año_ingreso.desc()).all()
    
    @staticmethod
    def buscar_por_texto(db: Session, texto: str, jugador_id: Optional[int] = None, solo_activos: bool = True):
        query = db.query(Jugador).filter(
            Jugador.nombre_completo.ilike(f"%{texto}%")
        )
        
        if jugador_id is not None:
            query = query.filter(Jugador.jugador_id == jugador_id)
        
        if solo_activos:
            query = query.filter(Jugador.activo == True)
        
        return query.order_by(Jugador.año_ingreso.desc()).all()
    
    @staticmethod
    def obtener_por_id(db: Session, registro_id:int, jugador_id: Optional[int] = None):
        query = db.query(Jugador).filter(Jugador.id == jugador_id)
        
        if jugador_id is not None:
            query = query.filter(Jugador.jugador_id == jugador_id)
        
        return query.first()
    
    @staticmethod
    def actualizar_registro(db: Session, registro_id: int, nombre_completo: str = None, numero_camiseta: int = None,
                                        nacionalidad: str = None, fecha_nacimiento: str = None, activo: bool = None, altura: int = None,
                                        peso: int = None, pie_dominante: str = None, posicion: str = None, valor: int = None, año_ingreso: int = None, estado: str = None;
                                        usuario_id: Optional[int] = None):
        jugadores = Jugador.obtener_por_id(db, registro_id, jugador_id)
        if jugadores:
            if nombre_completo is not None:
                jugadores.nombre_completo = nombre_completo
            if numero_camiseta is not None:
                jugadores.numero_camiseta = numero_camiseta
            if nacionalidad is not None:
                jugadores.nacionalidad = nacionalidad
            if fecha_nacimiento is not None:
                jugadores.fecha_nacimiento = fecha_nacimiento
            if activo is not None:
                jugadores.activo = activo
            if altura is not None:
                jugadores.altura = altura
            if peso is not None:
                jugadores.peso = peso
            if pie_dominante is not None:
                jugadores.pie_dominante = pie_dominante
            if posicion is not None:
                jugadores.posicion = posicion
            if valor is not None:
                jugadores.valor = valor
            if año_ingreso is not None:
                jugadores.año_ingreso = año_ingreso
            if estado is not None:
                jugadores.estado = estado

            db.commit()
            db.refresh(jugadores)
        return jugadores

    
    @staticmethod
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