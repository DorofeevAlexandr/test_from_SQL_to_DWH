from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase): 
    pass


class Area(Base):
    __tablename__ = 'area'

    id = Column(Integer, primary_key=True)
    hh_id = Column(Text, unique=True)
    name = Column(Text)
    url = Column(Text)
    vacancies = relationship("Vacancies", back_populates="area")


class Employer(Base):
    __tablename__ = 'employer'

    id = Column(Integer, primary_key=True)
    hh_id = Column(Text, unique=True)
    name = Column(Text)
    url = Column(Text)
    vacancies = relationship("Vacancies", back_populates="employer")


class Vacancies(Base):
    __tablename__ = 'vacancies'

    id = Column(Integer, primary_key=True)
    hh_id = Column(Text, unique=True)
    name = Column(Text)
    area_id = Column(Integer, ForeignKey("area.id"), nullable=False)
    area = relationship("Area", back_populates="vacancies")
    employer_id = Column(Integer, ForeignKey("employer.id"), nullable=False)
    employer = relationship("Employer", back_populates="vacancies")
    published_at = Column(Text)
    created_at = Column(Text)
    url = Column(Text)
