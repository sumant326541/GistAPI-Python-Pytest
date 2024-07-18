import pytest

def test_retrive_all_gist(retrieve_all_gists,create_gist, delete_gist):
    """
        test to retrive all available gist
    """
    response = create_gist()
    # to verify retrive gist response code is 200
    all_gist_response = retrieve_all_gists()
    assert all_gist_response.status_code == 200
    delete_gist(response.json()['id'])



def test_get_gist_by_id(get_gist_by_id,create_gist,delete_gist):
    """
        test to get gist by id
    """
   # to verify created gist response code is 201
    created_gist_response = create_gist()
    assert created_gist_response.status_code == 201

    created_gist_data = created_gist_response.json()
   
    # get created gist id 
    gist_id = created_gist_data['id']
    print(f"welcome {gist_id}")

    # to verify created gist by id
    get_gist_response_by_id = get_gist_by_id(gist_id=gist_id)
    # print(f"welcome 2 id {get_gist_response_by_id.json()}")
    assert get_gist_response_by_id.status_code == 200
    delete_gist(gist_id)