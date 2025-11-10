    # models.py (or similar)
    from sqlalchemy import create_engine, Column, Integer, String
    from sqlalchemy.orm import sessionmaker, declarative_base

    DATABASE_URL = "mssql+pyodbc://DESKTOP-04TR8M0\SQLEXPRESS/TTCabBookingDb1?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes"

    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, index=True)
        username = Column(String, unique=True, index=True)
        email = Column(String)
        full_name = Column(String)