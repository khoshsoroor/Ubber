Feature: Signup Check for client



   Scenario: check if a client is valid or not and sign up a new user

    Given Client number for signing up is 09999999900
    When Checking if the mobile number is invalid
     And checking sms
    Then sign up a new user
    And success flag for sign up is 1
    And verification flag for sign up is 1
    And user role is user



  Scenario: check if a client is valid or not and sign up a new user without checking sms

    Given Client number for signing up is 09686634466
    When Checking if the mobile number is invalid
    Then sign up a new user
    And success flag for sign up is 1
    And verification flag for sign up is 0
    And user role is user





  Scenario: check if a client is valid or not and sign up a new baarbari

    Given Client number for signing up is 09000000022
    When Checking if the mobile number is invalid
     And checking sms
    Then sign up a new baarbari
    And success flag for sign up is 1
    And verification flag for sign up is -5
    And user role is baarbari



  Scenario: check if a client is valid or not and sign up a new baarbari without checking sms

    Given Client number for signing up is 09000781622
    When Checking if the mobile number is invalid
    Then sign up a new baarbari
    And success flag for sign up is 1
    And verification flag for sign up is 0
    And user role is baarbari
