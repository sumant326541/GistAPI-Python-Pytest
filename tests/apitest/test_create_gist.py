import pytest

def test_create_new_gist(create_gist,payload):
    """
        test to create a new gest
    """
    # to verify created gist response code is 201
    assert create_gist.status_code == 201

    data = create_gist.json()
    # to verify created gist description 
    assert data['description'] == payload['description']
    # to verify created gist content 
    assert data['files']['README.md']['content'] == payload['files']['README.md']['content']