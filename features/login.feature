Feature: Login functionality

  @login @pipeline
  Scenario: Valid login
    Given user navigates to login page
    When user logs in with valid_user
    Then user should see dashboard
    Then user logout of the application
    Then session should not persist after logout

  @login @pipeline
  Scenario Outline: Invalid login
    Given user navigates to login page
    When user logs in with <user>
    Then user should see login error message for <user>
    Examples:
      |user |
    | invalid_username    |
    | invalid_password    |

  @login @pipeline
  Scenario: Empty credentials
    Given user navigates to login page
    When user logs in with empty_credentials
    Then validation messages should be displayed for empty_credentials