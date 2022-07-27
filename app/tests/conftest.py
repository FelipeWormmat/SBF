import pytest
from fastapi.testclient import TestClient
import factory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.db import get_db
from app.models.models import Base, Product, User
from app.app import app


@pytest.fixture()
def db_session():
    engine = create_engine('sqlite:///./test.db',
                           connect_args={'check_same_thread': False})
    Session = sessionmaker(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield Session()


@pytest.fixture()
def override_get_db(db_session):
    def _override_get_db():
        yield db_session

    return _override_get_db


@pytest.fixture()
def client(override_get_db):
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    return client


@pytest.fixture()
def user_factory(db_session):
    class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = User
            sqlalchemy_session = db_session

        id = None
        display_name = factory.Faker('name')
        email = factory.Faker('email')
        role = None
        password = '$2b$12$rPq8ggNxK5FFJKCdmfcdoeXsL2zr1O9vHGRZI/0zGUSskM2XuZkJu' 

    return UserFactory


@pytest.fixture()
def product_test(db_session):
    class Product_Test(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model: Product
            sqlalchemy_session = db_session

            id = factory.Faker('pyint')
            description =  factory.Faker('name')
            price = factory.Faker('pyfloat')
            technical_details = factory.Faker('name')
            image  = factory.Faker('name')
            visible = True

    return Product_Test