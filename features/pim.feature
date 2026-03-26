Feature: Employee Management - PIM
  Background:
    Given user navigates to login page
    When user logs in with valid_user

  @pim @pipeline
  Scenario: Full employee lifecycle
    Given user is on PIM page
    When user adds a new employee
      Then employee should be created with employee id
    When user searches for the employee
      Then employee should appear in search results
    When user edits employee details
      Then changes should be saved
    When user deletes the employee
      Then employee should be removed from list