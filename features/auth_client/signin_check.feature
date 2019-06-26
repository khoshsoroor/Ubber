Feature: Sign in Check
  Check if mobile number is ....

    Scenario: invalid mobile number
        Given Client number is 09900000074
        When Checking the mobile number
        Then sign up flag is 0


    Scenario: Client mobile number
        Given Client number is 09022012056
        When Checking the mobile number
        Then sign up flag is 1
        And login with username and pass


    Scenario: Correct password for user
        Given Client number is 09022012056
        And Client password is as1234
        When Checking the password for USERToken
        Then verification_flag is 1
        And  user role should be user
        And login with username and pass


    Scenario: Correct password for barbari
        Given Client number is 09000000011
        And Client password is as1234
        When Checking the password for USERToken
        Then verification_flag is 1
        And  user role should be baarbari
        And login with username and pass


    Scenario: Wrong password

        Given Client number is 09022012056
        And Client password is 1234sa
        When Checking the password for USERToken
        Then verification_flag is 0

    Scenario: email user ID
        Given Client ID is saloot@gmail.com
        And Client password is arashmidos
        When Checking the login
        Then verification_flag for email is 1
