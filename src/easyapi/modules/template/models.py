from application import BaseModel
from .constant import module_name

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from sqlalchemy import (
    String,
)

class DemoModel(BaseModel):
    __tablename__ = f"{module_name}_demo"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))