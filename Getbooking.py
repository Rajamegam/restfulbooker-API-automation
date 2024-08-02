import requests
from Utilities.configurations import *
from Utilities.resource import *
id= 953
get_booking_URL = getconfig()['API']['endpoint']+f"/booking/{id}"
print(get_booking_URL)
headers = {"content-Type": "application/json"}
get_booking_response = requests.get(url=get_booking_URL, headers=headers)

if get_booking_response.status_code == 200:
    try:
        get_booking = get_booking_response.json()
        print(get_booking)
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format. Response text:")
        print(get_booking_response.text)

else:
    print(f"Request failed with status code {get_booking_response.status_code}.Response_text:")
    print(get_booking_response.text)
