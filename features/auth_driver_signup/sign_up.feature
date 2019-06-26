Feature: Signup Check for driver



   Scenario: check if a driver is valid or not and sign up a new driver

    Given driver number for signing up is 09999999913
    When Checking if the driver mobile number is invalid
     And check sms for driver
    Then sign up driver
    And success flag for driver sign up is 1

