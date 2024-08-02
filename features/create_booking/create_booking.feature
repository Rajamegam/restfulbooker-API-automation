Feature:  Create a booking with booking dates

  Scenario: To check whether user is able to create a booking

    Given When the create API is hit with payload
      | firstname | lastname | totalprice | depositpaid | checkin    | checkout   | additionalneeds|
      | jim       | brown    | 111        | true        | 2018-01-01 | 2019-01-01 | breakfast      |
    When Execute the API
    Then check for the response whether it is 200 or not and print the details
