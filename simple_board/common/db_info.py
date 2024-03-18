from sqlmodel import Session, SQLModel, create_engine

engine = create_engine("sqlite:///C:/sqlite3/db/simpleboard.db")
SQLModel.metadata.create_all(engine)


def get_db():
    with Session(engine) as session:
        yield session
