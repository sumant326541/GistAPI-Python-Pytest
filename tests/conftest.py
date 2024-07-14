
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


# constants
@dataclass()
class Config():
    """
       A configuration class to manage all the settings and data required for test execution.
    """
    
    BASE_URL: str = "https://api.github.com/gists"
   
##################

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
def create_gist(payload, headers):
    """
    fixture to create a new gist
    """

    test_config = Config()
    response = requests.post(test_config.BASE_URL, headers=headers, data=json.dumps(payload)) # data=json.dumps(payload) Converts the Python dictionary payload into a JSON formatted string 
    return response 

@pytest.fixture(scope="session")
def test_config():
    """
       fixture to retrive all configuration data
    """

    return Config()