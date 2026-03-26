Feature: Performance Validation

  @performance @pipeline
  Scenario: Login performance validation
    When user loads login page with performance check

  @performance @pipeline
  Scenario: Dashboard load performance using browser API
    Given user navigates to login page
    When user logs in with valid_user
    Then dashboard should load within 3 seconds using browser metrics

  @performance @pipeline
  Scenario: Employee list page load performance
    Given user navigates to login page
    When user logs in with valid_user
    When user navigates to employee list with performance tracking
    Then employee list should load within 3 seconds using browser metrics

  @performance
  Scenario: Create employee performance using browser API
    Given user navigates to login page
    When user logs in with valid_user
    When user creates employee with browser performance tracking
    Then employee creation should complete within 2 seconds using browser metrics