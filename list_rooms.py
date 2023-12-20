import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = "MTNkNzk4MWUtZWE3Zi00YzNhLWE3ZjktYzY3NmRkZjJjMGVhNDNkNWE1N2UtMjYy_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de"

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
queryParams = { 'sortBy': 'lastactivity', 'max': '2' }

response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )

print( response.status_code )
print( response.text )

# This is a Request and not a Response :)
