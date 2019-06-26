Feature: Sign in Check
  Check if mobile number is ....


    Scenario: Admin login
        Given Admin logs in with email test@gmail.com and password is ATpl124SC
        When Checking the admin login
        Then verification flag for admin is 1


        Scenario: wrong password for admin login
        Given Admin logs in with email test@gmail.com and password is as1234
        When Checking the admin login
        Then verification flag for admin is 0
