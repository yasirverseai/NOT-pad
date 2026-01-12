# app/database.py
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("SUPABASE_DB_URL")
# DATABASE_URL = 'postgresql+psycopg2://postgres:xSNSFV3a0UN1y3bG@aws-0-region.pooler.supabase.com:6543/postgres'

# Database connection
database = Database(DATABASE_URL)

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
