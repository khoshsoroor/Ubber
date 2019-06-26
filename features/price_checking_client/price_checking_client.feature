# Created by pc at 4/24/2018

  Feature: check price after add order for client


  Scenario: successful get price after adding order for client
    Given login with username 09022012056 and password as1234
    When  An order is added by following options:
        | weight   | price  | source_city  | destination_city | source_region_id | destination_region_id | load_type | vehicle_type  | vehicle_options                | suspention_type       | load_value  | description  | sender_name    | sender_phone | sender_company  | receiver_name      | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address        | destination_address          | receiver_mobile_phone |
        | 5        | 150000 | تهران       | ساری             | 22               | 16                    | ابمیوه   | khavar        | khavar:khavar_mosaghaf_felezi  |                       | 10000000    | هیچی         | عسل عیار      | 09999999999  | سانا           | نوید              | 09999999999     | سانا             | karton          | 1      | 1     | 1      | yes       | day           | 09999999999         | ubaar         | sender       | 200000        |خیابان اول کوچه دوم | خیابان دوم کوچه سوم        | 09999999999           |
        | 2.5      | 100000 | کرمان       | ساری             | 21               | 16                    | نخود     | tak           | tak:tak_kompressi              |                       | 50000000    |               | محمد رضایی    | 09630213633  | سانا گستر     | وحید افشاری      | 09630213633     | Sana              | falleh          |        |       |        | yes       | day           | 09999999999         | ubaar         | sender       | 100000        |                      | خیابان دوم کوچه سوم پلاک 8  |                       |
        | 6        | 200000 | ساری        | ساری             | 16               | 16                    | میوه     | joft          | joft:hichkodam                 |                       | 100000000   | تخلیه ساعت 2 | رضا بینا      | 09552020202  | سانا گستر سبز | عباس ثابتی       | 09852222222     | سبز              | bandil          |        |       |        | yes       | day           | 09999999999         | ubaar         | receiver     | 100000        |                      |                               |                       |
        | 10       | 142500 | اصفهان      | تهران            | 3                | 22                    | اهن      | treili        | treili:treili_transit_chadori  | fanari                | 23000000    |               | علیرضا نوری   | 09658745222  | اوبار          |                   | 09552020202     |                  | kiseh_gooni     | 1.5    | 2.25  | 2      | yes       | night         | 09999999999         | ubaar         | sender       | 100000        |                      |                               |                       |
        | 5        | 785300 | کرمان       | تهران            | 21               | 22                    | پروفیل   | treili        | treili:treili_labehdar         | baloni                | 70000000    |               |                |              |                 |                   |                 |                  | hichkodam       | 1      | 2     | 2      | yes       | night         |                     | ubaar         | receiver     | 100000        |                      |                               |                       |

    Then The price is :
        | price      |
        | 131000     |
        | 70000      |
        | 140000     |
        | 116200     |
        | 678800     |


      Scenario: successful get price after adding order for barbari
    Given login with username 09000000011 and password as1234
    When  An order is added by following options:
        | weight   | price  | source_city  | destination_city | source_region_id | destination_region_id | load_type | vehicle_type  | vehicle_options                | suspention_type       | load_value  | description   | sender_name    | sender_phone | sender_company  | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address        | destination_address           | receiver_mobile_phone |
        | 5        | 150000 | تهران       | ساری             | 22               | 16                    | ابمیوه   | khavar        | khavar:khavar_mosaghaf_felezi  |                       | 10000000    | هیچی         | عسل عیار      | 09999999999  | سانا            | نوید            | 09999999999     | سانا             | karton          | 1      | 1     | 1      | yes       | day           | 09999999999         | ubaar         | sender       | 200000        |خیابان اول کوچه دوم | خیابان دوم کوچه سوم         | 09999999999           |
        | 2.5      | 100000 | کرمان       | ساری             | 21               | 16                    | نخود     | tak           | tak:tak_kompressi              |                       | 50000000    |               | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری    | 09630213633     | Sana              | falleh          |        |       |        | yes       | day           | 09999999999         | ubaar         | sender       | 100000        |                      | خیابان دوم کوچه سوم پلاک 8   |                       |
        | 6        | 200000 | ساری        | ساری             | 16               | 16                    | میوه     | joft          | joft:hichkodam                 |                       | 100000000   | تخلیه ساعت 2 | رضا بینا      | 09552020202  | سانا گستر سبز  | عباس ثابتی     | 09852222222     | سبز              | bandil          |        |       |        | yes       | day           | 09999999999         | ubaar         | receiver     | 100000        |                       |                               |                       |
        | 10       | 142500 | اصفهان      | تهران            | 3                | 22                    | اهن      | treili        | treili:treili_transit_chadori  | fanari                | 23000000    |               | علیرضا نوری   | 09658745222  | اوبار          |                  | 09552020202     |                  | kiseh_gooni     | 1.5    | 2.25  | 2      | yes       | night         | 09999999999         | ubaar         | sender       | 100000        |                       |                               |                       |
        | 5        | 785300 | کرمان       | تهران            | 21               | 22                    | پروفیل   | treili        | treili:treili_labehdar         | baloni                | 70000000    |               |                |              |                 |                  |                 |                  | hichkodam       | 1      | 2     | 2      | yes       | night         |                     | ubaar         | receiver     | 100000        |                       |                               |                       |

    Then The price is :
        | price      |
        | 150000     |
        | 100000     |
        | 200000     |
        | 142500     |
        | 785300     |


