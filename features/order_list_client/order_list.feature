# Created by pc at 4/15/2018
Feature: order list of clients




  Scenario Outline: successful search in order list for client
    Given login with username 09022012056 and password as1234
    When Search for order list for 5 items for <Status>
    Then success flag is 1
    And  status is 200

    Examples:
        | Status|
        | ongoing|
        | past_orders|



    Scenario Outline: successful search in order list for barbari
    Given login with username 09000000011 and password as1234
    When Search for order list for 5 items for <Status>
    Then success flag is 1
    And  status is 200

    Examples:
        | Status             |
        | ongoing            |
        | past_orders        |


    Scenario Outline: unsuccessful search of words in order list for client
    Given login with username 09022012056 and password as1234
    When Search for order list for abs items for <Status>
    Then success flag is 0
    And  status is 400

    Examples:
        | Status             |
        | ongoing            |
        | past_orders        |


    Scenario Outline: unsuccessful search of words in order list for barbari
    Given login with username 09000000011 and password as1234
    When Search for order list for abs items for <Status>
    Then success flag is 0
    And  status is 400

    Examples:
        | Status             |
        | ongoing            |
        | past_orders        |
