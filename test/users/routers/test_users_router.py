from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test__deve_listar_usuarios():
    response = client.get('/users/list-users')

    assert response.status_code == 200

    assert response.json() == [
        {
            'id': 1,
            'nome': "ronaldy",
            'idade': 18,
            'genero': 0,
            'estado': "MA",
            'cidade': "sao luis",
            'trilha': 1,
            'conhece_a_cultura': 2,
            'mais_se_interessa': 3
        },
        {
            'id':1,
            'nome':"aline",
            'idade':18,
            'genero':1,
            'estado':"SP",
            'cidade':"sao jose dos campos",
            'trilha':3,
            'conhece_a_cultura':4,
            'mais_se_interessa':5
        },
        {
            'id':1,
            'nome':"joao",
            'idade':23,
            'genero':0,
            'estado':"RN",
            'cidade':"natal",
            'trilha':1,
            'conhece_a_cultura':3,
            'mais_se_interessa':7
        },
    ]

def test_deve_criar_novo_usuario():
    novo_usuario = {
        'nome':"sóstenes",
        'idade':999,
        'genero':0,
        'estado':"maranhao",
        'cidade':"alemanha",
        'trilha':1,
        'conhece_a_cultura':2,
        'mais_se_interessa':3
    }

    novo_usuario_copy = novo_usuario.copy()
    novo_usuario_copy['id'] = 1

    response = client.post('/users/create-user', json=novo_usuario)

    assert response.status_code == 201
    assert response.json()==novo_usuario_copy