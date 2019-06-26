  Feature:  order detail


  Scenario: successful check order details by client
    Given login with username 09022012056 and password as1234
    When add an order
    And  get order details
    Then check the order detail
    And success flag for order detail is 1
    And the status code for detail should be 200
