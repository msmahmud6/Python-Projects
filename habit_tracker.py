import requests
import datetime as dt

def add_pixel(date,quantity):
    endpoint = f"{user_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
    # today_ = date.strftime("%Y%m%d")
    # print(today_)
    parameters = {
        "date": date,
        "quantity": quantity
    }
    response_ = requests.post(url=endpoint, json=parameters, headers=headers)
    print(response_.text)


USER_NAME = "msmahmud69"
TOKEN = "huwshudghyusgfyuguew"
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN" : TOKEN
}

### CREATE USER ACCOUNT ###
user_endpoint = "https://pixe.la/v1/users"
user_parameter = {
    "token" : TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
# response = requests.post(url=user_endpoint, json=user_parameter)
# print(response.text)

### CREATE GRAPH ###
graph_endpoint = f"{user_endpoint}/{USER_NAME}/graphs"
graph_parameter = {
    "id" : GRAPH_ID,
    "name" : "Daily Coding Hours",
    "unit" : "hours",
    "type" : "float",
    "color" : "ajisai"
}
# response = requests.post(url=graph_endpoint,json=graph_parameter, headers=headers)
# print(response.text)

### POSTING A PIXEL ###
date_given = input("Enter date : (yyyymmdd)\n")
total_hours = input("Enter Total Hours : \n")

add_pixel(date_given,total_hours)

