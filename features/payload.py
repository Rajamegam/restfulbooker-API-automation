def createbookingpayload():
    body = {
        "firstname": "Rajamegam",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": ""
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


def authpayload():
    body = {
        "username": "admin",
        "password": "password123"
    }

    return body

def headers():
    headers={
        "content-Type": "application/json"
    }
    return headers