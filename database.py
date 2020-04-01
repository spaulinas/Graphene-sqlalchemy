from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Department, Employee, Role
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # Create the fixtures
    math = Class(name='Math')
    db_session.add(math)
    biologie = Class(name='Biology')
    db_session.add(biology)

    Student = Role(name='Student')
    db_session.add(manager)
    Teacher = Role(name='Teacher')
    db_session.add(engineer)

    peter = Student(name='Peter', department=biology, role=Student)
    db_session.add(peter)
    roy = Student(name='Roy', department=math, role=Student)
    db_session.add(roy)
    tracy = Teacher(name='Tracy', department=math, role=Teacher)
    db_session.add(tracy)
    db_session.commit()
