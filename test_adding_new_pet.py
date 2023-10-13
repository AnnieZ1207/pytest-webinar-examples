import pytest

import petstore
import namechanger

def test_success_adding_pet():

    new_pet = petstore.create_new_pet()

    assert new_pet.status_code == 200

def test_success_adding_pet_with_custom_name():

    new_pet_body = namechanger.modify_new_pet_body("Bim")
    new_pet = petstore.create_new_pet_with_body(new_pet_body)

    assert new_pet.status_code == 200, \
    f"Expected 201, but actual is {new_pet.status_code}"
    assert new_pet.json()["name"] == "Bim"

@pytest.mark.parametrize("statusvalue",[
    pytest.param(
        "Available", id="Testing status value with string"
    ),
    pytest.param(
        "Недоступно", id="Testing status with russian alphabet"
    ),
    pytest.param(
        "234", id="Testing status value with numbers"
    )
])
def test_success_adding_new_pet_with_custom_status(statusvalue):
    new_pet_body = namechanger.modify_pet_body("status", statusvalue)
    new_pet = petstore.create_new_pet_with_body(new_pet_body)

    assert new_pet.status_code == 200
    assert new_pet.json()["status"] == statusvalue


def test_success_deleting_added_pet():
    added_pet_id = petstore.create_new_pet().json()["id"]
    deleted_pet = petstore.delete_pet(added_pet_id)

    assert deleted_pet.status_code == 200
    assert deleted_pet.json()["message"] == str(added_pet_id)




