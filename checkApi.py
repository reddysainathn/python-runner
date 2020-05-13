import requests
import json

allIds = [1, 2, 3]

url = "https://jsonplaceholder.typicode.com/posts/"


def getById(colId):
    for id in colId:
        try:
            getById = url+str(id)
            r = requests.get(getById)
            if(r.status_code == 200):
                result = r.json()
                printValues(result)
        except Exception as err:
            print(f'Other error occurred: {err}')


def getAllValues():
    try:
        r = requests.get(url)
        if(r.status_code == 200):
            result = r.json()
            for res in result:
                printValues(res)
    except Exception as err:
        print(f'Other error occurred: {err}')


def printValues(result):
    print("ID With str converter :  " + str(result["id"]))
    print(f"ID With format :  {result['id']}")
    print("Title :  " + result["title"])
    print("Body :  " + result["body"])
    print("\n")

# getAllValues()
# getById(allIds)
