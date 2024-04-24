import os
import pytest
from your_app import app, read_count, save_count

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # Send a GET request to the home page
    response = client.get('/')
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response data contains the expected content
    assert b'Hello World! 1' in response.data

def test_count_increment(client):
    # Get the initial count
    initial_count = read_count()
    # Send multiple GET requests to the home page
    client.get('/')
    client.get('/')
    # Get the count after requests
    updated_count = read_count()
    # Assert that the count has incremented correctly
    assert updated_count == initial_count + 2


  
