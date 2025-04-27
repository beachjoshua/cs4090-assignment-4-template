import pytest
from behave import given, when, then

tasks = []

@given("the task list is empty")
def step_impl(context):
    global tasks
    tasks = []

@when('I add a task with title "{title}" and description "{description}"')
def step_impl(context, title, description):
    tasks.append({"title": title, "description": description})

@then('the task list should contain a task titled "{title}"')
def step_impl(context, title):
    titles = [task["title"] for task in tasks]
    assert title in titles
