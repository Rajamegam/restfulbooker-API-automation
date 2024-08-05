Feature: Get the booking details with ID

  Scenario: Pass the booking ID of the newly created booking and get the details
    Given a booking ID is retrieved from the create API and passed in the URL
    When the booking details API is executed with the retrieved booking ID
    Then the response code should be 200