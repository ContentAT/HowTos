import requests
import json

  # generate a checkout token
def get_checkout_token():
  # for live environment("https://api.africastalking.com/checkout/token/create")
  url = "https://api.sandbox.africastalking.com/checkout/token/create"

  header = {
    "Content-Type" : "application/x-www-form-urlencoded",
  }

  param = {
    "phoneNumber" : "phoneNumber your want to create subscription for"
  }

  # *** This is an open endpoint(No need to provide your authentication credentials)

  # send post request
  response = requests.post(url, data = param, headers = header)
  #  grab checkout_token
  checkout_token = json.loads(response.text)['token']
  return checkout_token


# make the subscription request
def create_subscription():
  # live environment: https://api.africastalking.com/version1/subscription/create
  url = " https://api.sandbox.africastalking.com/version1/subscription/create"

  headers = {
    "apiKey" : "",
    "Content-Type" : "application/x-www-form-urlencoded",
}

  params = {
    "username" : "YOUR USERNAME",
    "shortCode" : "YOUR SHORT CODE",
    "keyword" : "YOUR KEYWORD",
    "phoneNumber" : "The phoneNumber to be subscribed",
    "checkoutToken" : get_checkout_token()
  }

  response = requests.post(url, data = params, headers = headers)

  return response.content


if __name__ == "__main__" :
  create_subscription()