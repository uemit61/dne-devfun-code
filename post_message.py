import requests

apiUrl = 'https://webexapis.com/v1/messages'
access_token = 'MTNkNzk4MWUtZWE3Zi00YzNhLWE3ZjktYzY3NmRkZjJjMGVhNDNkNWE1N2UtMjYy_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'

httpHeaders = { 'Content-type': 'application/json', 'Authorization': 'Bearer ' + access_token }

body = { 
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZmVlZDYwMDAtOWRmMi0xMWVlLTlkMzEtODllYzFhYzU5ZDRm",
   
    "text": "Hello World 2 ",
    
    "personEmail": "hopes61@icloud.com"}

response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

print( response.status_code )
print( response.text )
