from pydantic import BaseModel


class WantedItem(BaseModel):
    id: int
    name: str
    sex: str
    weight: float
    reward_text: str
    description: str
    images: str
    place_of_birth: str
    warning_message: str
