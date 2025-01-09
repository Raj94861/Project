Feature: open browser chrome and lauch demo url

Scenario Outline:open the browser and launch saucedemo web application
    Given user launch and open the browser chrome
    When User launch the url
    And User providing username and password
    And User select <item> and clicking add to cart button
#    Then enter the new user detail
    Examples:
        | item                |
        | Sauce Labs Backpack |