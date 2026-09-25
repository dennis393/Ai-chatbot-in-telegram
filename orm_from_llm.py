import asyncio
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func, Text, UniqueConstraint, BigInteger, SmallInteger, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from dotenv import load_dotenv 
import os

class Base(DeclarativeBase):
    pass

load_dotenv()


CONN_DB =  create_async_engine(f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")


class chatHistory(Base):
    __tablename__ = "chat_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True)
    
class LongMemory(Base):
    __tablename__ = "long_memory"
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(String(100)) #обо мне, о роли ИИ для этого
    fact: Mapped[str] = mapped_column(Text, nullable=False) #Факты о юзере чтобы ИИ помнил
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    
async_session = sessionmaker(bind=CONN_DB, class_=AsyncSession, expire_on_commit=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with CONN_DB.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await CONN_DB.dispose()    