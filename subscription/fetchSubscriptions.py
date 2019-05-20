import requests
import json

def fetch_subscriptions():
  # live environment: https://api.africastalking.com/version1/subscription
  url = "https://api.sandbox.africastalking.com/subscription"

  headers = {
    "apiKey" : "YOUR APIKEY",
    "Content-Type" : "application/x-www-form-urlencoded",
}

  data = {
    "username" : "YOUR USERNAME",
    "shortCode" : "YOUR SHORTCODE",
    "keyword" : "YOUR KEYWORD",
    "lastReceivedId" : "0"
  }

  response = requests.get(url, params = data, headers = headers)

  if response.status_code == 404:
    return "Not Found!"

  return response.json()


if __name__ == "__main__" :
  fetch_subscriptions()