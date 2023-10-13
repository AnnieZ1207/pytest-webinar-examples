import requests
import config
import data

def create_new_pet():
    return requests.post(config.BASE_URL + config.PET_API_PATH, json=data.PET_BODY)

def create_new_pet_with_body(body):
    return requests.post(config.BASE_URL + config.PET_API_PATH, json=body)

def delete_pet(id):
    return requests.delete(config.BASE_URL + config.PET_API_PATH +"/"+ str(id))
