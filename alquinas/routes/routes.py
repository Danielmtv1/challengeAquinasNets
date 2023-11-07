from fastapi import APIRouter, HTTPException
from domain.schemas.wanted import WantedItem
from bd.conect_db import get_mysql_connection
from core.request_fbi import  get_wanted_state, extract_wanted_data

router = APIRouter()

@router.get("/wanted/")
def get_wanted(state):
    result = get_wanted_state(state)
    if result is None:
        raise HTTPException(status_code=404, detail='Not available')
    wanted = result['items']
    items = [extract_wanted_data(item_dict) for item_dict in wanted]
    return items
