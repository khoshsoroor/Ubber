Feature: Sign in Check
  Check if mobile number is ....


    Scenario: Driver mobile number
        Given Driver number is 09999999911
        When Checking the driver login with sms code 53671
        Then success flag is 1


    Scenario: Wrong driver mobile number
        Given Driver number is 09999999911
        When Checking the driver login with sms code 52000
        Then success flag is 0