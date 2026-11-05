import json
import urllib
from http.client import HTTPResponse
from optparse import Option
from urllib.request import Request

import requests

url = 'https://demoqa.com/BookStore/v1/Books'
# Request
with urllib.request.urlopen(url) as response:
    assert response.status == 200
    resp_data = json.loads(response.read())
    assert 'books' in resp_data
    books = resp_data.get('books')
    assert len(books) > 0
    assert len(books) == 8
    for book in books:
        assert 'title' in book
    # for k, v in resp_data.items():
    #     print(f'key= {k}, value={v}')
    print(resp_data)
    print(response.status)

request = Request(url, method='OPTIONS')

with urllib.request.urlopen(request) as response:
    print(response.read())


url = 'https://demoqa.com/books'
resp = requests.options(url)
print(resp.status_code)
print(resp.text)

