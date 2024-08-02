def createbookingpayload(firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    body = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }

    return body


def updatebookingpayload():
    body1 = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 1112,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    return body1


def authpayload(username, password):
    body = {
        "username": username,
        "password": password
    }

    return body


def headers():
    headers = {
        "content-Type": "application/json"
    }
    return headers
