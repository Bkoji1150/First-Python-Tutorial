import requests 
import config
from pprint import pprint
url = "https://api.yelp.com/v3/businesses/search"
headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Barber",
    "location": "MD"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
# [item for item in items] list compression
result = [business['location'] for business in businesses if business['location']['city']=='Baltimore']
address_display = [address['display_address'] for address in result]
pprint(address_display)