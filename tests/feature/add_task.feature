Feature: Add New Task
  As a user
  I want to add a new task
  So that I can organize my work

Scenario: Adding a task with title and description
  Given the task list is empty
  When I add a task with title "Complete Homework" and description "Finish math and science homework"
  Then the task list should contain a task titled "Complete Homework"