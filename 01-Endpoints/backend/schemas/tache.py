from pydantic import BaseModel, Field
from enum import Enum

class Statut(str, Enum):
    A_FAIRE = "à faire"
    EN_COURS = "en cours"
    TERMINEE = "terminée"

class Tache(BaseModel):
    titre: str = Field(min_length=1)
    description: str = Field(min_length=1)
    statut: Statut