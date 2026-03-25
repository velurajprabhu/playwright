Feature: Login functionality

  Scenario: Valid login
    Given user navigates to login page
    When user logs in with username "Admin" and password "admin123"
    Then user should see dashboard

  Scenario: Invalid login
    Given user navigates to login page
    When user logs in with username "wrong" and password "wrong"
    Then user should see login error message

