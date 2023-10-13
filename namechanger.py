import data

def modify_new_pet_body(name):
    body = data.PET_BODY.copy()
    body["name"] = name

    return body

def modify_pet_body(key,value):

    body = data.PET_BODY.copy()
    body[key] = value

    return body
