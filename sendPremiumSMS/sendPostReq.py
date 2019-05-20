import requests
import json

def send_premiumSMS() : 
  # use "https://api.africastalking.com/version1/messaging" when live
  url = "https://api.sandbox.africastalking.com/version1/messaging"

  #  headers
  headers = {
    "apiKey" : "499ac6dc05804d035efe4dc97f4ba19acd93891d93883c91fb059b96a6db84e0",
    "Content-Type" : "application/x-www-form-urlencoded",
  }
  params = {
    "username" : "sandbox",
    "to" : ["+254715894752"],
    "message" : "testing",
    "from" : "17572",
    "keyword" : "stocks",
    # IF YOU ARE SENDING AN ON DEMAND MESSAGE, SPECIFY A LINK ID
    # "linkId" : "",
    "retryDurationInHours" : 1
  }

  response = requests.post(url, data = params, headers = headers)
  return response.content



