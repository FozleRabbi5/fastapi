from datetime import datetime
from typing import Optional
from typing_extensions import Annotated
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import BIGINT, TIMESTAMP, VARCHAR, ForeignKey, Integer, func


int_pk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]

user_fk = Annotated[
    int, mapped_column(BIGINT, ForeignKey(
        "users.id", ondelete='SET NULL'
    ))
]

str_255 = Annotated[str, mapped_column(VARCHAR(255))]

class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )

    class Config:
        abstract = True

class TableNameMixin:

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

class User(Base, TimestampMixin, TableNameMixin):

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    full_name:Mapped[str_255]
    # full_name: Mapped[str] = mapped_column(VARCHAR(255))
    username:Mapped[Optional[str_255]]
    # username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    referrer_id: Mapped[Optional[user_fk]]

    # referrer_id: Mapped[int] = mapped_column(
    #     BIGINT,
    #     ForeignKey('users.id', ondelete='SET NULL'),
    #     nullable=True
    # )

class Product(Base, TimestampMixin, TableNameMixin):
    product_id: Mapped[int_pk]
    title:Mapped[str_255]
    description: Mapped[Optional[str_255]]
    price: Mapped[float] = mapped_column(VARCHAR(3000))


class Order(Base, TimestampMixin, TableNameMixin):
    order_id: Mapped[int_pk]
    user_id: Mapped[user_fk]

class OrderProduct(Base, TimestampMixin, TableNameMixin):
    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("orders.order_id", ondelete="CASCADE"),
        primary_key=True,
    )

    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.product_id")
    )

    quantity: Mapped[int]

