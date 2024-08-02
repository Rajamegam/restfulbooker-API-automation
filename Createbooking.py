import requests

import payload
from Utilities.configurations import *
from Utilities.resource import *
from payload import *

create_booking_URL = getconfig()['API']['endpoint'] + APIresources.booking
create_booking = requests.post(url=create_booking_URL, json=createbookingpayload(), headers=payload.headers())
create_book_response = create_booking.json()

print(create_book_response)
