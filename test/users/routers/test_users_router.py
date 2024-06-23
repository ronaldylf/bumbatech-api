from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared.dependencies import get_db
from shared.database import Base

client = TestClient(app)

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
# database in sqlite just for tests

def prepare_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

test_users = [
    {
        "email": "ronaldylf@gmail.com",
        "senha": "1234",
        "nome": "Ronaldy",
        "idade": 18,
        "genero": 1,
        "estado": "MA",
        "cidade": "sao luis",
        "trilha": 1,
        "conhece_a_cultura": 2,
        "mais_se_interessa": 3
    },
    {
        "email": "joaobalao@gmail.com",
        "senha": "1234",
        "nome": "joao balao",
        "idade": 5,
        "genero": 3,
        "estado": "AB",
        "cidade": "sao jose de ribamar",
        "trilha": 1,
        "conhece_a_cultura": 1,
        "mais_se_interessa": 5
    }
]

def test_deve_criar_usuario():
    prepare_test_db()
    must_be_id = 0
    for user in test_users:
        must_be_id += 1
        response = client.post("users/create-user", json=user)
        returned_user = response.json()
        assert response.status_code == 201
        assert returned_user['id'] == must_be_id


def test__deve_listar_usuarios():
    prepare_test_db()

    test_users_copy = test_users.copy()

    must_be_id = 0
    for index, user in enumerate(test_users):
        must_be_id += 1
        response = client.post("users/create-user", json=user)
        returned_user = response.json()
        test_users_copy[index]['id'] = must_be_id

    response = client.get('/users/')

    assert response.status_code == 200
    assert test_users_copy == test_users
