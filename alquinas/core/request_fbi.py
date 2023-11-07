import requests
import json


def get_wanted_state(state):

    response = requests.get('https://api.fbi.gov/wanted/v1/list',
                            params={'field_offices': state
                                    }
                            )
    data = json.loads(response.content)
    return data


def extract_wanted_data(item_dict):
    item = {
        'title': item_dict['title'],
        'sex': item_dict['sex'],
        'weight': item_dict['weight'],
        'reward_text': item_dict['reward_text'],
        'description': item_dict['description'],
        'images': item_dict['images'][0]['original'],
        'place_of_birth': item_dict['place_of_birth'],
        'warning_message': item_dict['warning_message'],
        'occupations': item_dict['occupations'],
        'hair': item_dict['hair'],
        'eyes': item_dict['eyes'],
        'race': item_dict['race']
    }
    return item