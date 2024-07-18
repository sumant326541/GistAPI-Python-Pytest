import pytest

def test_delete_all_gist(retrieve_all_gists,delete_gist,create_gist):
    """
        test to delete all available gist
    """
    
    # to verify created gist response code is 201
    created_gist_response = create_gist()
    assert created_gist_response.status_code == 201

    # retrive all gist
    all_gist_response = retrieve_all_gists()
    assert all_gist_response.status_code == 200

    # iterate all gist and delete by id
    all_gists = all_gist_response.json()
    for gist in all_gists:
        gist_id = gist['id']
        print(f"Deleting gist with ID...: {gist_id}")
        delete_gist(gist_id=gist_id)
        
    
    # # Verify that all gists are deleted
    all_gists_post_delete = retrieve_all_gists().json()
    assert len(all_gists_post_delete) == 0
    
