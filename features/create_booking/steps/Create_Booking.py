import requests
from Utilities.configurations import *
from features import payload
from behave import *


@Given('When the create API is hit with payload')
def stepimp(context):
    context.create_endpoint = getconfig()['API']['endpoint'] + "/booking"

    for row in context.table:
        context.firstname = row['firstname']
        context.lastname = row['lastname']
        context.totalprice = row['totalprice']
        context.depositpaid = row['depositpaid']
        context.checkin = row['checkin']
        context.checkout = row['checkout']
        context.additionalneeds = row['additionalneeds']


@when('Execute the API')
def stepimp(context):
    context.response_json = requests.post(url=context.create_endpoint,
                                          json=payload.createbookingpayload(context.firstname, context.lastname,
                                                                            context.totalprice,
                                                                            context.depositpaid, context.checkin,
                                                                            context.checkout,
                                                                            context.additionalneeds),
                                          headers=payload.headers())


@then('check for the response whether it is 200 or not and print the details')
def stepimp(context):
    context.create_response = context.response_json.json()
    assert context.response_json.status_code == 200
    print(context.create_response)


@then('check if the 400(bad request) is showing if the user does not send the value for totalprice key')
def stepimp(context):
    context.response = requests.post(url=context.create_endpoint,
                                     json=payload.createbookingpayload(context.firstname, context.lastname, None,
                                                                       context.depositpaid, context.checkin,
                                                                       context.checkout,
                                                                       context.additionalneeds),
                                     headers=payload.headers())

    assert context.response.status_code == 200
    print(context.response)
