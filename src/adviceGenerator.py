"""NOTE: Code is highly based on factGenerator.py"""
import requests

ADVICE_URL = "	https://api.adviceslip.com/advice"
USEDLOG_PATH = "./localData/usedAdvice.log"

f = open(USEDLOG_PATH, "r")
usedID = f.read()
f.close()


def getAdvice():
    try:
        r = requests.get(ADVICE_URL)
        if r.status_code != 200:
            raise Exception(f"Code: {r.status_code}")
        
        response = r.json()
        if str(response["slip"]["id"]) in usedID:
            content = getAdvice()
        else:
            content = response["slip"]["advice"]
            addID(str(response["slip"]["id"]))
        return content
    except Exception as e:
        raise Exception(f"Unable to get fun fact. \nErrors:\n{str(e)}")

def addID(adviceID):
    f = open(USEDLOG_PATH, "w")
    f.write(f"{usedID}{adviceID}\n")
    f.close()