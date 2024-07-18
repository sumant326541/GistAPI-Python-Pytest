import pytest

def test_create_new_gist(create_gist,payload, delete_gist):
    """
        test to create a new gest
    """

    # to verify created gist response code is 201
    created_gist_response = create_gist()
    assert created_gist_response.status_code == 201

    created_gist_data = created_gist_response.json()
    # to verify created gist description 
    assert created_gist_data['description'] == payload['description']
    # to verify created gist content 
    print(f"created GIST ID = {created_gist_data['id']}")
    assert created_gist_data['files']['README.md']['content'] == payload['files']['README.md']['content']
    delete_gist(created_gist_data['id'])