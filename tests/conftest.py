
"""
utility functions and fixture for test cases
"""
import pytest
import requests
import os
import json
from dotenv import load_dotenv, find_dotenv
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
   
@pytest.fixture(scope="session")
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

@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def create_gist(payload, headers,test_config,delete_gist):
    """
    fixture to create a new gist
    """    
    def _create_gist():
        response = requests.post(test_config.BASE_URL, headers=headers, data=json.dumps(payload)) # data=json.dumps(payload) Converts the Python dictionary payload into a JSON formatted string 
        # data = response.json()
        # created_gist_id = data["id"]
    
        return response
    
    return _create_gist

    # print(f"deleted newly created gistid: {created_gist_id}")
    
    # #Teardown: Delete the gist after the test
    # try:
    #     print(f"deleted newly created gistid: {created_gist_id}")
    #     delete_gist(created_gist_id)
    #     print(f"deleted newly created gistid: {created_gist_id}")
    # except Exception as e:
    #     # Handle the exception if gist already deleted
    #     print(f"gist already deleted of id {created_gist_id}: {e}")


@pytest.fixture(scope="session")
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
    
@pytest.fixture(scope="session")
def retrieve_all_gists(headers,test_config):
    """
    fixture to retrive a gist 
    """

    def _retrieve_all_gists():
        response = requests.get(test_config.BASE_URL, headers=headers) 
        return response 
    return _retrieve_all_gists

@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
def test_config():
    """
       fixture to retrive all configuration data
    """

    return Config()