Feature: Leave Lifecycle
Background:
    Given user navigates to login page
    When user logs in with valid_user

  @leave
  Scenario: Leave lifecycle with entitlement

    Given admin creates leave type
    When admin assigns leave type to employee
    When user logs in with employee
    And employee applies leave using assigned type
    Then leave should be in pending status


#
#  Scenario: Full leave lifecycle
#    Given admin creates leave type
#
#    When employee applies for leave
#    Then leave should be in pending status
#
#    When manager approves leave request
#    Then leave should be approved
#    And leave balance should be deducted
#
#    When employee cancels the leave
#    Then leave balance should be restored
#
#    When employee applies overlapping leave
#    Then overlap error should be shown