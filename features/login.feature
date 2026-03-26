Feature: Login functionality

  @login
  Scenario: Valid login
    Given user navigates to login page
    When user logs in with valid_user
    Then user should see dashboard

  @login
  Scenario Outline: Invalid login
    Given user navigates to login page
    When user logs in with <user>
    Then user should see login error message for <user>
    Examples:
      |user |
    | invalid_username    |
    | invalid_password    |



