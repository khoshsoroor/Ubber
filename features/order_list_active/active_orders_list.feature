Feature: show active orders list for driver


  Scenario Outline: successful search in order list for driver
    Given Driver number is 09999999911
    And Checking the driver login
    When Search active order list for 5 items for <ActiveStatus>
    Then success flag is 1
    And  status is 200

    Examples:
        | ActiveStatus             |
        | waiting_price            |
        | waiting_price_approved   |
        | driver_approved          |
        | registered               |
        | applied_for              |
        | waiting_agreement        |
        | waiting_complete_info    |
        | client_approved          |
        | assigned                 |
        | pickedup                 |
        | delivered                |
        | reject_price             |
        | notfound                 |
        | cancelled                |
        |                          |
