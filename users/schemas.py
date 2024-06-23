from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    id: int
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

class UserRequest(BaseModel):
    email: str # email para login
    senha: str # senha para login
    nome: str # nome
    idade: int # idade
    genero: int = Field(ge=0, le=3) # numero entre 0 e 3 (Masculino, Feminino, Nao Binario, Outro) 
    estado: str = Field(max_length=2) # abreviatura (ex: MA, SP, BA)
    cidade: str
    trilha: int = Field(ge=0, le=5) #numero entre 0 e 5 (NAO, Back, Front, Dados, Design, Jogos)
    conhece_a_cultura: int = Field(ge=0, le=2) # numero entre 0 e 2 (bom, basico, NAO)
    mais_se_interessa: int = Field(ge=0, le=7) # numero entre 0 e 7 (Bumba meu boi, Cacuriá, Tambor de crioula, Reggae maranhense,Artesanato, Culinária, Literatura, História)