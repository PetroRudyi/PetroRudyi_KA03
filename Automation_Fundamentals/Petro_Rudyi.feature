# Created by Piter at 16.11.2022
Feature: EPAM Test cases

  Scenario: EPAM website works
    Given our web browser
    When we input "https://www.epam.com" into the browser
    Then EPAM website load

  Scenario: Search works
    Given go to "https://www.epam.com/search"
    When we print our request in field and press "FIND"
    Then page update and show result for our request

  Scenario: We don't have access to admin page
    Given we are not admin
    When we go to "https://www.epam.com/root"
    Then website show us 404 page

  Scenario Outline: Menu works in any size of browser size
    Given we are at "https://www.epam.com" in any size of window
    When we <menu> button
    Then <do> site show us menu points
    Examples:
      | menu       |        do            |
      | have       | press button "menu" and |
      | don't have |                         |

  Scenario: Main page access from any place
    Given go to any non-existent page
    When we press icon "EPAM" in the upper left corner
    Then website show us main page

  Scenario:  Contact Us button works
    Given we are at "https://www.epam.com"
    When we push "Contact us" button
    Then open "https://www.epam.com/about/who-we-are/contact" page

  Scenario:  EPAM's Facebook page works
    Given we are at "https://www.epam.com/"
    When we push Facebook icon
    Then open "https://www.facebook.com/EPAM.Global" page

  Scenario: Feedback send
    Given we are at "https://www.epam.com/about/who-we-are/contact"
    And we fill all fields
    When we push "SUBMIT" button
    Then we see a "thanks" message

