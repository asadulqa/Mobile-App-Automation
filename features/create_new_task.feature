
Feature: Create New TO DO List Task
  # There is five type of list, It will create five different task for each type of list and closed.

  Scenario: Create "Default" Task!
    Given At First Open "To Do List" App
    When Click on "+" Icon
    Then Enter Task Name In The Input Section
    Then Click On Calendar Section And Select Date
    Then Click On "Ok" Button
    Then Click On Time Section
    Then Click On "Ok" Button
    Then Click On "Tick Mark" Icon
    Then Verify The task In List
    Then Click On Close Task Box, It Will Closed The Task
    Then Verify The Task Is Closed

  Scenario: Create "Personal" Task!
    Given At First Open "To Do List" App
    When Click on "+" Icon
    Then Enter Task Name In The Input Section
    Then Click On Calendar Section And Select Date
    Then Click On "Ok" Button
    Then Click On Time Section
    Then Click On "Ok" Button
    Then Click On "Default DropDown" Section And Select "Personal"
    Then Click On "Tick Mark" Icon
    Then Verify The task In List
    Then Click On Close Task Box, It Will Closed The Task
    Then Verify The Task Is Closed

  Scenario: Create "Shopping" Task!
    Given At First Open "To Do List" App
    When Click on "+" Icon
    Then Enter Task Name In The Input Section
    Then Click On Calendar Section And Select Date
    Then Click On "Ok" Button
    Then Click On Time Section
    Then Click On "Ok" Button
    Then Click On "Default DropDown" Section And Select "Shopping"
    Then Click On "Tick Mark" Icon
    Then Verify The task In List
    Then Click On Close Task Box, It Will Closed The Task
    Then Verify The Task Is Closed

  Scenario: Create "Wishlist" Task!
    Given At First Open "To Do List" App
    When Click on "+" Icon
    Then Enter Task Name In The Input Section
    Then Click On Calendar Section And Select Date
    Then Click On "Ok" Button
    Then Click On Time Section
    Then Click On "Ok" Button
    Then Click On "Default DropDown" Section And Select "Wishlist"
    Then Click On "Tick Mark" Icon
    Then Verify The task In List
    Then Click On Close Task Box, It Will Closed The Task
    Then Verify The Task Is Closed

  Scenario: Create "Work" Task!
    Given At First Open "To Do List" App
    When Click on "+" Icon
    Then Enter Task Name In The Input Section
    Then Click On Calendar Section And Select Date
    Then Click On "Ok" Button
    Then Click On Time Section
    Then Click On "Ok" Button
    Then Click On "Default DropDown" Section And Select "Work"
    Then Click On "Tick Mark" Icon
    Then Verify The task In List
    Then Click On Close Task Box, It Will Closed The Task
    Then Verify The Task Is Closed

