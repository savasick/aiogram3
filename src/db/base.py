import asyncio
import sqlite3
import aiosqlite

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.settings import config

Base = declarative_base()

from.models import *

def get_database_url():
    return f'postgresql+asyncpg://{config.BOT_DATABASE_USER}:{config.BOT_DATABASE_PASSWORD.get_secret_value()}@{config.BOT_DATABASE_HOST}:{config.BOT_DATABASE_PORT}/{config.BOT_DATABASE_NAME}'

def get_sqlite_url():
    return 'sqlite+aiosqlite:///sqlite.db'

async def create_database_session():
    try:
        engine = await create_async_engine(get_database_url())
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        return async_session
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        engine = create_async_engine(get_sqlite_url())
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        return async_session

async def get_database_session():
    try:
        engine = await create_async_engine(get_database_url())
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        return async_session
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        engine = create_async_engine(get_sqlite_url())
        async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
        return async_session

def setup_database():
    try:
        engine = create_engine(f'postgresql://{config.BOT_DATABASE_USER}:{config.BOT_DATABASE_PASSWORD.get_secret_value()}@{config.BOT_DATABASE_HOST}:{config.BOT_DATABASE_PORT}/{config.BOT_DATABASE_NAME}')
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        engine = create_engine('sqlite:///sqlite.db')
        Base.metadata.create_all(engine)
