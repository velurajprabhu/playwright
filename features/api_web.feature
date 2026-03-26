Feature: API + UI Hybrid

  @api @pipeline
  Scenario: Employee lifecycle via API and UI
    When employee is created via API
    Then employee should appear in UI
    Then employee list from API should match UI
    When leave is applied via API
    Then leave should be visible in UI
    When leave is approved via API
    Then leave status should be updated in UI
    Then employee should be deleted via API