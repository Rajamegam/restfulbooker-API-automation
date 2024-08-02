Feature:  Login into the system and update the user details

  Scenario: Verify if the login is successfully completed

    Given The username and password of the user
    When We execute login API
    Then logged in successfully


Scenario: Verify if only the valid user is able to update the created booking

  Given Authenticate the user
  When Execute the update API
  Then Update completed successfully

