#Feature: Find suitable vehicle
#
#
#
#     Scenario: Find  vehicle types
#        Given login with username 09022012056 and password as1234
#        When Checking the suitable vehicle for:
#           | weight_load | length_load | width_load | height_load|
#           | 5           | 0           | 0          | 0          |
#        Then the vehicle type should be:
#            | type 1  | type 2  | type 3 | type 4  |
#            | khavar  | treili  | joft   | tak     |
#
#        And success flag for suitable vehicle is 1
#
#
#
#
#    Scenario: Find suitable vehicle options
#        Given login with username 09022012056 and password as1234
#        When Checking the suitable vehicle for:
#           | weight_load | length_load | width_load | height_load |
#           | 5           | 0           | 0          | 0           |
#           | 25          | 0           | 0          | 0           |
#           | 16          | 0           | 0          | 0           |
#           | 16          | 2           | 1          | 1           |
#
#        Then the vehicle options should be:
#            | 1                      | 2                      | 3                      | 4                      | 5                   | 6                  | 7                | 8                | 9                        | 10                     | 11               | 12           | 13                 | 14               | 15               | 16               | 17               | 18               | 19             | 20            | 21                 | 22                   |  23         | 24            | 25            | 26         | 27                   | 28          | 29                |
#            | khavar_mosaghaf_felezi | khavar_baghalbazsho    | hichkodam              | khavar_yakhchali       | khavar_kompressi    | khavar_roobaz      | treili_labehdar  | treili_nimlabeh  | treili_transit_chadori   | treili_baghalbazsho    | treili_kafi      | hichkodam    | treili_yakhchali   | treili_kompressi | treili_20foot    | treili_40foot    | treili_tigheh    | joft_yakhchali   | joft_kompressi | hichkodam     | joft_baghalbazsho  | joft_mosaghaf_felezi | joft_bari   | tak_yakhchali | tak_kompressi | hichkodam  | tak_mosaghaf_felezi  | tak_bari    | tak_baghalbazsho  |
#            | hichkodam              | treili_labehdar        | treili_nimlabeh        | treili_transit_chadori | treili_baghalbazsho | treili_kafi        | hichkodam        | treili_yakhchali | treili_kompressi         | treili_tigheh          | hichkodam        | hichkodam    |                    |                  |                  |                  |                  |                  |                |               |                    |                      |             |               |               |            |                      |             |                   |
#            | hichkodam              | treili_labehdar        | treili_nimlabeh        | treili_transit_chadori | treili_baghalbazsho | treili_kafi        | hichkodam        | treili_yakhchali | treili_kompressi         | treili_20foot          | treili_40foot    |treili_tigheh | joft_baghalbazsho  | hichkodam        | joft_bari        | joft_kompressi   | hichkodam        |                  |                |               |                    |                      |             |               |               |            |                      |             |                   |
#            | hichkodam              | treili_labehdar        | treili_nimlabeh        | treili_transit_chadori | treili_baghalbazsho | treili_kafi        | hichkodam        | treili_yakhchali | treili_kompressi         | treili_20foot          | treili_40foot    |treili_tigheh | joft_baghalbazsho  | hichkodam        | joft_bari        | joft_kompressi   | hichkodam        |                  |                |               |                    |                      |             |               |               |            |                      |             |                   |
#         And success flag for suitable vehicle is 1
#
#
#
#
#  Scenario: Find suitable truck dimensions
#        Given login with username 09022012056 and password as1234
#        When Checking the suitable dimensions for:
#           | weight_load | length_load | width_load | height_load |
#           | 1           | 0           | 0          | 0           |
#           | 5           | 5           | 2          | 2           |
#           | 25          | 0           | 0          | 0           |
#           | 16          | 0           | 0          | 0           |
#           | 16          | 2           | 1          | 1           |
#           | 27          | 0           | 0          | 0           |
#
#        Then the allowed dimensions is calculating
#        And success flag for suitable vehicle is 1
#
#
#
