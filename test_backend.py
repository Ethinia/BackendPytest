
import requests

url = "http://localhost:3001/api/wolapp"

def test_getlist():
    r = requests.get(url)
    responseA = '<Response [200]>'
    assert str(r) == responseA


def test_post_liike():
    expected_response = "<Response [201]>"
    liike = {
        "liikeID":1,
        "name":"Jalkapainot",
        "date":"7.11.2022",
        "weight":115,
        "sarjat":5,
        "toistot":5
    }
    r = requests.post(url, json=liike)
    assert str(r) == expected_response

# test delete
# test edit