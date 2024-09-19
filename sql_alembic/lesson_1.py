from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker


url = URL.create(
    drivername="postgresql+psycopg2",
    username="testuser",
    password="testpassword",
    host="localhost",
    database="testuser",
    port=5433,
)

engine = create_engine(
    url=url,
    echo=True
)

session_pool = sessionmaker(engine)

# session = session_pool()


with session_pool() as session:
    session.execute(text('SELECT 1'))
    # session.commit()

