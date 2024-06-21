from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from shared.dependencies import get_db
from users.models.user_model import User

router = APIRouter(prefix="/users")

class UserResponse(BaseModel):
    id: int
    email: str
    senha: str
    nome: str
    idade: int
    genero: int # numero entre 0 e 3 (Masculino, Feminino, Nao Binario, Outro)
    estado: str # abreviatura (ex: MA, SP, BA)
    cidade: str
    trilha: int #numero entre 0 e 5 (NAO, Back, Front, Dados, Design, Jogos)
    conhece_a_cultura: int # numero entre 0 e 2 (bom, basico, NAO)
    mais_se_interessa: int # numero entre 0 e 7 (Bumba meu boi, Cacuriá, Tambor de crioula, Reggae maranhense,Artesanato, Culinária, Literatura, História)

class UserRequest(BaseModel):
    email: str
    senha: str
    nome: str
    idade: int
    genero: int
    estado: str
    cidade: str
    trilha: int
    conhece_a_cultura: int
    mais_se_interessa: int


@router.post("/create-user", response_model=UserResponse, status_code=201)
def criar_usuario(new_user_request: UserRequest,
                  db: Session = Depends(get_db)) -> UserResponse:

    new_user = User(
        **new_user_request.model_dump()
    )
    #new_user.senha = criptografar(new_user.senha) #não esquecer

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        **new_user.__dict__
    )

@router.get("/list-users", response_model=List[UserResponse])
def listar_usuarios(db: Session = Depends(get_db)) -> List[UserResponse]:
    return db.query(User).all()