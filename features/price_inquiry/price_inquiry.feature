Feature: price inquiry


  Scenario: successful get price after order for client
    Given sign up and log in with username 09999999900 and password as1234
    When  get price for options like the following:
        | weight | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options                | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address     | destination_address        | receiver_mobile_phone |
        | 5      | تهران       | ساری             | 22               | 16                    | ابمیوه   | khavar        | khavar:khavar_mosaghaf_felezi  |                       | 10000000    | هیچی         | عسل عیار      | 09999999999  | سانا           | نوید             | 09999999999     | سانا             | karton          | 1      | 1     | 1      | yes       |                   | day           | 09999999999         | ubaar         | sender       | 200000        |خیابان اول کوچه دوم | خیابان دوم کوچه سوم        | 09999999999           |
        | 2.5    | کرمان       | ساری             | 21               | 16                    | نخود     | tak           | tak:tak_kompressi              |                       | 50000000    |              | محمد رضایی    | 09999999999  | سانا گستر      | وحید افشاری      | 09999999999     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09999999999         | ubaar         | sender       | 100000        |                    | خیابان دوم کوچه سوم پلاک 8  |                       |
        | 6      | ساری        | ساری             | 16               | 16                    | میوه     | joft          | joft:hichkodam                 |                       | 100000000   | تخلیه ساعت 2 | رضا بینا      | 09552020202  | سانا گستر سبز  | عباس ثابتی       | 09852222222     | سبز              | bandil          |        |       |        | no        | havaleh           | day           | 09999999999         | ubaar         | receiver     | 100000        |                    |                            |                       |
        | 10     | اصفهان      | تهران            | 3                | 22                    | اهن      | treili        | treili:treili_transit_chadori  | fanari                | 23000000    |              | علیرضا نوری   | 09658745222  | اوبار          |                  | 09552020202     |                  | kiseh_gooni     | 1.5    | 2.25  | 2      | yes       |                   | night         | 09999999999         | ubaar         | sender       | 100000        |                    |                            |                       |
        | 5      | کرمان       | تهران            | 21               | 22                    | پروفیل   | treili        | treili:treili_labehdar         | baloni                | 70000000    |              |               |              |                |                  |                 |                  | hichkodam       | 1      | 2     | 2      | no        | hichkodam         | night         |                     | ubaar         | receiver     | 100000        |                    |                            |                       |
    Then success flag for get price is 1
    And the response should be :
        | discount  | driver_income | max_acceptable_price | min_acceptable_price | order_credit  | predicted_price | status         | status_farsi       | tavafoghi_flag |
        | 0         | 0             | 215000               | 140000               | 0             | 165000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 870000               | 569000               | 0             | 669400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 191000               | 125000               | 0             | 147000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 852000               | 557000               | 0             | 655400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 1167000              | 763000               | 0             | 897600          | reject_price   | "عدم پذیرش قیمت"   | 0              |

    And status for price inquiry is 200






  Scenario: successful get price after order for barbari
    Given login with username 09000000011 and password as1234
    When  get price for options like the following:
        | weight   | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options                | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address     | destination_address        | receiver_mobile_phone |
        | 5        | تهران       | ساری             | 22               | 16                    | ابمیوه   | khavar        | khavar:khavar_mosaghaf_felezi  |                       | 10000000    | هیچی         | عسل عیار      | 09999999999  | سانا           | نوید             | 09999999999     | سانا             | karton          | 1      | 1     | 1      | yes       | day           | 09999999999         | ubaar         | sender       | 200000        |خیابان اول کوچه دوم | خیابان دوم کوچه سوم        | 09999999999           |
        | 2.5      | کرمان       | ساری             | 21               | 16                    | نخود     | tak           | tak:tak_kompressi              |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       | day           | 09999999999         | ubaar         | sender       | 100000        |                    | خیابان دوم کوچه سوم پلاک 8  |                       |
        | 6        | ساری        | ساری             | 16               | 16                    | میوه     | joft          | joft:hichkodam                 |                       | 100000000   | تخلیه ساعت 2 | رضا بینا      | 09552020202  | سانا گستر سبز  | عباس ثابتی       | 09852222222     | سبز              | bandil          |        |       |        | yes       | day           | 09999999999         | ubaar         | receiver     | 100000        |                    |                            |                       |
        | 10       | اصفهان      | تهران            | 3                | 22                    | اهن      | treili        | treili:treili_transit_chadori  | fanari                | 23000000    |              | علیرضا نوری   | 09658745222  | اوبار          |                  | 09552020202     |                  | kiseh_gooni     | 1.5    | 2.25  | 2      | yes       | night         | 09999999999         | ubaar         | sender       | 100000        |                    |                            |                       |
        | 5        | کرمان       | تهران            | 21               | 22                    | پروفیل   | treili        | treili:treili_labehdar         | baloni                | 70000000    |              |               |              |                |                  |                 |                  | hichkodam       | 1      | 2     | 2      | yes       | night         |                     | ubaar         | receiver     | 100000        |                    |                            |                       |
    Then success flag for get price is 1
    And the response should be :
        | discount  | driver_income | max_acceptable_price | min_acceptable_price | order_credit  | predicted_price | status         | status_farsi       | tavafoghi_flag |
        | 0         | 0             | 215000               | 140000               | 0             | 165000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 870000               | 569000               | 0             | 669400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 191000               | 125000               | 0             | 147000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 852000               | 557000               | 0             | 655400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 0                    | 0                    | 0             | 0               | reject_price   | "عدم پذیرش قیمت"   | 1              |

    And status for price inquiry is 200




  Scenario: successful get price after order for admin
    Given Admin logs in with email test@gmail.com and password is ATpl124SC
    When  get price for options like the following:
        | weight   |source_city  | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options                | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | baarnameh_options | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address     | destination_address        | receiver_mobile_phone |
        | 5        | تهران       | ساری             | 22               | 16                    | ابمیوه   | khavar        | khavar:khavar_mosaghaf_felezi  |                       | 10000000    | هیچی         | عسل عیار      | 09999999999  | سانا           | نوید             | 09999999999     | سانا             | karton          | 1      | 1     | 1      | yes       |                   | day           | 09999999999         | ubaar         | sender       | 200000        |خیابان اول کوچه دوم | خیابان دوم کوچه سوم        | 09999999999           |
        | 2.5      | کرمان       | ساری             | 21               | 16                    | نخود     | tak           | tak:tak_kompressi              |                       | 50000000    |              | محمد رضایی    | 09999999999  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | yes       |                   | day           | 09999999999         | ubaar         | sender       | 100000        |                    | خیابان دوم کوچه سوم پلاک 8  |                       |
        | 6        | ساری        | ساری             | 16               | 16                    | میوه     | joft          | joft:hichkodam                 |                       | 100000000   | تخلیه ساعت 2 | رضا بینا      | 09552020202  | سانا گستر سبز  | عباس ثابتی       | 09852222222     | سبز              | bandil          |        |       |        | no        | havaleh           | day           | 09999999999         | ubaar         | receiver     | 100000        |                    |                            |                       |
        | 10       | اصفهان      | تهران            | 3                | 22                    | اهن      | treili        | treili:treili_transit_chadori  | fanari                | 23000000    |              | علیرضا نوری   | 09658745222  | اوبار          |                  | 09552020202     |                  | kiseh_gooni     | 1.5    | 2.25  | 2      | yes       |                   | night         | 09999999999         | ubaar         | sender       | 100000        |                    |                            |                       |
        | 5        | کرمان       | تهران            | 21               | 22                    | پروفیل   | treili        | treili:treili_labehdar         | baloni                | 70000000    |              |               |              |                |                  |                 |                  | hichkodam       | 1      | 2     | 2      | no        | hichkodam         | night         |                     | ubaar         | receiver     | 100000        |                    |                            |                       |

    Then success flag for get price is 1
    And the response should be :
        | discount  | driver_income | max_acceptable_price | min_acceptable_price | order_credit  | predicted_price | status         | status_farsi       | tavafoghi_flag |
        | 0         | 0             | 215000               | 140000               | 0             | 165000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 870000               | 569000               | 0             | 669400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 191000               | 125000               | 0             | 147000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 852000               | 557000               | 0             | 655400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 1167000              | 763000               | 0             | 897600          | reject_price   | "عدم پذیرش قیمت"   | 0              |

    And status for price inquiry is 200



   Scenario: unsuccessful price inquiry for client
    Given login with username 09022012056 and password as1234
    When  get price for options like the following:
        | weight  | source_city | destination_city | source_region_id | destination_region_id | load_type| vehicle_type  | vehicle_options                | suspention_type       | load_value  | description  | sender_name   | sender_phone | sender_company | receiver_name    | receiver_phone  | receiver_company | package_options | length | width | height | baarnameh | unload_option | sender_mobile_phone | announce_type | payment_type | surplus_costs | source_address     | destination_address        | receiver_mobile_phone |
        | 5       | تهران       | ساری             | 800              | 16                    | ابمیوه   | khavar        | khavar:khavar_mosaghaf_felezi  |                       | 10000000    | هیچی         | عسل عیار      | 09999999999  | سانا           | نوید             | 09999999999     | سانا             | karton          | 1      | 1     | 1      | yes       | day           | 09999999999         | mydrivers     | sender       | 200000        |خیابان اول کوچه دوم | خیابان دوم کوچه سوم        | 09999999999           |
        | 100     | کرمان       | ساری             | 21               | 16                    | نخود     | tak           | tak:tak_kompressi              |                       | 50000000    |              | محمد رضایی    | 09630213633  | سانا گستر      | وحید افشاری      | 09630213633     | Sana             | falleh          |        |       |        | no        | day           | 09999999999         | ubaar         | sender       | 100000        |                    | خیابان دوم کوچه سوم پلاک 8  |                       |
        | 6       | ساری        | ساری             | 16               | 16                    | میوه     | joft          | joft                           |                       | 100000000   | تخلیه ساعت 2 | رضا بینا      | 09552020202  | سانا گستر سبز  | عباس ثابتی       | 09852222222     | سبز              | bandil          | 40     |       |        | yes       | day           | 09999999999         | ubaar         | receiver     | 100000        |                    |                            |                       |
        | 10      | اصفهان      | تهران            | 3                | 22                    | اهن      | treili        | treili:treili_transit_chadori  | fanari                | 23000000    |              | علیرضا نوری   | 09658745222  | اوبار          |                  | 09552020202     |                  |                 | 1.5    | 2.25  | 2      | no        | night         | 09999999999         | ubaar         | sender       | 100000        |                    |                            |                       |
        | 5       | کرمان       | تهران            | 21               | 22                    | پروفیل   | tak           | joft:hichkodam                 | baloni                | 70000000    |              |               |              |                |                  |                 |                  | hichkodam       | 1      | 2     | 2      | yes       | night         |                     | ubaar         | receiver     | 100000        |                    |                            |                       |

    Then success flag for get price is 0
    And the response should be :
        | discount  | driver_income | max_acceptable_price | min_acceptable_price | order_credit  | predicted_price | status         | status_farsi       | tavafoghi_flag |
        | 0         | 0             | 215000               | 140000               | 0             | 165000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 870000               | 569000               | 0             | 669400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 191000               | 125000               | 0             | 147000          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 852000               | 557000               | 0             | 655400          | reject_price   | "عدم پذیرش قیمت"   | 0              |
        | 0         | 0             | 1167000              | 763000               | 0             | 897600          | reject_price   | "عدم پذیرش قیمت"   | 0              |
    And status for price inquiry is 400
