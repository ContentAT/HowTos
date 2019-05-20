import requests
import json

def send_premiumSMS() : 
  # use "https://api.africastalking.com/version1/messaging" when live
  url = "https://api.sandbox.africastalking.com/version1/messaging"

  #  headers
  headers = {
    "apiKey" : "YOUR API_KEY",
    "Content-Type" : "application/x-www-form-urlencoded",
  }
  params = {
    "username" : "YOUR_USERNAME",
    "to" : ["+2547XXXXXXXX","+2547XXXXXXXX"],
    "message" : "MESSAGE GOES HERE",
    "from" : "YOUR SHORT CODE",
    "keyword" : "(OPTIONAL) YOUR KEYWORD",
    # IF YOU ARE SENDING AN ON DEMAND MESSAGE, SPECIFY A LINK ID
    # "linkId" : "",
    "retryDurationInHours" : 1 
  }

  response = requests.post(url, data = params, headers = headers)
  return response.content

if __name__ == "__main__" :
  send_premiumSMS()


