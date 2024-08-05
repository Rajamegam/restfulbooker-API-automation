import requests
from Utilities.configurations import *
from features import payload
from behave import *


@Given('a booking ID is retrieved from the create API and passed in the URL')
def stepimp(context):
    #booking_id=context.config.userdata.get('booking_id',None)
    context.booking_id = context.config.userdata['booking_id']
    context.get_booking_details = getconfig()['API']['endpoint'] + f"/booking/{context.booking_id}"
    print(context.get_booking_details)



@When('the booking details API is executed with the retrieved booking ID')
def stepimp(context):
    context.booking_details_response = requests.get(url=context.get_booking_details, headers=payload.headers())
    print(context.booking_details_response)

@Then('the response code should be 200')
def stepimp(context):
    assert context.booking_details_response.status_code ==200