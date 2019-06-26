Feature: apply for ride



#   Scenario: apply an old driver to an order by admin

#
#    Given login with username 09022012056 and password as1234
#     And an order is added by following options for applying driver
#        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address     | destination_address        | receiver_mobile_phone |
#        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        |                    | خیابان دوم کوچه سوم پلاک 8  |                       |
#
#     And call for order detail
#     When a driver is assigned to order with number 09666996999
##     Then status should be waiting_agreement
##     Then turn the status back to cancelled
##




   Scenario: apply a new driver to an order by admin


    Given login with username 09022012056 and password as1234
     And an order is added by following options for applying driver
        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address           | destination_address         | receiver_mobile_phone  |
        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک  | خیابان دوم کوچه سوم پلاک 8   |                        |

    And call for order detail
    When A new driver is sign up with number 09999999915
    And a driver is assigned to order with number 09999999915
#    Then status should be applied_for
    Then turn the status back to cancelled
    And the driver is deleted



