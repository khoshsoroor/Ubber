Feature: show active orders list for admin


#  Scenario Outline: successful search in order list for admin
#    Given Admin logs in with email test@gmail.com and password is ATpl124SC
#    And Checking the admin login
#    When Search order list of admin for <ActiveStatus>
#    And  status is 200
#
#    Examples:
#        | ActiveStatus             |
#        | waiting_price            |
#        | waiting_price_approved   |
#        | driver_approved          |
#        | registered               |
#        | applied_for              |
#        | waiting_agreement        |
#        | waiting_complete_info    |
#        | client_approved          |
#        | assigned                 |
#        | pickedup                 |
#        | delivered                |
#        | reject_price             |
#        | notfound                 |
#        | cancelled                |
#        |                          |
#
#
#
#

  Scenario Outline: successful search in order list for admin
    Given Admin logs in with email test@gmail.com and password is ATpl124SC
    And Checking the admin login
    When Search order list of admin for status

        | status                   |
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
    And  status is 200

