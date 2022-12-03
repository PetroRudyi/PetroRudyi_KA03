Feature: Pay Grades test om OrangeHRM

  Scenario: Pay Grades adding and editing
    Given we have driver initialized
    When we login successfully
     And we go to Pay Grades
     And we add new Pay Grades
    Then we have new Pay Grades appeared
     And we add new Currency
    Then we have new Currency
     And we remove Currency
     And we remove our Pay Grades