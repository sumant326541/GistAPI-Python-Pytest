
"""
utility functions and fixture for test cases
"""
import pytest # type: ignore
import requests
import os
import json
from dotenv import load_dotenv, find_dotenv # type: ignore
from dataclasses import dataclass, field
from typing import Sequence, Mapping
from functools import partial


# constants
@dataclass()
class Config():
    """
       A configuration class to manage all the settings and data required for test execution.
    """
    
    BASE_URL: str = "https://api.github.com/gists"
   
@pytest.fixture(scope="function")
def headers():
    """
       fixture to set authrization token and Content-Type to headers
    """

    # To ensure that the .env file is found and loaded
    dotenv_path = find_dotenv()
    if not dotenv_path:
        print("Error: .env file not found.")
    else:
        load_dotenv(dotenv_path)
        print(f"Loaded .env file from: {dotenv_path}")
 
    return {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {os.getenv('GITHUB_ACCESS_TOKEN')}" 
    }

@pytest.fixture(scope="function")
def payload():
    """
        fixture to craete payload for new gist creation
    """

    payload = {
        "description": "created a new gist",
        "public": False,
        "files": {
            "README.md": {
                "content": "testing gist api"
            }
        }
    }
    return payload


@pytest.fixture(scope="function")
def create_gist(payload, headers, test_config, delete_gist):
    """
    Fixture to create a new gist and delete it after the test function
    """
    gist_id = []
    # SetUp: Create the gist before the test function
    def _create_gist():
        response = requests.post(test_config.BASE_URL, headers=headers, data=json.dumps(payload))
        data = response.json()
        gist_id.append(data["id"])  # Store the gist ID in the list
        print(f"SetUp: Created a new gist...: {gist_id[0]}")
        return response
    
    yield _create_gist

    # Teardown: Delete the gist after the test function
    if gist_id:
        try:
            print(f"TearDown: Deleting newly created gist ID...: {gist_id[0]}")
            delete_gist(gist_id[0])
        except Exception as e:
            print(f"TearDown: Failed to delete newly created gist or gist already deleted in test - gist ID {gist_id[0]}: {e}")


@pytest.fixture(scope="function")
def delete_gist(headers,test_config):
    """
    fixture to delete a gist
    """
    def _delete_gist(gist_id, headers,test_config):
        """
        function to delete a gist
        """

        response = requests.delete(f"{test_config.BASE_URL}/{gist_id}", headers=headers) 
        response.raise_for_status()
        return response 

    delete_gist_partial = partial(_delete_gist, headers=headers,test_config=test_config)
    return delete_gist_partial
    
@pytest.fixture(scope="function")
def retrieve_all_gists(headers,test_config):
    """
    fixture to retrive a gist 
    """

    def _retrieve_all_gists():
        response = requests.get(test_config.BASE_URL, headers=headers) 
        return response 
    return _retrieve_all_gists

@pytest.fixture(scope="function")
def get_gist_by_id(headers,test_config):
    """
    fixture to get a gist by id
    """
    def _get_gist_by_id(gist_id, headers,test_config):
        """
        function to get a gist by id
        """

        response = requests.get(f"{test_config.BASE_URL}/{gist_id}", headers=headers) 
        return response 

    get_gist_by_id = partial(_get_gist_by_id, headers=headers,test_config=test_config)
    return get_gist_by_id


@pytest.fixture(scope="function")
def test_config():
    """
       fixture to retrive all configuration data
    """

    return Config()