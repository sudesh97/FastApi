    # schemas.py (or similar)
    from pydantic import BaseModel

    class UserSchema(BaseModel):
        id: int
        username: str
        email: str | None = None
        full_name: str | None = None

        class Config:
            orm_mode = True # Important for SQLAlchemy integration