import requests

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'MTNkNzk4MWUtZWE3Zi00YzNhLWE3ZjktYzY3NmRkZjJjMGVhNDNkNWE1N2UtMjYy_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'

httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 'toPersonEmail': 'tofrench@webex.bot', 'text': 'Hello' }

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )
