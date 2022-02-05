from app import db
from sqlalchemy import(
    Column,
    Integer,
    String
)

class Persona(db.Base):

    """Clase creada para ser el modelo de la tabla Persona
    en la base de datos mydatabase.sqlite
    
    La tabla PERSONAS tiene los mismos atributos de clase
    con el id de cada persona que se registre
    
    Attributes:
        * name (str): nombre de la persona que se registra
        * email (str): email de la persona que se registra
        * city (str): ciudad de la persona que se registra
        Todos los atributos son obligatorios y se verifican
        en el formulario app/forms/FormPerson.py en la clase
        Persona
    """

    __tablename__ = 'PERSONAS'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    email = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)

    def __init__(self, name: str, email: str, city: str):
        self.nombre = name
        self.email = email
        self.ciudad = city
