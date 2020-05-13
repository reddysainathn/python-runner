import requests
import json

colId = [1, 2, 3]

url = "https://jsonplaceholder.typicode.com/posts/"

for id in colId:
    try:
        getById = url+str(id)
        r = requests.get(getById)
        if(r.status_code == 200):
            result = r.json()
            print("ID With str converter :  " + str(result["id"]))
            print(f"ID With format :  {result['id']}")
            print("Title :  " + result["title"])
            print("Body :  " + result["body"])
            print("\n")
    except Exception as err:
        print(f'Other error occurred: {err}')
