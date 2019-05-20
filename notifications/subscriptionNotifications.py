# First configure your call back URL in your app  --> https://account.africastalking.com/apps/sandbox/sms/premium/callback

# set up an outgoing webhook to alert our application

from flask import Flask,request, Response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def  subscription_notification():
  phoneNumber = request.form.get('phoneNumber')
  shortCode   = request.form.get('shortCode')
  keyword     = request.form.get('keyword')
  updateType  = request.form.get('updateType')

  print(phoneNumber, shortCode, keyword, updateType)

  return Response(),200

if __name__ == "__main__":
  app.run(debug= True)

    


