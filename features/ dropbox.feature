Feature: Dropbox test

  Scenario: Upload normal-flow
    Given we upload file
    When we check file name
    Then we remove file