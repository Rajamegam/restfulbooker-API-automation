import requests
from Utilities.configurations import *
from Utilities.resource import *
from payload import *
id=953
update_booking_URL = getconfig()['API']['endpoint'] +f"/booking/{id}"


headers = {"Content-Type": "application/json", "cookie": "token=ea1aa0dae9d99ce"}

update_booking = requests.put(url=update_booking_URL, json=updatebookingpayload(), headers=headers)

if update_booking.status_code == 200:
    try:
        update_booking_response = update_booking.json()
        print(update_booking_response)
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format. Response text:")
        print(update_booking.text)
else:
    print(f"Request failed with status code {update_booking.status_code}. Response text:")
    print(update_booking.text)
