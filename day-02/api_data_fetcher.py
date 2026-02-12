import requests

api_url= "https://fake-json-api.mock.beeceptor.com/users"

response=requests.get(url=api_url)

for url in response.json():
    if url["id"] == 1:
        print("found")
    else:
        print("not found")

print(response.json())

Output:
PS C:\Users\Satish_More\Documents\Josh-pythondevops\python-for-devops\day-02> python .\API.PY
not found
not found
not found
not found
not found
not found
found
not found
not found
not found
