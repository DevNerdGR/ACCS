import requests

FUNFACT_URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"
USEDLOG_PATH = "./localData/used.log"

f = open(USEDLOG_PATH, "r")
usedID = f.read()
f.close()


def getFunfact():
    try:
        r = requests.get(FUNFACT_URL + "?language=en")
        if r.status_code != 200:
            raise Exception(f"Code: {r.status_code}")
        
        response = r.json()
        if response["id"] in usedID:
            content = getFunfact()
        else:
            content = response["text"]
            addID(response["id"])
        return content
    except Exception as e:
        raise Exception(f"Unable to get fun fact. \nErrors:\n{str(e)}")

def addID(factID):
    f = open(USEDLOG_PATH, "w")
    f.write(f"{usedID}{factID}\n")
    f.close()