Feature:  Create a booking with booking dates

Scenario: To check whether user is able to create a booking

  Given When the create API is hit
  When Execute the API
  Then check for the response whether it is 200 or not and print the details
