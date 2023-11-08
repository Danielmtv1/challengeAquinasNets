from fastapi import APIRouter, HTTPException, Path
from domain.models.wanted import Wanted
from core.request_fbi import (
    get_wanted_state,
    extract_wanted_data)
from bd.conect_db import SessionLocal
import re

router = APIRouter()


@router.get("/wanted/")
def get_wanted(state):
    result = get_wanted_state(state)
    if result is None:
        raise HTTPException(status_code=404, detail='Not available')
    wanted = result['items']
    items = [extract_wanted_data(item_dict) for item_dict in wanted]
    return items


@router.post("/wanted/")
def post_wanted(state):
    result = get_wanted_state(state)
    if result is None:
        raise HTTPException(status_code=404, detail='Not available')
    wanted = result['items']
    items = [extract_wanted_data(item_dict) for item_dict in wanted]

    with SessionLocal() as db:
        for item in items:
            weight_str = item['weight']
            if weight_str:
                weight_float = float(
                    re.findall(
                        r'\d+\.\d+|\d+',
                        weight_str)[0]
                    ) if re.findall(r'\d+\.\d+|\d+', weight_str) else None
            else:
                weight_float = None
            occupations = (', '.join(item['occupations'])
                           if item['occupations'] else None)
            wanted_item = Wanted(
                name=item['title'],
                sex=item['sex'],
                weight=weight_float,
                reward_text=item['reward_text'],
                description=item['description'],
                images=item['images'],
                place_of_birth=item['place_of_birth'],
                warning_message=item['warning_message'],
                hair=item['hair'],
                eyes=item['eyes'],
                race=item['race'],
                occupation=occupations
            )
            db.add(wanted_item)
        db.commit()
    return items


@router.get("/wanted/{item_id}")
def get_wanted_by_id(item_id: int = Path(..., title="ID database")):
    with SessionLocal() as db:
        wanted_item = db.query(Wanted).filter_by(id=item_id).first()
        if wanted_item is None:
            raise HTTPException(
                status_code=404,
                detail="Elemento no encontrado"
            )
        result = {
            "id": wanted_item.id,
            "name": wanted_item.name,
            "sex": wanted_item.sex,
            "weight": wanted_item.weight,
            "reward_text": wanted_item.reward_text,
            "description": wanted_item.description,
            "images": wanted_item.images,
            "place_of_birth": wanted_item.place_of_birth,
            "warning_message": wanted_item.warning_message,
            "hair": wanted_item.hair,
            "eyes": wanted_item.eyes,
            "race": wanted_item.race,
            "occupation": wanted_item.occupation,
        }
        return result
