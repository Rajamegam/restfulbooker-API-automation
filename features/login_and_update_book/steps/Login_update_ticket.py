from behave import *
from Utilities.configurations import *
from features import payload
import requests


@Given('The username and password of the user')
def stepimpl(context):

    context.auth_endpoint = getconfig()['API']['endpoint'] + "/auth"
    # following for loop is to get the username and password from the "login.feature" file
    for row in context.table:
        context.username = row['username']
        context.password = row['password']


@when('We execute login API')
def step_impl(context):

    context.auth_response = requests.post(url=context.auth_endpoint, json=payload.authpayload(context.username,context.password),
                                          headers=payload.headers())


@Then('logged in successfully')
def step_impl(context):
    auth_response_json = context.auth_response.json()
    assert context.auth_response.status_code == 200
    print(auth_response_json)
    context.token_value = auth_response_json['token']
    context.config.userdata['token_value'] = context.token_value


@Given('Authenticate the user')
def step_impl(context):
    token_value = context.config.userdata.get('token_value', None)
    #id = 953
    context.update_booking_URL = getconfig()['API']['endpoint'] + f"/booking/{id}"
    context.headers = {"Content-Type": "application/json", "cookie": f"token={token_value}"}
    print(context.headers)


@When('Execute the update API')
def step_impl(context):
    context.update_booking = requests.put(url=context.update_booking_URL, json=payload.updatebookingpayload(),
                                          headers=context.headers)


@Then('Update completed successfully')
def step_impl(context):
    if context.update_booking.status_code == 200:
        try:
            update_booking_response = context.update_booking.json()
            print(update_booking_response)
        except requests.exceptions.JSONDecodeError:
            print("Response is not in JSON format. Response text:")
            print(context.update_booking.text)
    else:
        print(f"Request failed with status code {context.update_booking.status_code}. Response text:")
        print(context.update_booking.text)
