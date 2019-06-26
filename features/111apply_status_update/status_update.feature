Feature: status update


#
#   Scenario: driver_approved and waiting_price :
#
#
#     Given sign up a new client user with 09999999900
#     When an order is added by following options for applying driver
#        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address             | destination_address        | receiver_mobile_phone |
#        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک 8  | خیابان دوم کوچه سوم پلاک 8  |                       |
#        | 2.5     | 0        |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک 8  | خیابان دوم کوچه سوم پلاک 8  |                       |
#
#     Then the status after add order should be:
#     | status            |
#     | driver_approved   |
#     | waiting_price     |
#
#     And turn the status back to cancelled
#     And delete the number of new client
#
#
#
#
#   Scenario: applied_for :
#
#
#    Given login with username 09022012056 and password as1234
#     And an order is added by following options for applying driver
#        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address            | destination_address        | receiver_mobile_phone |
#        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک 8 | خیابان دوم کوچه سوم پلاک 8  |                       |
#    And  call for order detail
#    When A new driver is sign up with number 09999999915
#    And a driver is assigned to order with number 09999999915
#    Then the status code for status update should be 200
##    And status should be applied_for
#    And turn the status back to cancelled
#    And the driver is deleted


#
#
#   Scenario: status progress : registered, waiting_agreement, waiting_complete_info(400)
#
#
#    Given login with username 09022012056 and password as1234
#     And an order is added by following options for applying driver
#        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address              | destination_address        | receiver_mobile_phone |
#        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک 8   | خیابان دوم کوچه سوم پلاک 8  | 09522252522           |
#    And  call for order detail
#    When A new driver is sign up with number 09999999915
#    And a driver is assigned to order with number 09999999915
#    Then update the status by modify_order to:
#     | status                |
#     | waiting_agreement     |
#     | waiting_complete_info |
#     | client_approved       |
#     | assigned              |
#     | pickedup              |
#
#     And order status code is
#     | code           |
#     | 200            |
#     | 400            |
#     | 200            |
#     | 200            |
#     | 200            |
#    And the driver is deleted


#
#
#  Scenario: upload barnaameh, assigned status
#
#    Given login with username 09022012056 and password as1234
#     And an order is added by following options for applying driver
#        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address               | destination_address        | receiver_mobile_phone |
#        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک      | خیابان دوم کوچه سوم پلاک 8  |                       |
#    And  call for order detail
#    When A new driver is sign up with number 09999999915
#    And a driver is assigned to order with number 09999999915
#    And update the status by modify_order to:
#     | status                |
#     | waiting_agreement     |
#     | waiting_complete_info |
#     | client_approved       |
#    And upload a new baarnameh
#    Then the status after add barnameh should be:
#     | status                |
#     | assigned              |
#
#    And the driver is deleted
#
#
#
#
#Scenario: picked_up , delivered
#
#    Given login with username 09022012056 and password as1234
#     And an order is added by following options for applying driver
#        | weight  | price    | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options    | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address             | destination_address        | receiver_mobile_phone |
#        | 2.5     | 350000   |کرمان        | ساری             | 21               | 16                    | نخود     | joft          | joft:hichkodam     |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09552020202         | ubaar         | sender       | 100000        | خیابان دوم کوچه سوم پلاک    | خیابان دوم کوچه سوم پلاک 8  |                       |
#    And  call for order detail
#    When A new driver is sign up with number 09999999915
#    And a driver is assigned to order with number 09999999915
#    And update the status by modify_order to:
#     | status                |
#     | waiting_agreement     |
#     | waiting_complete_info |
#     | client_approved       |
#    And upload a new baarnameh
#    Then update the status by modify_order to:
#     | status                |
#     | pickedup              |
#     | delivered             |
#
#    And the driver is deleted
