import requests
from Build_JSON_Data import JSON_Data

class Requester:
    server = "http://localhost"
    port = 5000
    endpoint = "heartbeat"
    url = f"{server}:{port}/{endpoint}"

    def __init__(self, url = url):
        self.url = url
    
    def Post_Heartbeat(self):
        data = JSON_Data()
        payload = data.build_data()
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
    
        response = requests.request("POST", self.url, headers=headers, data=payload)
    
        print(response.text)

    def Patch_Heartbeat(self):
        data = JSON_Data()
        payload = data.build_data()
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }
    
        response = requests.request("PATCH", self.url, headers=headers, data=payload)
    
        print(response.text)

    def Get_Heartbeat(self):

        payload={}
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        }

        response = requests.request("GET", self.url, headers=headers, data=payload)

        print(response.text)
