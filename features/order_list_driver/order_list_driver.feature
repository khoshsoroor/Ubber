# Created by rezaei at 4/21/18
Feature: order list of driver

  Scenario Outline: successful search in order list for driver
    Given Driver number is 09999999911
    And Checking the driver login
    When Search for driver order list for 5 items for <DriverStatus>
    Then success flag is 1
    And  status is 200

    Examples:
        | DriverStatus   |
        | ongoing        |
        | past_orders    |

    Scenario Outline: unsuccessful search of words in order list for driver
    Given Driver number is 09999999911
    And Checking the driver login
    When Search for driver order list for ab items for <Status>
    Then success flag is 0
    And  status is 400

    Examples:
        | Status         |
        | ongoing        |
        | past_orders    |






