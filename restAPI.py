"""
The object is to gather horizon server list of desktop pools info.
https method as such "get,post,put" applied.
Used python3

Source: https://developer.vmware.com/api

Steps:
1) Get token, https methods: POST
2) Refresh token if experies, https method: POST
3) Get a list of desktop pools, https methods: GET
"""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

api_url = "https://jsonplaceholder.typicode.com/todos/1"
api_url2 = "https://jsonplaceholder.typicode.com/todos"
post_api="https://conn2.gsslabs.org/rest/"
session=requests.Session()
post_api="https://conn2.gsslabs.org/"
# session=requests.Session()
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)
#
# x=session.get(post_api)


payload={
    "domain":"gsslabs.org",
"username":"administrator",
"password":"VMware123!"
}
payload2={
    "domain":"gsslabs.org",
"username":"administrator",
"password":"VMware123!"
}

#x=input("Enter URl name :\n")
y=input("Enter http method : \n ")
httpsMethod=["get","post","put","patch","delete"]
todo = {"userId": 1, "title": "Buy milk", "completed": False}
putTodo = {"userId": 1, "title": "Wash car", "completed": True}
patchTodo = {"title": "Mow lawn"}
for i in range(len(httpsMethod)):
    if httpsMethod[i] in y.lower() :
        if  httpsMethod[i] == "get":
            response=requests.get(api_url)
            print(response.json())
            print(response.status_code)
        elif  httpsMethod[i] == "post":
            response = requests.post(post_api,verify=False, json=payload)
            print(response.json())
            print(response.status_code)
        elif httpsMethod[i] == "put":
            response = requests.put(api_url, json=putTodo)
            print(response.json())
            print(response.status_code)
        elif httpsMethod[i] == "patch":
            response = requests.patch(api_url, json=patchTodo)
            print(response.json())
            print(response.status_code)
        elif httpsMethod[i] == "delete":

            response = requests.delete(api_url)
            print(response.json())
            print(response.status_code)
        else:
            break


