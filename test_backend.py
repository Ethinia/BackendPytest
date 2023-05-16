
import requests
import datetime

current_time = datetime.datetime.now()
date = str(f"{current_time.year}-0{current_time.month}-{current_time.day}")

url = "http://localhost:3001/api/wolapp"

def test_getlist():
    r = requests.get(url)
    assert r.status_code == requests.codes.ok

def test_post_liike():
    liike = {
        "liikeID":1,
        "name":"PyTestKyykky",
        "paiva":date,
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
        "paiva":date,
        "weight":50,
        "sarjat":5,
        "toistot":5
    }
    requests.post(url, json=liike)
    r = requests.get(url)
    data = r.json()
    d = requests.delete(url+"/"+(data[-1]['id']))
    assert d.status_code == requests.codes.ok


# test edit. post something then get last items id in DB and use that in the url part and then put/edit that 

def test_edit_liike():
    liike = {
        "liikeID":18,
        "name":"EditMe",
        "paiva":date,
        "weight":50,
        "sarjat":5,
        "toistot":5
    }
    liikeE = {
        "liikeID":18,
        "name":"EditedYou",
        "paiva":date,
        "weight":35,
        "sarjat":5,
        "toistot":5
    }

    requests.post(url, json=liike)
    r = requests.get(url)
    data = r.json()
    d = requests.put(url+"/"+(data[-1]['id']), json=liikeE)
    assert d.status_code == requests.codes.ok

