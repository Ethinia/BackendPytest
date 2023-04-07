
import requests

url = "http://localhost:3001/api/wolapp"

def test_getlist():
    r = requests.get(url)
    assert r.status_code == requests.codes.ok

def test_post_liike():
    liike = {
        "liikeID":1,
        "name":"Kasipainot",
        "date":"7.11.2022",
        "weight":35,
        "sarjat":5,
        "toistot":5
    }
    r = requests.post(url, json=liike)
    assert r.status_code == requests.codes.created

# post something into database then get the DB id for that item (last item in DB) and input that id into the delete url.
def test_delete_liike():
    liike = {
        "liikeID":15,
        "name":"Destroythis",
        "date":"7.11.2022",
        "weight":50,
        "sarjat":5,
        "toistot":5
    }
    requests.post(url, json=liike)
    r = requests.get(url)
    data = r.json()
    d = requests.delete(url+"/"+(data[-1]['id']))
    assert d.status_code == requests.codes.ok


# test edit

