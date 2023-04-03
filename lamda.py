import requests
def lambda_handler(event, context):
  url="https://ij92qpvpma.execute-api.eu-west-1.amazonaws.com/candidate-email_serverless_lambda_stage/data"
  response = requests.post(url)
  