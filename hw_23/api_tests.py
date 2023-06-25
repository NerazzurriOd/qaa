import requests
import pytest

product_headers = {
    "content-type": "application/json"
}


@pytest.mark.parametrize('endpoint', ['/objects/7'])
def test_get_request(endpoint):
    url = f'https://api.restful-api.dev{endpoint}'
    response = requests.get(url)
    print(response.json())
    assert response.status_code == 200, 'Invalid status code'
    assert 'name' in response.json(), 'Response body does not contain "name" key'


@pytest.mark.parametrize('endpoint', ['/objects'])
def test_post_request(endpoint):
    url = f'https://api.restful-api.dev{endpoint}'
    data = {
        'name': 'Apple MacBook Pro 16',
        'data': {
            'year': 2019,
            'price': 1849.99,
            'CPU model': 'Intel Core i9',
            'Hard disk size': '1 TB'
        }
    }
    response = requests.post(url, json=data)
    print(response.json())
    assert response.status_code == 200, 'Invalid status code'
    assert response.json()['name'] == 'Apple MacBook Pro 16', 'Name in response body does not match'


@pytest.mark.parametrize('endpoint', ['/objects/ff80818188e67add0188f41f18aa0829'])
def test_put_request(endpoint):
    url = f'https://api.restful-api.dev{endpoint}'
    data = {
        'name': 'Apple MacBook Pro 16',
        'data': {
            'year': 2019,
            'price': 2049.99,
            'CPU model': 'Intel Core i9',
            'Hard disk size': '2 TB',
            'color': 'silver'
        }
    }
    response = requests.put(url, json=data)
    assert response.status_code == 200, 'Invalid status code'
    # assert response.json()['price'] == 2049.99, 'Price in response body does not match'


@pytest.mark.parametrize('endpoint', ['/objects/ff80818188e67add0188f41f18aa0829'])
def test_patch_request(endpoint):
    url = f'https://api.restful-api.dev{endpoint}'
    data = {'name': 'Apple MacBook Pro 17'}
    response = requests.patch(url, json=data)
    assert response.status_code == 200, 'Invalid status code'
    assert response.json()['name'] == 'Apple MacBook Pro 17', 'Name in response body does not match'


@pytest.mark.parametrize('endpoint', ['/objects/ff80818188e67add0188f41f18aa0829'])
def test_delete_request(endpoint):
    url = f'https://api.restful-api.dev{endpoint}'
    response = requests.delete(url)
    assert response.status_code == 200, 'Invalid status code'
    # assert response.content == {
    #     "message": "Object with id = ff80818188e67add0188f41f18aa0829, has been deleted."
    #     }, 'Message is not correct'
